# Produktanalyse TeePilot

Grundlage der Marketingwebsite. Erhoben am 21.09.2026 aus dem Repository
`christophschnurrenberger-sketch/CMS-Golfpros`, ergänzt um eine lokale
Installation mit dem Demo-Bestand, den `install.php` auf Wunsch anlegt.

**Regel für die gesamte Website:** Was hier nicht als *vorhanden* steht, wird
dort nicht als Produktfunktion behauptet.

---

## 1. Was das Produkt ist

Eine PHP-Anwendung für Golfbetriebe. Kein SaaS, keine gehostete Plattform:
Der Pro lädt die Dateien auf seinen Webspace, ruft `install.php` auf und hat
danach eine eigene Installation mit eigener Datenbank.

| | |
|---|---|
| Sprache | PHP 8.1+, keine externen Abhängigkeiten (kein Composer, kein Node) |
| Datenbank | SQLite (eine Datei) **oder** MySQL – Auswahl beim Installieren |
| Struktur | 46 Klassen in `lib/`, 54 Seiten in `app/`, Autoloader ohne Composer |
| Mandanten | Ja – `lib/Tenant.php` setzt `workspace_id` selbst in jede Bedingung |
| Rollen | 4: Inhaber, Head Pro, Trainer, Assistenz (`lib/Auth.php`) |
| Einrichtung | Geführt in 9 Schritten, endet mit veröffentlichter Website |
| Schriften | Archivo + Caveat lokal in `assets/fonts/`, kein Google-Aufruf |
| Statistik | Cookiefrei, IP wird nicht gespeichert (`lib/Analytics.php`) |

---

## 2. Feature-Matrix

Quelle: `lib/Module.php` (Modulverzeichnis), `lib/Schema.php` (68 Tabellen),
`app/` (Seiten). „Kern“ = immer sichtbar, nicht abschaltbar.

| Bereich | Vorhanden | Teilweise | Nicht vorhanden | Kern | Ab Stufe | Beleg |
|---|:--:|:--:|:--:|:--:|---|---|
| Dashboard | X | | | X | Starter | `app/index.php` |
| Kunden | X | | | X | Starter | `app/kunden.php`, `app/kunde.php`, `lib/Customers.php` |
| Leads | X | | | | Pro | `app/leads.php`, `lib/Leads.php` |
| Kalender | X | | | X | Starter | `app/kalender.php` |
| Buchungen | X | | | X | Starter | `app/buchungen.php`, `app/verfuegbarkeit.php`, `buchen.php` |
| Pakete | X | | | | Starter | `app/pakete.php` (Unterpunkt von Buchungen) |
| Training | X | | | | Pro | `app/training.php`, `app/trainingsplan.php`, `app/uebungen.php` |
| Videoanalyse | X | | | | Business | `app/videoanalyse.php`, `assets/js/video.js` |
| Kurse | X | | | | Pro | `app/kurse.php`, `lib/Courses.php` |
| Produkte | X | | | | Pro | `app/produkte.php`, `lib/Commerce.php` |
| Zahlungen | X | | | | Pro | `lib/Stripe.php`, `webhook.php`, `kaufen.php` |
| Rechnungen | X | | | | Pro | `app/rechnungen.php`, `lib/Invoices.php`, `lib/PDF.php` |
| Website | X | | | X | Starter | `app/website.php`, `app/seite.php`, `lib/Bloecke.php`, `lib/Renderer.php` |
| Inhalte / Blog | X | | | | Starter | `app/inhalte.php`, `app/beitrag.php`, `app/medien.php` |
| Events | X | | | | Pro | `app/events.php`, `lib/Events.php` |
| Reisen | X | | | | Pro | `app/reisen.php`, `reise.php`, `lib/Trips.php` |
| Marketing | X | | | | Pro | `app/marketing.php`, `app/kampagne.php` |
| Newsletter | X | | | | Pro | `app/newsletter.php`, `api.php`, `abmelden-newsletter.php` |
| Automationen | X | | | | Business | `app/automationen.php`, `lib/Automations.php` |
| Community | X | | | | Business | `app/community.php`, `lib/Gamification.php` |
| Auswertung | X | | | | Business | `app/auswertung.php`, `lib/Analytics.php` |
| KI-Assistent | X | | | | Business | `app/ki.php`, `lib/KI.php` |
| Einstellungen | X | | | X | Starter | `app/einstellungen.php`, `app/team.php`, `app/tarif.php` |
| Kundenportal | X | | | | – | `portal/`, `lib/Kundenlogin.php` |

### Nur unter Bedingungen vorhanden

