# -*- coding: utf-8 -*-
"""Sammelstelle aller Seiten. Die Reihenfolge bestimmt die Ausgabe der Sitemap."""

from . import start, produkt, demo, zielgruppen, rest


def ALLE_SEITEN():
    return [
        start.bauen(),

        produkt.produkt(),
        produkt.funktionen(),
        produkt.dashboard(),
        produkt.website(),
        produkt.kurse(),
        produkt.buchungen(),

        demo.demo(),
        demo.tour(),
        demo.beispiel(),
        demo.screenshots(),
        demo.linkedin(),

        zielgruppen.golfpros(),
        zielgruppen.golflehrer(),
        zielgruppen.golfakademien(),

        rest.vorteile(),
        rest.preise(),
        rest.faq(),
        rest.ueber_uns(),
        rest.kontakt(),
        rest.impressum(),
        rest.datenschutz(),
        rest.vierhundertvier(),
    ]
