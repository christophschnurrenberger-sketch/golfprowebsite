# GolfProCMS – Marketingwebsite

Die Verkaufs- und Marketingwebsite für [GolfProCMS](https://github.com/christophschnurrenberger-sketch/CMS-Golfpros).
23 Seiten, statisches HTML, keine Laufzeitabhängigkeit.

Sie erklärt und verkauft das Produkt. Sie ist **nicht** das Produkt – das
liegt im Repository `CMS-Golfpros` und bleibt davon unberührt.

---

## Was daran besonders ist

**Alle Screenshots sind echt.** Für diese Website wurde GolfProCMS lokal
installiert, der Demo-Bestand angelegt und mit einem Browser fotografiert:
68 Aufnahmen aus dem laufenden System, in drei Bildschirmbreiten. Kein
nachgebautes Dashboard, keine gezeichnete Oberfläche.

**Jede Aussage ist belegt.** Was GolfProCMS kann, steht in
[`src/daten.py`](src/daten.py) – zu jedem Bereich die Datei im Produkt, aus
der er stammt. Die Funktionsseite zeigt diese Spalte offen. Was das Produkt
nicht kann, steht in [`PRODUKT-ANALYSE.md`](PRODUKT-ANALYSE.md) und wird
nirgends behauptet: keine erfundenen Nutzerzahlen, keine Testimonials, keine
Logos, keine Zertifikate.

**Dieselbe Handschrift wie das Produkt.** Die Schriften Archivo und Caveat
sind dieselben Dateien wie im CMS. Farben, Radien und Rhythmus folgen einer
eigenen Art Direction, die in [`DESIGN.md`](DESIGN.md) steht: warmes
Off-White als Grundfläche, tiefes Golfgrün als Akzent, Linien statt
Schatten – und keine zwei Abschnitte hintereinander, die gleich aussehen.
Karten, Icon-Kreise und zentrierte Blöcke wurden bewusst abgebaut
(192 Karten → 0).

**Ohne Fotos fertig, mit Fotos besser.** Die Website enthält keine
Fotografie. Wo ein Foto hingehört, entfällt der Abschnitt oder es steht
eine typografische Lösung an seiner Stelle – graue Platzhalter gibt es
nirgends. Sechs Plätze sind vorbereitet, siehe
[`assets/img/foto/LIESMICH.txt`](assets/img/foto/LIESMICH.txt).

---

## Aufbau

```
build.py          Der Erzeuger – Python 3, nur Standardbibliothek
src/
  daten.py        Produktwahrheit: Module, Belege, Navigation, Tarife
  layout.py       Kopf, Navigation, Fuß, Dokumentkopf
  bausteine.py    Wiederverwendbare Abschnitte
  icons.py        Strichsymbole als Inline-SVG
  seiten/         Je Themenbereich eine Datei
  og-vorlage.html Vorlage für die Social-Media-Karte
assets/
  css/site.css    Das Design-System
  css/schriften.css
  js/site.js      Verhalten – ein Skript, keine Abhängigkeit
  fonts/          Archivo + Caveat (aus dem Produkt übernommen)
  img/shots/      68 Aufnahmen × 2 Breiten als WebP
  img/og.png      Social-Media-Karte
```

Das erzeugte HTML liegt im Projektordner (`index.html`, `produkt/index.html`,
…) und ist unverändert hochladbar.

## Ansehen – ohne irgendetwas zu installieren

**Das HTML ist fertig und liegt im Repository.** `build.py` brauchst du nur,
wenn du Texte änderst. Zum Ansehen genügt:

> Repository herunterladen (grüner Knopf **Code → Download ZIP**), entpacken,
> **Doppelklick auf `index.html`**.

Der Browser öffnet die Startseite, die Navigation funktioniert, alle Bilder
sind da. Es läuft kein Server, es wird nichts installiert.

Wer lieber einen lokalen Server möchte (nötig ist er nicht):

```sh
python3 -m http.server 8090
# dann http://localhost:8090 öffnen
```

## Veröffentlichen

Alles außer `src/`, `build.py` und den beiden `.md`-Dateien ist die Website.

* **Eigener Webspace (FTP):** Ordnerinhalt hochladen, fertig. `.htaccess`
  liegt bei und regelt 404, Komprimierung und Cache.
* **GitHub Pages:** im Repository unter *Settings → Pages* als Quelle
  *Deploy from a branch* wählen, den Branch dieses Codes und den Ordner
  `/ (root)`. `.nojekyll` liegt bei.
* **Netlify / Cloudflare Pages:** Publish directory `/`, **kein**
  Build-Befehl. `_headers` liegt bei.

### Warum das überall funktioniert

Alle Verweise im HTML sind **relativ** zur jeweiligen Seite
(`../assets/css/site.css` statt `/assets/css/site.css`) und Seitenverweise
enden auf `index.html`. Das ist der Unterschied zwischen „läuft nur an einer
Domain-Wurzel" und „läuft überall":

| Ort | absolute Pfade | relative Pfade |
|---|---|---|
| Doppelklick auf `index.html` | kaputt | läuft |
| GitHub Pages unter `/reponame/` | kaputt | läuft |
| Unterordner auf dem Webspace | kaputt | läuft |
| Domain-Wurzel | läuft | läuft |

Gesteuert wird das über `PFADE` in [`src/daten.py`](src/daten.py). Der
Standard ist `"relativ"`. Wenn die Website später direkt an einer
Domain-Wurzel liegt und du saubere Adressen ohne `index.html` willst, setze
`PFADE = "absolut"` und baue neu – dann gilt allerdings wieder die erste
Spalte der Tabelle.

## Ändern und neu bauen

Nur nötig, wenn du Texte, Farben oder Seiten änderst.

```sh
python3 build.py
```

Kein Node, keine `node_modules`, kein Build-Werkzeug – nur Python 3, das auf
macOS und Linux schon da ist. Der Aufruf löscht die erzeugten Ordner und
schreibt sie neu. Danach die geänderten Dateien committen.

Wo was steht:

| Du willst ändern | Datei |
|---|---|
| Texte einer Seite | `src/seiten/…` |
| Was das Produkt kann, Navigation, Tarife | `src/daten.py` |
| Farben, Schriften, Abstände | `assets/css/site.css` |
| Fotos ergänzen | `assets/img/foto/` + `FOTOS` in `src/daten.py` |
| Impressum, Datenschutz | `src/seiten/rest.py` |

---

## Vor dem Livegang ausfüllen

Alles an einer Stelle: [`src/daten.py`](src/daten.py).

| Eintrag | Bedeutung |
|---|---|
| `BASIS_URL` | Die echte Domain – geht in Canonical, Sitemap und Open Graph |
| `KONTAKT_MAIL` | Ersetzt den Platzhalter auf Kontaktseite und Formular |
| `FORMULAR_ENDPUNKT` | Leer = das Formular sagt ehrlich, dass es nichts sendet, und nennt die E-Mail-Adresse. Sobald hier ein Endpunkt steht, wird wirklich gesendet |
| `APP_BASIS` | Adresse der laufenden CMS-Installation. Leer = alle „Öffnen“-Knöpfe führen in die Demo dieser Website statt auf einen Login, den es nicht gibt |
| `DEMO_ZUGANG` | Direktlink auf `demo.php?k=…`, falls ein öffentlicher Demo-Zugang eingerichtet ist |

Dazu: **Impressum und Datenschutzerklärung** in
[`src/seiten/rest.py`](src/seiten/rest.py). Beide sind Vorlagen mit
Platzhaltern in eckigen Klammern und auf `noindex` gesetzt. Solange die
Platzhalter darin stehen, sind sie nicht rechtsgültig; die Vorlagen ersetzen
keine Rechtsberatung.

---

## Seiten

| Adresse | Inhalt |
|---|---|
| `/` | Startseite: Problem, Lösung, Module, Demo, Beispiel-Website, Stufen, FAQ |
| `/produkt/` | Produktübersicht, Bereich für Bereich |
| `/funktionen/` | Alle 22 Bereiche, mit Belegtabelle |
| `/funktionen/dashboard/` | Dashboard im Detail |
| `/funktionen/website/` | Website-Baukasten |
| `/funktionen/kurse/` | Kurse und Training |
| `/funktionen/buchungen/` | Buchungen und Online-Buchung |
| `/demo/` | Interaktive Produktdemo, 10 Bereiche |
| `/demo/produkt-tour/` | Geführter Rundgang in 5 Schritten |
| `/demo/beispiel-website/` | Die erzeugte Golfpro-Website auf 3 Geräten |
| `/demo/screenshots/` | Galerie aller Aufnahmen mit Filter und Lupe |
| `/demo/golfpro/` | Reduzierte Landingpage für Links aus LinkedIn (`noindex`) |
| `/fuer-golfpros/` `/fuer-golflehrer/` `/fuer-golfakademien/` | Zielgruppen |
| `/vorteile/` | Vier Situationen aus dem Alltag, mit Ablauf |
| `/preise/` | Die vier Stufen und die technischen Voraussetzungen |
| `/faq/` | 16 Fragen, mit FAQ-Auszeichnung für Suchmaschinen |
| `/ueber-uns/` | Warum es das Produkt gibt |
| `/kontakt/` | Kurzes Formular mit Prüfung im Browser |
| `/impressum/` `/datenschutz/` | Vorlagen (`noindex`) |
| `/404.html` | Fehlerseite |

---

## Messung vorbereitet, aber nichts gemessen

Es ist **kein** Tracker eingebunden und **kein** Cookie gesetzt. Das Skript
sammelt Ereignisse nur in einer Warteschlange:

```js
window.gpAnalytics.queue        // [{event, daten, t}, …]
window.gpAnalytics.sink = fn    // Übergabe an ein Werkzeug nach Einwilligung
window.gpMelden('name', {...})  // von Hand melden
```

Vorbereitete Ereignisse: `hero_demo_click`, `trial_click`,
`product_demo_start`, `product_tour_start`, `product_tour_step`,
`product_tour_complete`, `screenshot_open`, `screenshot_filter`,
`demo_website_open`, `demo_geraet_wechsel`, `pricing_cta_click`,
`contact_form_start`, `contact_form_submit`, `linkedin_demo_click`,
`sticky_cta_click`.

Wird später ein Werkzeug angebunden, gehört davor ein Consent-Banner – und
die Datenschutzerklärung muss es beschreiben.

---

## Barrierefreiheit und Technik

* Semantisches HTML, eine `h1` je Seite, Sprungmarke zum Inhalt
* Tastaturbedienung für Mega-Menü, Demo-Reiter (Pfeiltasten), Tour, Lupe
* `aria-expanded`, `aria-selected`, `aria-current`, Beschriftungen an allen Knöpfen
* Sichtbarer Fokus überall, `prefers-reduced-motion` wird beachtet
* Alle Screenshots mit beschreibendem Alternativtext
* Kein horizontaler Scroll von 320 px bis Breitbild
* Schriften lokal – kein Aufruf zu Google, siehe LG München I, 20.01.2022,
  Az. 3 O 17493/20
* Bilder als WebP in zwei Breiten, `loading="lazy"` außer im ersten Bild

## Geprüft

Mit Playwright über alle 23 Seiten: HTTP-Status, interne Links (56),
Konsolenfehler, fehlende Dateien, horizontaler Scroll, Alternativtexte,
Titel- und Beschreibungslängen, `h1`-Anzahl. Dazu Interaktionstests für
Mega-Menü (Hover, Klick, Tastatur, Escape), mobile Navigation, Demo-Reiter,
Produkt-Tour, Galerie-Filter, Lupe, Gerätewechsler, Formularprüfung und den
klebenden CTA – auf Desktop und mit 390 × 844.

## Lizenz

Noch nicht festgelegt – wie beim Produkt.
