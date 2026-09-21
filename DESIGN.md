# Art Direction

Warum die Website so aussieht, wie sie aussieht – und woran man merken
würde, dass jemand davon abgewichen ist.

---

## Die Regel, aus der alles folgt

**Keine zwei Abschnitte hintereinander sehen gleich aus.**

Das ist keine Geschmacksfrage. Ein Kachelraster nach dem anderen ist das
Erkennungsmerkmal automatisch zusammengesetzter Seiten, und eine Website,
die so aussieht, macht ihr Produkt unglaubwürdig, bevor der erste Satz
gelesen ist.

Konkret auf der Startseite:

```
Aufmacher, asymmetrisch      Text links, Produkt rechts und tiefer
Aussage                      nur Typografie, sonst nichts
Produkt über volle Breite    ein Screenshot, eine Legende
Fünf Kapitel                 01–05, Bild wechselt die Seite
Split-Screen                 CMS | Linie | Website
Ablauf                       eine Kette, keine vier Kästen
Dunkler Moment               Markenaussage, ein Screenshot
Beispielwebsite              Gerätewechsler
Heute / danach               zwei Listen, keine Ampelfarben
Für wen                      typografische Liste
Umfang                       Liste, kein Kaufknopf
Fragen                       Haarlinien und ein Plus
Schluss                      dunkel, linksbündig
```

---

## Was gezählt wurde

Beim Umbau nachgemessen, nicht geschätzt:

| | vorher | nachher |
|---|---:|---:|
| Karten site-weit | 192 | 0 |
| Icon-Kreise | 61 | 0 |
| zentrierte Blöcke | 33 | 13 |
| nummerierte Kapitel | 0 | 5 |
| typografische Listen | 0 | 24 |

Karten sind nicht verboten – aber jede einzelne muss sich rechtfertigen.
Auf dieser Website hat es keine geschafft.

---

## Farbe

Der Großteil der Fläche ist warmes Off-White. Grün ist Marken- und
Akzentfarbe, nicht Grundton.

| | | Verwendung |
|---|---|---|
| `--papier` | `#f6f4ee` | Grundfläche, rund zwei Drittel der Seite |
| `--papier-2` | `#edeae1` | abgesetzte Bänder |
| `--gruen` | `#17352b` | Knöpfe, Marke, Links |
| `--gruen-tief` | `#0f241d` | dunkle Abschnitte, Fußzeile |
| `--salbei` | `#a7b6a8` | Linien, Kapitelnummern, ruhige Akzente |
| `--sand` | `#c8b795` | der einzige warme Akzent, sehr sparsam |
| `--tinte` | `#202522` | Text |

**Kein gelber Textmarker.** Das Produkt benutzt ihn auf seinen eigenen
Websites; auf der Marketingseite wäre er die lauteste Stelle. Stattdessen
liegt eine Sandlinie unter dem hervorgehobenen Wort.

---

## Typografie

Archivo, dieselbe Datei wie im Produkt. Caveat nur für einen einzigen
handschriftlichen Einwurf.

* Aufmacher `clamp(44px, 5.6vw, 80px)` – groß, aber nicht 140px
* Zeilenhöhe 0.98 bis 1.04 bei Überschriften
* Fließtext nie breiter als 680px
* Überschriften werden in `ch` begrenzt, **am Element selbst** – `ch` bezieht
  sich auf die Schriftgröße des Elements, und am Container mit 17px
  Grundschrift ergäben 20ch rund 350px. Deutsche Komposita brauchen ohnehin
  mehr Lauflänge als englische.

---

## Linien statt Schatten

Tiefe entsteht über Überlagerung, Fläche und Position – nicht über
Weichzeichner. Schatten sind kaum sichtbar, Ränder sind 1px Haarlinien.

Rundungen: Knöpfe 7px, Flächen 10px, Screenshots 12px. Nichts ist
pillenförmig.

---

## Fotografie

**Es sind keine Fotos enthalten.** Das ist die eine Anforderung, die nicht
erfüllt ist, und der Grund ist technisch: Aus der Umgebung, in der diese
Website gebaut wurde, war keine Bildquelle erreichbar.

Die Website ist deshalb so gebaut, dass sie ohne Fotos **fertig** aussieht:
Wo kein Foto liegt, entfällt der Abschnitt oder es steht eine typografische
Lösung an seiner Stelle. Graue Platzhalterflächen gibt es nirgends.

Sechs Plätze sind vorbereitet und in `assets/img/foto/LIESMICH.txt` mit
Zuschnitt und Bildsprache beschrieben. Datei ablegen, Namen in
`src/daten.py` unter `FOTOS` eintragen, neu bauen – der Abschnitt erscheint
von selbst.

Was dort **nicht** hingehört: gekaufte Stockfotos mit Werbe-Pose, HDR,
knallblauer Himmel, Landschaft ohne Menschen. Der Golfpro steht im
Mittelpunkt, nicht der Ball.

---

## Drei Ebenen, die zusammengehören

| Ebene | Charakter |
|---|---|
| Marketingwebsite | ruhig, redaktionell, Softwaremarke |
| Produkt (CMS) | funktional, präzise, Werkzeug |
| Beispiel-Website | persönlich, wärmer, Golfschule |

Dass die Beispiel-Website anders aussieht, ist Absicht: Der Besucher soll
sehen, dass GolfProCMS nicht nur ein Backend ist, sondern einen eigenen
Auftritt ermöglicht. Deshalb hat sie den gelben Marker und die
Handschrift, die die Marketingseite bewusst nicht benutzt.

---

## Was hier nicht vorkommt

Keine Glow-Verläufe, keine Blur-Kugeln, keine Glaskarten, kein Neon, keine
violetten Verläufe, keine schwebenden 3D-Geräte, keine Sparkles, keine
Stock-Illustrationen, kein Countdown, keine erfundenen Nutzerzahlen, keine
ausgedachten Stimmen, kein „Revolution", kein „Gamechanger".

---

## Prüfung nach dem Umbau

* 23 Seiten × 6 Breiten (320–1920) ohne Überlauf
* 81 aufgelöste interne Ziele erreichbar
* 42 Interaktionsprüfungen (Menü, Demo, Tour, Filter, Lupe,
  Gerätewechsler, Formular, mobiles Menü)
* keine Konsolenfehler

Zwei Fehler sind dabei gefunden und behoben worden: Inline gesetzte Raster
ließen sich von der Media Query nicht überschreiben, sodass auf dem Telefon
zwei Spalten stehen blieben; und die typografische Liste entschärfte HTML
in der ersten Spalte, wodurch auf `/funktionen/` roher Quelltext sichtbar
wurde.
