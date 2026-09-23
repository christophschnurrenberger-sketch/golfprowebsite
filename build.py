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

import hashlib
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


# Jede Datei unter assets/ bekommt ihren Inhalts-Fingerabdruck in die
# Adresse: site.css?v=3fa9c2d1. Der Server darf sie dann ein Jahr lang im
# Browser liegen lassen, und trotzdem kommt jede Aenderung sofort an - weil
# eine geaenderte Datei eine neue Adresse hat. Vorher hiess site.css nach
# jeder Aenderung wieder site.css, und wer die Seite kannte, sah bis zu
# einem Monat lang das alte Stylesheet zum neuen HTML.
#
# Schriften sind ausgenommen: Sie aendern sich nie unter demselben Namen
# (eine neue Schrift ist eine neue Datei), und das Vorladen im Kopf muss
# genau dieselbe Adresse treffen wie schriften.css - sonst laedt der
# Browser jede Schrift zweimal.
_ASSET = re.compile(r'\b(href|src|content)="([^"]*?)(assets/[^"?#]+)"')
_FINGERABDRUCK = {}


def fingerabdruck(pfad):
    if pfad not in _FINGERABDRUCK:
        voll = os.path.join(HIER, pfad)
        if not os.path.isfile(voll):
            _FINGERABDRUCK[pfad] = None
        else:
            with open(voll, "rb") as f:
                _FINGERABDRUCK[pfad] = hashlib.md5(f.read()).hexdigest()[:8]
    return _FINGERABDRUCK[pfad]


def versionieren(html):
    def ersetzen(t):
        attribut, davor, pfad = t.group(1), t.group(2), t.group(3)
        if pfad.startswith("assets/fonts/"):
            return t.group(0)
        v = fingerabdruck(pfad)
        if not v:
            return t.group(0)
        return '%s="%s%s?v=%s"' % (attribut, davor, pfad, v)
    return _ASSET.sub(ersetzen, html)


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
    """Das TP-Monogramm, wie es in lib/Marke.php des Produkts steht.

    T und P teilen sich einen Stamm; die Schale des P ist derselbe Bogen
    wie im Bildzeichen. Als Monogramm und nicht als Bildzeichen, weil ein
    Favicon 16 Pixel gross wird - darunter zerfaellt ein Punkt mit einer
    Linie zu zwei Flecken.
    """
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
        '<rect width="100" height="100" rx="26" fill="#0b2b22"/>'
        '<path d="M39 22V78" stroke="#f6f5f0" stroke-width="11" '
        'stroke-linecap="round" fill="none"/>'
        '<path d="M20 22H39" stroke="#f6f5f0" stroke-width="11" '
        'stroke-linecap="round" fill="none"/>'
        '<path d="M39 22C66 22 80 30 80 39.5C80 49 66 56 39 56" '
        'stroke="#c3e35c" stroke-width="11" stroke-linecap="round" fill="none"/>'
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
    # Vor den Seiten: Ihr Fingerabdruck steht in jeder Seite.
    schreiben("assets/img/favicon.svg", favicon())

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
        html = versionieren(html)
        groesse = schreiben(ziel_datei(seite["pfad"]), html)
        gesamt += groesse
        print("  %-34s %6.1f KB" % (seite["pfad"], groesse / 1024))

    schreiben("sitemap.xml", sitemap(seiten))
    schreiben("robots.txt", robots())

    print()
    print("  %d Seiten, %.1f KB HTML" % (len(seiten), gesamt / 1024))


if __name__ == "__main__":
    main()
