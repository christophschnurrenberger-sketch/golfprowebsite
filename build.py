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
    """Ein Fähnchen im Markengrün – als SVG, damit es überall scharf ist."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        '<rect width="32" height="32" rx="7" fill="#0d6b4f"/>'
        '<g fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" '
        'stroke-linejoin="round">'
        '<path d="M10 25V8.5s1.4-1.2 4.6-1.2S19.6 9.8 22 9.8s2.4-.7 2.4-.7v9.6s-1 .8-3.2.8'
        'c-2.8 0-4.6-2.3-7.8-2.3-2.4 0-3.4 1-3.4 1"/></g></svg>'
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
        groesse = schreiben(ziel_datei(seite["pfad"]), seite_bauen(seite))
        gesamt += groesse
        print("  %-34s %6.1f KB" % (seite["pfad"], groesse / 1024))

    schreiben("sitemap.xml", sitemap(seiten))
    schreiben("robots.txt", robots())
    schreiben("assets/img/favicon.svg", favicon())

    print()
    print("  %d Seiten, %.1f KB HTML" % (len(seiten), gesamt / 1024))


if __name__ == "__main__":
    main()
