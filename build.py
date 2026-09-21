#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Der Erzeuger.

Nimmt die Seitenbeschreibungen aus src/seiten/, setzt Kopf, Navigation und
Fuss darum und schreibt statisches HTML in den Projektordner. Kein Node, kein
Framework, keine Abhaengigkeit ausser der Standardbibliothek – aus demselben
Grund, aus dem das CMS ohne Composer auskommt: Was nicht da ist, kann nicht
kaputtgehen.

    python3 build.py

Das Ergebnis liegt danach im Projektordner und laesst sich unveraendert auf
jeden Webspace, auf GitHub Pages oder hinter einen beliebigen Webserver legen.
"""

import os
import re
import shutil
import sys
from datetime import date

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "src"))

import daten as D                      # noqa: E402
import layout as L                     # noqa: E402
from seiten import ALLE_SEITEN         # noqa: E402


# Verzeichnisse, die der Erzeuger erzeugt und darum auch aufraeumen darf.
ERZEUGT = [
    "produkt", "funktionen", "demo", "fuer-golfpros", "fuer-golflehrer",
    "fuer-golfakademien", "vorteile", "preise", "faq", "ueber-uns", "kontakt",
    "impressum", "datenschutz",
]


def schreiben(pfad, inhalt):
    voll = os.path.join(HIER, pfad.lstrip("/"))
    os.makedirs(os.path.dirname(voll), exist_ok=True)
    with open(voll, "w", encoding="utf-8") as f:
        f.write(inhalt)
    return len(inhalt.encode("utf-8"))


def seite_bauen(seite):
    teile = [
        L.kopf_html(seite),
        '<a class="sprung" href="#inhalt">Zum Inhalt springen</a>',
        L.kopfzeile(seite.get("aktiv", seite["pfad"]), band=seite.get("band", True)),
    ]
    if seite.get("krumen"):
        teile.append(L.krumen(seite["krumen"]))
    teile.append('<main id="inhalt">')
    teile.append(seite["inhalt"])
    teile.append("</main>")
    teile.append(L.fuss_html(mit_sticky=seite.get("sticky", True)))
    return "\n".join(teile)


# --------------------------------------------------------------- Verweise --

_VERWEIS = re.compile(r'\b(href|src)="(/[^"/][^"]*|/)"')


def relativ_machen(html, seitenpfad):
    """Absolute Verweise in Verweise relativ zu dieser Seite umschreiben.

    Der Grund: Eine Seite, die mit ``/assets/css/site.css`` auf ihr
    Stylesheet zeigt, findet es nur, wenn sie an der Wurzel einer Domain
    liegt. Per Doppelklick (``file://``) sucht der Browser dann im
    Wurzelverzeichnis der Festplatte, auf GitHub Pages unter
    ``benutzer.github.io/assets/…`` – beides ist falsch, und die Seite
    erscheint ohne Gestaltung und ohne Bilder.

    Deshalb bekommt jede Seite ihre eigenen Verweise, gerechnet aus ihrer
    Tiefe. Seitenverweise enden dabei auf ``index.html``: Ohne Server gibt
    es kein Verzeichnisverzeichnis, ein Verweis auf einen Ordner öffnet
    also nichts.

    Meta-Angaben bleiben unberührt – ``canonical`` und ``og:image`` stehen
    als vollständige Adresse in ``content``/``href`` mit ``https://`` davor
    und werden vom Muster gar nicht erst erfasst.
    """
    tiefe = 0 if ziel_datei(seitenpfad) == os.path.basename(ziel_datei(seitenpfad)) \
            else ziel_datei(seitenpfad).count("/")
    hoch = "../" * tiefe

    def ersetzen(treffer):
        attribut, ziel = treffer.group(1), treffer.group(2)

        # Anker und Abfrage abtrennen, damit /funktionen/#kunden heil bleibt
        rest = ""
        for zeichen in "#?":
            if zeichen in ziel:
                ziel, _, schwanz = ziel.partition(zeichen)
                rest = zeichen + schwanz + rest
                break

        if ziel == "/":
            neu = "index.html"
        elif ziel.endswith("/"):
            neu = ziel.strip("/") + "/index.html"
        else:
            neu = ziel.lstrip("/")

        return '%s="%s%s%s"' % (attribut, hoch, neu, rest)

    return _VERWEIS.sub(ersetzen, html)


def ziel_datei(pfad):
    if pfad == "/":
        return "index.html"
    if pfad.endswith(".html"):
        return pfad.lstrip("/")
    return pfad.strip("/") + "/index.html"


def sitemap(seiten):
    heute = date.today().isoformat()
    eintraege = []
    for s in seiten:
        if s.get("noindex"):
            continue
        prio = "1.0" if s["pfad"] == "/" else ("0.8" if s["pfad"].count("/") <= 2 else "0.6")
        eintraege.append(
            "  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>"
            % (D.BASIS_URL.rstrip("/"), s["pfad"], heute, prio)
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(eintraege) + "\n</urlset>\n")


def robots():
    return ("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n"
            % D.BASIS_URL.rstrip("/"))


def favicon():
    """Dasselbe Zeichen wie im Kopf: Fahnenstock, dessen Tuch ein
    Inhaltsblock ist. Auf gruener Flaeche, damit es im Tab auch auf hellem
    wie dunklem Browserchrom steht."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        '<rect width="32" height="32" rx="7" fill="#17352b"/>'
        '<rect x="12.5" y="6" width="14" height="10.5" rx="1.5" fill="#fffefb"/>'
        '<path d="M15.8 9.8h7.4M15.8 13h4.4" stroke="#17352b" stroke-width="1.7" '
        'stroke-linecap="round"/>'
        '<path d="M11.6 5v21.5" stroke="#fffefb" stroke-width="2.6" stroke-linecap="round"/>'
        '<path d="M6.5 26.5h10.2" stroke="#c8b795" stroke-width="2.4" stroke-linecap="round"/>'
        "</svg>"
    )


def aufraeumen():
    """Alte Ausgabe entfernen, damit geloeschte Seiten nicht liegen bleiben."""
    for ordner in ERZEUGT:
        voll = os.path.join(HIER, ordner)
        if os.path.isdir(voll):
            shutil.rmtree(voll)


def main():
    aufraeumen()

    gesamt = 0
    seiten = ALLE_SEITEN()
    pfade = set()

    for seite in seiten:
        if seite["pfad"] in pfade:
            raise SystemExit("Doppelter Pfad: %s" % seite["pfad"])
        pfade.add(seite["pfad"])
        html = seite_bauen(seite)
        if getattr(D, "PFADE", "relativ") == "relativ":
            html = relativ_machen(html, seite["pfad"])
        groesse = schreiben(ziel_datei(seite["pfad"]), html)
        gesamt += groesse
        print("  %-34s %6.1f KB" % (seite["pfad"], groesse / 1024))

    schreiben("sitemap.xml", sitemap(seiten))
    schreiben("robots.txt", robots())
    schreiben("assets/img/favicon.svg", favicon())

    print()
    print("  %d Seiten, %.1f KB HTML" % (len(seiten), gesamt / 1024))


if __name__ == "__main__":
    main()