| Thema | Stand | Folge für die Website |
|---|---|---|
| Stripe-Zahlungen | Vorhanden, braucht aber Schlüssel des Betreibers | „Mit Stripe-Konto möglich; ohne Stripe wird auf Rechnung verkauft.“ |
| KI-Funktionen | Vorhanden, ohne API-Schlüssel regelbasierter Generator | So auch formuliert, nie als „KI inklusive“ |
| SMS / WhatsApp | Konfiguration vorgesehen, standardmäßig leer | Nur „Erinnerungen per E-Mail“ behaupten |
| Cronjob | Optional, sonst Wartung beim Dashboard-Aufruf | Als Option erwähnt, nicht als Voraussetzung |

### Nicht vorhanden – darf nirgends behauptet werden

* **Keine Abrechnung für TeePilot selbst.** Die vier Stufen in
  `Module::plaene()` steuern den Funktionsumfang *innerhalb* des CMS. Es gibt
  keinen Bezahlvorgang, kein Abo-Management, keine Kündigungsstrecke.
  → Die Preisseite zeigt deshalb Stufen ohne Kaufknopf und sagt das auch.
* **Kein Import aus anderen Systemen** (WordPress, Wix, Jimdo o. ä.).
  → In der FAQ ausdrücklich verneint.
* **Keine mobile App.** Die Oberfläche ist responsiv, mehr nicht.
* **Keine belegten Nutzerzahlen, keine Referenzen, keine Testimonials.**
  → Nirgends behauptet; die Komponenten dafür sind vorbereitet, aber leer.

---

## 3. Belegte Zahlen

Nachgezählt in einer lokalen Installation (SQLite, Demo-Workspace):

| Zahl | Wert | Herkunft |
|---|---|---|
| Module | 22 (6 Kern) | `lib/Module.php` |
| Bausteintypen im Baukasten | 27 | `lib/Bloecke.php` |
| Datenbanktabellen | 68 | `lib/Schema.php` |
| Einrichtungsschritte | 9 | `app/onboarding.php` |
| Rollen | 4 | `lib/Auth.php` |
| Demo: Kunden | 40 | `SELECT COUNT(*) FROM customers` |
| Demo: Termine | 1152 | `SELECT COUNT(*) FROM bookings` |
| Demo: Rechnungen | 73 | `SELECT COUNT(*) FROM invoices` |

Die vier Stufen mit Preisen (29 / 59 / 99 / 199 € pro Monat) stehen wörtlich
in `Module::plaene()`. Sie sind damit **im Produkt hinterlegt**, aber nicht
als Verkaufspreis belegt – siehe oben.

---

## 4. Herkunft der Screenshots

Alle 68 Aufnahmen unter `assets/img/shots/` stammen aus einer laufenden
Installation:

1. Repository lokal ausgecheckt, `data/` und `uploads/` angelegt.
2. Kopfloser Installer (entspricht `install.php`): SQLite, eigener Workspace,
   danach `Demo::anlegen()`.
3. `php -S 127.0.0.1:8088`, Anmeldung über `demo.php`.
4. Playwright, 1440×900 bei doppelter Pixeldichte; Tablet 834×1112,
   Telefon 390×844.
5. Umgewandelt nach WebP (Qualität 82) in zwei Breiten: 1600 px und 800 px.

Nichts ist nachgebaut, nachgezeichnet oder retuschiert. Die Bildplatzhalter
auf der Beispiel-Website („Aufmacher: Range im Abendlicht“) sind das
tatsächliche Verhalten des Produkts, solange kein Bild hochgeladen wurde.

---

## 5. Offene Punkte

* **Fotografie fehlt.** Die Website kommt ohne Fotos aus und setzt auf
  Produktaufnahmen und Typografie. Wer Fotos ergänzen will (Pro beim
  Training, Range, Putting-Unterricht), legt sie unter `assets/img/` ab –
  bitte nur mit geklärten Rechten.
* **Platzhalter vor dem Livegang ersetzen:** `KONTAKT_MAIL`, `BASIS_URL`,
  sowie Impressum und Datenschutzerklärung (`src/seiten/rest.py`).
* **Kontaktformular hat kein Backend.** Es sagt das ehrlich und verweist auf
  die E-Mail-Adresse. Sobald ein Endpunkt existiert, genügt
  `FORMULAR_ENDPUNKT` in `src/daten.py`.
* **Kein Link in die laufende App**, solange `APP_BASIS` leer ist. Dann
  führen alle „Öffnen“-Knöpfe in die Demo dieser Website statt auf einen
  Login, den es nicht gibt.
