# Art Direction

Warum die Website so aussieht, wie sie aussieht – und woran man merken
würde, dass jemand davon abgewichen ist.

---

## Die Marke kommt aus dem Produkt, nicht aus dieser Website

Farben, Schriften und Zeichen sind nicht hier entstanden. Sie stehen in
`lib/Marke.php` und `assets/css/app.css` des Produkts (Stand `b15aaa3`,
„Aus GolfPro CMS wird TeePilot") und sind von dort übernommen — Wert für
Wert, Pfad für Pfad. Wenn sich die Marke ändert, ändert sie sich dort, und
diese Website zieht nach. Nicht umgekehrt.

| | |
|---|---|
| **Pine** `#0b2b22` | Der Grund der Marke. Vorhang, dunkle Abschnitte, Fußzeile. |
| **Fairway** `#12513f` | Knöpfe, Links, aktive Zustände. |
| **Signal** `#c3e35c` | Akzent — **nur als Fläche auf Dunkel.** |
| **Olive** `#5f7320` | Der Akzent, wo er lesbar sein muss (4,9:1). |
| **Horizon** `#8fcbb4` | Die zweite Stimme auf Dunkel: Linien, Nummern, Unterzeilen. |
| **Chalk** `#f6f5f0` | Grundton der Seite. |
| **Anthracite** `#1c201d` | Fließtext. |

**Signal steht nie als Schrift auf Hell.** Dort liegt es bei 1,33:1 und
fällt durch jeden Test. Auf dieser Website kommt es genau dreimal vor: als
Linie unter dem letzten Satzteil einer Überschrift (eine Linie muss nicht
lesbar sein), und zweimal als Farbe des Bildzeichens — im Fuß und im
Vorhang, beide auf Pine, dort 10,5:1. Gemessen, nicht geschätzt.

**Das Zeichen** ist ein Punkt und eine Linie: der Ball auf dem Tee und die
Bahn, die er nimmt. Dieselbe Form liest sich auf einer Karte als Standort
mit geplanter Route. Es nimmt die Schriftfarbe an (`currentColor`), damit
dasselbe Zeichen hell auf Pine und dunkel auf Chalk stehen kann, ohne
zweimal im Dokument zu liegen. Die Maße der Wortmarke stehen im Handbuch
und deshalb auch hier: Abstand 0,3 × Zeichenhöhe, Schriftgrad 0,78 ×,
Gewicht 700, Laufweite −0,04 em.

Fürs Favicon steht das **TP-Monogramm**, nicht das Bildzeichen: Ein Favicon
wird 16 Pixel groß, und darunter zerfällt ein Punkt mit einer Linie zu zwei
Flecken.

**Schriften:** Schibsted Grotesk trägt die Seite, IBM Plex Mono alles, was
Zahl oder Randnotiz ist. Beide liegen auf diesem Server. Archivo und Caveat
sind weg — sie gehören zum Entwurf „Sonnenhang" der Website, die ein
Golfpro mit TeePilot baut. Das ist sein Auftritt, nicht unserer.

**Die Handschrift ist damit auch weg.** Wo vorher eine gespielte Handschrift
stand (`.hand`), steht jetzt eine Randnotiz in IBM Plex Mono (`.notiz`).
Eine Handschrift, die keine ist, gehört zu einer Golfschule — ein Werkzeug
schreibt nicht mit der Hand.

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

## Das Zeichen

Ein Fahnenstock, dessen Tuch ein Inhaltsblock mit zwei Textzeilen ist. Golf
und CMS in einem Zeichen, nicht eine Fahne neben einem Zahnrad.

Vier Entwürfe wurden gebaut und nebeneinander angesehen:

| | Idee | Ergebnis |
|---|---|---|
| A | Fahnenstock als Textcursor | Idee kam nicht an, las sich als gewöhnliches Fahnensymbol |
| B | Reine Wortmarke mit Punkt | Sauber, aber der Sandpunkt verschwand |
| C | Loch von oben, Fahne daneben | Klar lesbar, aber ein Standard-Golfsymbol |
| D | Monogramm im Kreis | Austauschbar, wie jede App |
| E | **Fahne als Textblock** | **gewählt** — trägt die Idee und liest auch bei 17px |
| F | Das „o" ist das Loch | Wirkte klein wie ein Fleck im Wort |
| G | Fahne im abgerundeten Quadrat | Genau das App-Icon-Muster, das vermieden werden soll |
| H | Kreis unter dem „o" | Nahezu unsichtbar |

**Kein abgerundetes Quadrat um das Zeichen.** Das ist die Form eines
App-Symbols, nicht die einer Marke.

**Wortmarke:** „GolfPro" trägt das Gewicht (600), „CMS" steht leichter
daneben (400, gedämpft). Der Betrieb ist die Hauptsache, die Software das
Werkzeug.

**Die Sandlinie** unter dem Stock ist der Boden. Sie ist die einzige Stelle,
an der die Akzentfarbe im Logo vorkommt.

Beim Überfahren neigt sich der Stock um vier Grad, wie im Wind. Das ist die
einzige Animation am Logo.

## Die Navigation ist eine Seite, keine Klappbox

Ein Klick auf einen Punkt im Kopf zieht einen **Vorhang** über das ganze
Fenster: tiefes Grün, darauf das Verzeichnis des Bereichs, groß gesetzt und
durchnummeriert. Eine Inhaltsseite, keine Oberfläche.

Davor standen drei Fassungen, und alle drei sind an derselben Stelle
gescheitert. Erst die ganze Aufnahme in einem 400 Pixel breiten Rahmen: 1440
auf 400, also 28 Prozent, ein graues Raster. Dann ein Ausschnitt daraus in
Originalgröße: lesbar, aber ein Rechteck aus einem fremden Bildschirm, das im
Klappmenü aus dem Zusammenhang fiel. Dann der Grundriss des Programms, alle
22 Bereiche als Wortfeld: ehrlich, aber eine zweite Liste neben der ersten.

Dreimal wurde die Nutzlast getauscht, dreimal blieb der Kasten. **Der Kasten
war das Problem.** Eine weiße Klappbox mit zwei Textspalten und etwas rechts
daneben ist die Form, die jede Software-Seite hat – die Füllung ändert daran
nichts.

**Die Form**

* **Vollbild.** Tiefes Grün (`--gruen-tief`) über alles. Es ist die einzige
  Stelle der Website, an der die Marke die ganze Fläche nimmt.
* **Das Verzeichnis** ist das ganze Gestaltungsmittel: Nummer in Salbei,
  Name in `clamp(26px, 3.5vw, 50px)`, Satz rechtsbündig an derselben
  Haarlinie, dazwischen eine Linie in 15 Prozent Papierweiß.
* **Die Sätze stehen rechtsbündig.** Linksbündig standen sie frei im Raum
  und lasen sich als zweite Liste; `max-content` kann sie nicht
  untereinander bringen, weil jede Zeile ein eigenes Raster ist. Bündig ist
  es eine Inhaltsseite.
* **Kein Bild, kein Kasten, keine Fläche.** Auch kein riesiges Wort im
  Hintergrund – das war eine Fassung lang drin und kollidierte mit dem Satz
  darunter. Dekoration ist genau das, was hier dreimal durchgefallen ist.
* **Der Inhalt beginnt in derselben Spalte wie das Logo.** Die Breite ist
  `--breite-weit` minus zweimal `--rand-seite`, nicht ein eigener Wert.

**Das Verhalten**

* **Hover öffnet – aber erst nach 170 ms.** Ohne diese Absichtsfrist zieht
  jede Maus, die im Vorbeifahren die Leiste streift, eine ganze Seite auf.
  170 ms sind lang genug, dass ein Durchfahren nichts auslöst, und kurz
  genug, dass es nicht träge wirkt. Auf Geräten ohne feinen Zeiger
  (`hover: hover and pointer: fine`) gilt nur der Klick.
* **Steht der Vorhang, wird ohne Frist gewechselt.** Zwischen zwei
  Bereichen hinge die Frist sonst spürbar nach.
* **Ein Klick in den ersten 400 ms nach dem Hover-Öffnen schließt nicht.**
  Er gilt dem, was man gerade erst gesehen hat, nicht dem Zumachen. Danach
  schließt derselbe Knopf wie erwartet.
* **Zumachen ist leicht:** Escape, derselbe Knopf, oder ein Klick
  irgendwohin, wo kein Ziel ist. Bei einem Vorhang, der von selbst aufgeht,
  muss das so sein.
* **Und er geht von selbst zu, wenn man ihn verlässt.** Weil er das ganze
  Fenster füllt, feuert `mouseleave` nie – es gibt kein Außen. Stattdessen
  ein Feld: die Kopfzeile über die ganze Breite, darunter der Inhalt mit
  56 px Luft. Wer da herausfährt – weit nach rechts, weit nach links, unter
  einen kurzen Abschnitt – meint den Vorhang nicht mehr.
* **Zwei Dinge halten das ruhig.** Das Feld ist großzügiger als der Inhalt,
  und das Zugehen wartet 340 ms ab: Wer über den Rand wischt und
  zurückkommt, löst nichts aus. Gemessen: achtmal über die Grenze und
  zurück, je 110 ms – kein einziges Zugehen.
* **An jeder Kante bleibt ein Streifen von mindestens 48 px**, der immer
  schließt. Aus der bloßen Zugabe wären bei 1440 px acht Pixel geworden –
  dahin trifft niemand absichtlich. Die Klammer greift nie in den Text:
  geprüft bei 1024, 1440 und 1920 px. Auf breiten Schirmen sind es 208 px
  je Seite.
* Das Feld wird bei jedem Öffnen und jedem Wechsel neu gemessen. Ein kurzer
  Abschnitt wie „Über uns" bekommt dadurch von selbst ein Schließfeld
  unter sich, ein langer wie „Produkt" nicht.
* **Beim Überfahren tritt eine Zeile vor, weil die anderen zurücktreten** –
  von Papierweiß auf 42 Prozent. Kein Kasten, kein Versatz, nur Helligkeit.
* **Der Aufbau** läuft als Animation, nicht als Übergang: Der Vorhang fällt
  über `clip-path` in 520 ms, darunter ziehen sich die Haarlinien von links
  (ab 90 ms), die Zeilen schweben ein (ab 150 ms), die Nummern kommen
  zuletzt (ab 300 ms) – je 55 ms versetzt. Animationen deshalb, weil sie
  neu anlaufen, sobald ein Element frisch dargestellt wird: Beim Wechsel
  des Abschnitts baut sich das Verzeichnis dadurch wieder auf. Ein Übergang
  täte das nicht, weil der versteckte Zustand nie gerendert wurde.
* **Der Kopf wechselt die Farbe nicht mit dem Vorhang, sondern wenn der
  Vorhang ihn erreicht hat** (150 ms beim Aufziehen, 430 ms beim Zumachen).
  Sofort gewechselt stand helle Schrift einen Moment auf hellem Grund.
  Aus demselben Grund macht die Deckkraft des Vorhangs die Arbeit nicht,
  sondern springt erst, wenn der Zuschnitt fertig ist – eine überlagerte
  Blende ließ ihn durchsichtig werden, während er noch da war.
* Unter `prefers-reduced-motion` steht er einfach da.
* **Der Kopf bleibt darüber stehen und wird hell.** Das Zeichen nimmt
  `currentColor`, die Zeilen im Fahnentuch eine Variable – so färbt der
  Vorhang dasselbe Logo um, statt ein zweites mitzubringen.
* **Wo der Kopf endet, wird gemessen, nicht geraten.** Ob das
  Ankündigungsband noch steht, hängt am Scrollstand; auf dem Telefon lag
  die erste Zeile sonst im Logo. JavaScript setzt `--kopf-unten` beim
  Öffnen.
* Escape schließt, ein Klick neben das Verzeichnis schließt, derselbe
  Knopf noch einmal schließt. Der Fokus geht danach dorthin zurück, wo er
  herkam, und wird solange zwischen Kopf und Vorhang gehalten.

**Ein Bauteil für beide Größen.** Auf großen Schirmen zeigt der Vorhang den
Abschnitt, den der Kopf anwählt; auf kleinen alle untereinander, mit
Abschnittsnamen und den beiden Knöpfen am Fuß. Vorher waren das zwei
Bauteile – Mega-Menü und Vollbildmenü – mit zwei Fehlerquellen. Das erzeugte
HTML ist dadurch von 864 auf 561 KB gefallen.

Er liegt bewusst **neben** dem Kopf im Dokument, nicht darin: Der Kopf trägt
ein `backdrop-filter`, und das macht ihn zum Bezugsrahmen für
`position: fixed`. Innerhalb wäre der Vorhang auf Kopfhöhe eingesperrt
gewesen.

## Keine Etiketten über Überschriften

Das kleine gesperrte Versal-Schildchen mit Strich davor —
`—— GOLFPROS · WEBSITE · CMS` — ist das deutlichste Erkennungsmerkmal
automatisch zusammengesetzter Seiten. Es stand 84 Mal auf dieser Website.

Die meisten sagten nichts: „Mehr davon", „Die Bereiche", „Im Alltag",
„Fragen". Eine Überschrift, die ein Schild darüber braucht, um verstanden
zu werden, ist noch nicht fertig.

**Regel:** Abschnitte beginnen mit ihrer Überschrift. Wo Orientierung
wirklich fehlt, steht sie im Vorspann als ganzer Satz, nicht als Etikett.

Geblieben sind neun Stellen, die Information tragen:

* der Schrittzähler der Produkt-Tour (`Schritt 03 · Buchungen`) — man muss
  wissen, wo man steht
* die vier Fälle unter Vorteile (`Der erste Fall`, `Der zweite`, …) — als
  gesprochene Zeile, nicht als Nummernplakette

Auch diese neun stehen in normaler Schreibung, ohne Strich und ohne
Sperrung. Ein Etikett, das aussieht wie ein Etikett, ist ein Etikett; eine
kleine Zeile Text ist eine kleine Zeile Text.

Dasselbe gilt für Nummernplaketten an Ablaufschritten. Vier Schritte
untereinander, durch Haarlinien getrennt, liest ohnehin jeder von oben nach
unten. `01 02 03 04` sagt nur, dass hier jemand gezählt hat. Die großen
Umrissziffern der fünf Kapitel bleiben — die sind ein bewusstes
redaktionelles Mittel, kein Aufzählungszeichen.

Bildunterschriften folgen dem Muster `01 Dashboard` plus Satz, in normaler
Schreibung. In Versalien mit weiter Sperrung sah dieselbe Zeile aus wie ein
Schnittstellen-Etikett.

## Was gezählt wurde

Beim Umbau nachgemessen, nicht geschätzt:

| | vorher | nachher |
|---|---:|---:|
| Karten site-weit | 192 | 0 |
| Icon-Kreise | 61 | 0 |
| zentrierte Blöcke | 33 | 13 |
| Etiketten über Überschriften | 84 | 9 |
| Nummernplaketten an Schritten | 18 | 0 |
| nummerierte Kapitel | 0 | 5 |
| typografische Listen | 0 | 24 |

Karten sind nicht verboten – aber jede einzelne muss sich rechtfertigen.
Auf dieser Website hat es keine geschafft.

---

## Farbe

Der Großteil der Fläche ist Chalk. Fairway ist Marken- und Akzentfarbe,
nicht Grundton. Die Werte kommen aus dem Produkt — siehe ganz oben.

| | | Verwendung |
|---|---|---|
| `--papier` | `#f6f5f0` | Chalk, Grundfläche, rund zwei Drittel der Seite |
| `--papier-2` | `#f0efe9` | abgesetzte Bänder |
| `--gruen` | `#12513f` | Fairway: Knöpfe, Marke, Links |
| `--gruen-tief` | `#0b2b22` | Pine: Vorhang, dunkle Abschnitte, Fußzeile |
| `--salbei` | `#8fcbb4` | Horizon: Linien und Nummern auf Dunkel |
| `--signal` | `#c3e35c` | Linie unter der Überschrift, Zeichen auf Pine |
| `--akzent` | `#5f7320` | Olive: der Akzent, wo er lesbar sein muss |
| `--sand` | `#e4dac4` | der ruhige warme Ton, sehr sparsam |
| `--tinte` | `#1c201d` | Anthracite, Text |

**Kein gelber Textmarker.** Das Produkt benutzt ihn auf den Websites, die
ein Golfpro damit baut; hier wäre er die lauteste Stelle. Stattdessen liegt
eine Linie unter dem hervorgehobenen Wort — in Signal, weil eine Linie
nicht lesbar sein muss. Sand war dafür zu blass, seit er aus der Marke
kommt (`#e4dac4` statt `#c8b795`).

---

## Typografie

Schibsted Grotesk, dieselbe Datei wie im Produkt. IBM Plex Mono für
Randnotizen und alles, was Zahl ist.

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
sehen, dass TeePilot nicht nur ein Backend ist, sondern einen eigenen
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
  Gerätewechsler, Formular, Vorhang auf dem Telefon)
* keine Konsolenfehler

Zwei Fehler sind dabei gefunden und behoben worden: Inline gesetzte Raster
ließen sich von der Media Query nicht überschreiben, sodass auf dem Telefon
zwei Spalten stehen blieben; und die typografische Liste entschärfte HTML
in der ersten Spalte, wodurch auf `/funktionen/` roher Quelltext sichtbar
wurde.
