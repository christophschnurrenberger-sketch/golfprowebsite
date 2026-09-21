#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schneidet die Menue-Vorschauen aus den Original-Aufnahmen.

Die Navigation zeigt rechts eine Vorschau des Bereichs, auf dem der Zeiger
steht. Frueher war das die ganze Aufnahme, in einen 400 Pixel breiten Rahmen
geschrumpft – 28 Prozent der Originalgroesse. Man sah, dass da eine Oberflaeche
ist, aber nicht, was drinsteht. Jetzt steht dort ein Ausschnitt in
Originalgroesse: dieselbe Schriftgroesse wie im Programm selbst.

    python3 ausschnitte.py /pfad/zu/den/originalen

Die Originale sind die unverkleinerten PNG-Dateien der Aufnahmen
(2880 x 1800, also doppelte Aufloesung eines 1440 x 900 grossen Fensters).
Sie liegen nicht im Repository – sie entstehen bei der Aufnahme des
Programms und sind zusammen ueber 200 MB gross. Das Ergebnis dieses
Skripts liegt im Repository: assets/img/nav/.

Wer die Ausschnitte verschieben will, aendert AUSSCHNITTE in src/daten.py
und laesst das Skript noch einmal laufen. Danach build.py.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

import daten as D  # noqa: E402

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow fehlt:  pip3 install Pillow")

# Der Rahmen im Menue ist 400 x 250 gross. Wir liefern hoechstens das
# Doppelte, damit er auf feinen Bildschirmen scharf bleibt – und nie mehr,
# als im Original steckt: Ein kleiner Ausschnitt kuenstlich vergroessert
# waere wieder unscharf, und unscharf war ja das Problem.
BREITE, HOEHE = 800, 500
ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "assets", "img", "nav")


def schneiden(quelle):
    os.makedirs(ZIEL, exist_ok=True)
    fehlt, fertig = [], 0

    for name, werte in sorted(D.AUSSCHNITTE.items()):
        x, y, breite, hoehe = werte[:4]
        pfad = os.path.join(quelle, name + ".png")
        if not os.path.exists(pfad):
            fehlt.append(name)
            continue

        bild = Image.open(pfad).convert("RGB")
        # Die Aufnahme ist doppelt so gross wie das Fenster, in dem sie
        # entstanden ist. Die Koordinaten in daten.py sind Fensterkoordinaten.
        faktor = bild.width / 1440.0
        kasten = (round(x * faktor), round(y * faktor),
                  round((x + breite) * faktor), round((y + hoehe) * faktor))
        if kasten[2] > bild.width or kasten[3] > bild.height:
            sys.exit("%s: Ausschnitt liegt ausserhalb der Aufnahme %s"
                     % (name, bild.size))

        stueck = bild.crop(kasten)
        ziel = (min(BREITE, stueck.width), min(HOEHE, stueck.height))
        if stueck.size != ziel:
            stueck = stueck.resize(ziel, Image.LANCZOS)

        stueck.save(os.path.join(ZIEL, name + ".webp"),
                    "WEBP", quality=88, method=6)
        fertig += 1
        print("  %-22s Fenster %4d x %-4d  Datei %d x %d"
              % (name, breite, hoehe, stueck.width, stueck.height))

    print("\n%d Ausschnitte in assets/img/nav/" % fertig)
    if fehlt:
        print("Nicht gefunden: %s" % ", ".join(fehlt))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__.strip().splitlines()[0] +
                 "\n\n  python3 ausschnitte.py /pfad/zu/den/originalen")
    schneiden(sys.argv[1])
