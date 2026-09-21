# -*- coding: utf-8 -*-
"""
Produktwahrheit und Seitenregister.

Diese Datei ist die einzige Stelle, an der steht, was GolfProCMS kann. Jede
Aussage hier ist im Repository CMS-Golfpros belegt; der Beleg steht als
Dateiname daneben. Wer eine Behauptung auf der Website findet, die hier nicht
vorkommt, hat einen Fehler gefunden.

Grundregel: Was nicht belegt ist, steht nicht auf der Website.
"""

# --------------------------------------------------------------- Eckdaten --

MARKE = "GolfProCMS"
TAGLINE = "Das CMS für Golfpros."

# Die laufende Installation. Solange hier None steht, zeigen alle
# „Öffnen“-Knöpfe auf die Demo dieser Website statt auf einen erfundenen
# Login. Sobald das CMS unter einer Adresse läuft, hier eintragen –
# dann schalten Header, Preise und CTA automatisch um.
APP_BASIS = None          # z. B. "https://app.golfprocms.de"
DEMO_ZUGANG = None        # z. B. "https://app.golfprocms.de/demo.php?k=schluessel"

# Kontakt. Platzhalter in eckigen Klammern werden vor dem Livegang ersetzt.
KONTAKT_MAIL = "[E-Mail-Adresse eintragen]"
FORMULAR_ENDPUNKT = ""    # leer = kein Backend, das Formular sagt das ehrlich

BASIS_URL = "https://example.com"   # für Sitemap und Open Graph

# ------------------------------------------------------------- Kennzahlen --
#
# Belegt durch den Demo-Workspace, den install.php auf Wunsch anlegt
# (lib/Demo.php). Die Zahlen sind mit einer lokalen Installation nachgezählt.

DEMO_ZAHLEN = {
    "kunden": 40,
    "termine": 1152,
    "rechnungen": 73,
    "leistungen": 8,
    "seiten": 7,
    "beitraege": 6,
}

# Belegt: lib/Module.php (21 Module + 1 Unterpunkt), app/ (54 Seiten),
# lib/ (46 Klassen je eine Datei, laut README.md).
SYSTEMZAHLEN = {
    "module": 22,
    "kernmodule": 6,
    "bausteine": 25,     # lib/Bloecke.php
    "onboarding": 9,     # app/onboarding.php SCHRITTE
    "rollen": 4,         # lib/Auth.php ROLLEN
}


# ----------------------------------------------------------------- Module --
#
# Reihenfolge und Beschreibung stammen aus lib/Module.php. „kern“ markiert
# die sechs Bereiche, die immer sichtbar sind; „plan“ ist die Stufe, ab der
# ein Modul einschaltbar ist.

def M(key, name, gruppe, plan, icon, kurz, kern=False, beleg="", bild=None,
      sehen=None, tun=None, nutzen="", seite=None):
    return dict(key=key, name=name, gruppe=gruppe, plan=plan, icon=icon,
                kurz=kurz, kern=kern, beleg=beleg, bild=bild,
                sehen=sehen or [], tun=tun or [], nutzen=nutzen, seite=seite)


MODULE = [
    M("dashboard", "Dashboard", "", "starter", "dashboard",
      "Zahlen, Termine und Empfehlungen des Tages auf einen Blick.",
      kern=True, beleg="app/index.php", bild="app-dashboard",
      seite="/funktionen/dashboard/",
      sehen=[
          "Umsatz heute, diesen Monat und dieses Jahr – jeweils mit Vergleich zum "
          "gleich langen Vorzeitraum.",
          "Auslastung der laufenden Woche und die Zahl der Termine dahinter.",
          "Die nächsten Termine mit Uhrzeit, Leistung und Name.",
          "Empfohlene Aktionen, aus den eigenen Daten berechnet – offene Anfragen, "
          "überfällige Rechnungen, auslaufende Pakete, Kunden ohne Termin.",
      ],
      tun=["Termin anlegen", "Kalender öffnen", "Aus jeder Empfehlung direkt in den "
           "passenden Bereich springen"],
      nutzen="Der Tag beginnt mit dem, was ansteht – nicht mit der Suche danach."),

    M("customers", "Kunden", "kunden", "starter", "customers",
      "Kundenakte mit HCP, Historie, Paketen und Kommunikation.",
      kern=True, beleg="app/kunden.php, app/kunde.php, lib/Customers.php",
      bild="app-kundenakte",
      sehen=["Stammdaten, Handicap und Status", "Alle bisherigen Termine",
             "Gekaufte Pakete mit verbrauchten und offenen Einheiten",
             "Rechnungen, Notizen und die Kommunikationshistorie"],
      tun=["Notiz festhalten", "Termin aus der Akte heraus anlegen",
           "Etiketten vergeben", "Eigene Felder ergänzen"],
      nutzen="Vor der Stunde ein Blick in die Akte – und du weißt wieder, woran ihr arbeitet."),

    M("leads", "Leads", "kunden", "pro", "leads",
      "Anfragen von der Website bis zum Kunden begleiten.",
      beleg="app/leads.php, app/lead.php, lib/Leads.php", bild="app-leads",
      sehen=["Alle Anfragen mit Quelle, Wert und Stufe",
             "Wie lange eine Anfrage schon liegt"],
      tun=["Stufe ändern", "Anfrage in einen Kunden überführen", "Nachfassen vermerken"],
      nutzen="Keine Anfrage bleibt im Postfach liegen, weil niemand mehr weiß, dass sie da war."),

    M("calendar", "Kalender", "kunden", "starter", "calendar",
      "Wochen- und Tagesansicht über alle Trainer und Standorte.",
      kern=True, beleg="app/kalender.php", bild="app-kalender",
      sehen=["Woche und Tag", "Mehrere Trainer nebeneinander", "Mehrere Standorte",
             "Abwesenheiten und Sperrzeiten"],
      tun=["Termin anlegen und verschieben", "Nach Trainer filtern"],
      nutzen="Ein Kalender für den Betrieb – nicht drei, die nicht zusammenpassen."),

    M("bookings", "Buchungen", "kunden", "starter", "bookings",
      "Leistungen, Verfügbarkeiten, Pakete und Online-Buchung.",
      kern=True, beleg="app/buchungen.php, app/buchung.php, app/verfuegbarkeit.php, buchen.php",
      bild="app-buchungen", seite="/funktionen/buchungen/",
      sehen=["Alle Termine mit Status", "Wer gebucht hat und worüber",
             "Warteliste", "Erinnerungen, die rausgegangen sind"],
      tun=["Verfügbarkeiten je Leistung und Trainer festlegen",
           "Termine bestätigen, verschieben, absagen",
           "Die Online-Buchung auf der eigenen Website freigeben"],
      nutzen="Kunden buchen selbst, zu den Zeiten, die du freigegeben hast."),

    M("packages", "Pakete", "kunden", "starter", "ticket",
      "Zehnerkarten und Guthaben: anlegen, verkaufen, verbrauchen.",
      beleg="app/pakete.php", bild="app-pakete",
      sehen=["Welche Pakete verkauft sind", "Wie viele Einheiten offen sind",
             "Wann ein Paket ausläuft"],
      tun=["Pakete anlegen und verkaufen", "Einheiten einem Termin zuordnen"],
      nutzen="Zehnerkarten auf Papier führen niemanden mehr in die Irre."),

    M("training", "Training", "training", "pro", "training",
      "Trainingspläne, Übungsbibliothek und Leistungsdaten.",
      beleg="app/training.php, app/trainingsplan.php, app/uebungen.php",
      bild="app-trainingsplan",
      sehen=["Pläne mit Wochen und Einheiten", "Eigene Übungsbibliothek",
             "Leistungswerte über die Zeit"],
      tun=["Plan bauen und einem Kunden zuweisen", "Übungen anlegen",
           "Werte eintragen"],
      nutzen="Was zwischen zwei Stunden passieren soll, steht schriftlich beim Schüler."),

    M("video", "Videoanalyse", "training", "business", "video",
      "Schwunganalyse mit Zeichenwerkzeugen und Einzelbildschritt.",
      beleg="app/videoanalyse.php, app/videos.php, assets/js/video.js",
      bild="app-videoanalyse",
      sehen=["Aufnahmen je Kunde", "Zeichnungen auf dem Einzelbild",
             "KI-Hinweise und Pro-Analyse als getrennte Blöcke"],
      tun=["Einzelbild vor und zurück", "Linien und Winkel zeichnen",
           "Analyse für den Schüler freigeben"],
      nutzen="Die fachliche Bewertung bleibt beim Trainer – und man sieht, dass sie es ist."),

    M("courses", "Kurse", "training", "pro", "courses",
      "Online-Kurse mit Modulen, Lektionen, Quiz und Zertifikat.",
      beleg="app/kurse.php, app/kurs.php, lib/Courses.php", bild="app-kurs-detail",
      seite="/funktionen/kurse/",
      sehen=["Module und Lektionen", "Wer wie weit gekommen ist", "Quizergebnisse"],
      tun=["Kurs aufbauen", "Lektionen als Text oder Video anlegen",
           "Kurs verkaufen oder freigeben", "Zertifikat ausstellen"],
      nutzen="Theorie einmal aufnehmen statt fünfzigmal erzählen."),

    M("products", "Produkte", "verkauf", "pro", "products",
      "Pakete, Gutscheine, Kurse und Merchandise verkaufen.",
      beleg="app/produkte.php, app/gutscheine.php, lib/Commerce.php",
      bild="app-produkte",
      sehen=["Alle Artikel mit Preis und Status", "Rabatte", "Bestellungen"],
      tun=["Artikel anlegen", "Gutscheine ausgeben", "Auf der Website zeigen"],
      nutzen="Was du verkaufst, steht an einer Stelle – und kommt von dort auf die Website."),

    M("payments", "Zahlungen", "verkauf", "pro", "payments",
      "Kartenzahlung, SEPA, Apple Pay und Abos über Stripe.",
      beleg="lib/Stripe.php, webhook.php, kaufen.php, app/zahlungen.php",
      bild="app-zahlungen",
      sehen=["Eingegangene Zahlungen", "Offene Beträge"],
      tun=["Stripe-Schlüssel hinterlegen", "Auf Rechnung verkaufen, wenn kein Stripe da ist"],
      nutzen="Ohne Stripe-Konto funktioniert der Verkauf trotzdem – dann eben auf Rechnung."),

    M("invoices", "Rechnungen", "verkauf", "pro", "invoices",
      "Rechnungen, Gutschriften und offene Posten.",
      beleg="app/rechnungen.php, app/rechnung.php, lib/Invoices.php, lib/PDF.php",
      bild="app-rechnung",
      sehen=["Alle Rechnungen mit Status und Fälligkeit", "Offene Posten"],
      tun=["Rechnung schreiben und als PDF ausgeben", "Gutschrift erstellen",
           "Zahlung vermerken"],
      nutzen="Rechnungsnummern ohne Lücken. Korrigiert wird mit einer Gutschrift, "
             "gelöscht wird nie."),

    M("website", "Website", "web", "starter", "website",
      "Baukasten, Seiten, Landingpages und Design.",
      kern=True, beleg="app/website.php, app/seite.php, lib/Bloecke.php, lib/Renderer.php, site.php",
      bild="app-baukasten", seite="/funktionen/website/",
      sehen=["Alle Seiten mit Status", "Den Aufbau einer Seite als Liste von Bausteinen",
             "Die Vorschau in Desktop, Tablet und Telefon"],
      tun=["Bausteine hinzufügen und per Griff umsortieren",
           "Texte und Bilder ändern", "Seitentitel und Beschreibung für Suchmaschinen setzen",
           "Veröffentlichen oder als Entwurf lassen"],
      nutzen="Eine Änderung an der Website dauert Minuten und braucht niemanden sonst."),

    M("content", "Inhalte", "web", "starter", "content",
      "Blog, Beiträge, Kategorien und Mediathek.",
      kern=False, beleg="app/inhalte.php, app/beitrag.php, app/medien.php",
      bild="app-inhalte",
      sehen=["Beiträge mit Status und Aufrufen", "Kategorien", "Hochgeladene Bilder und Dokumente"],
      tun=["Beitrag schreiben und veröffentlichen", "Bilder hochladen"],
      nutzen="Ein Beitrag über die Platzreife beantwortet die Frage, die sonst jeder einzeln stellt."),

    M("events", "Events", "web", "pro", "events",
      "Workshops, Camps, Turniere und Gruppentrainings.",
      beleg="app/events.php, app/event.php, lib/Events.php", bild="app-events",
      sehen=["Termine mit Plätzen und Anmeldungen"],
      tun=["Event anlegen", "Anmeldungen verwalten", "Auf der Website zeigen"],
      nutzen="Ein Camp mit zwölf Plätzen füllt sich, ohne dass du mitzählst."),

    M("travel", "Reisen", "web", "pro", "globe",
      "Golfreisen mit Hotel, Zimmerwahl, Anzahlung und Anmeldung.",
      beleg="app/reisen.php, app/reise.php, reise.php, lib/Trips.php", bild="app-reisen",
      sehen=["Reisen mit Programm und Plätzen", "Anmeldungen mit Zimmerwunsch"],
      tun=["Reise anlegen", "Anzahlung festlegen", "Anmeldungen führen"],
      nutzen="Die Golfwoche organisiert sich nicht von allein – aber an einer Stelle."),

    M("marketing", "Marketing", "wachstum", "pro", "marketing",
      "Kampagnen, Formulare und Social-Media-Inhalte.",
      beleg="app/marketing.php, app/kampagne.php, lib/Campaigns.php", bild="app-kampagne",
      sehen=["Kampagnen mit Zielgruppe und Ergebnis", "Formulare und ihre Eingänge"],
      tun=["Kampagne aufsetzen", "Formular bauen und auf eine Seite stellen"],
      nutzen="Ein Formular auf der Website landet als Anfrage im CMS, nicht im Postfach."),

    M("newsletter", "Newsletter", "wachstum", "pro", "newsletter",
      "Newsletter bauen, segmentieren, planen und auswerten.",
      beleg="app/newsletter.php, app/segmente.php, abmelden-newsletter.php, api.php",
      bild="app-newsletter",
      sehen=["Versendete Newsletter", "Segmente und wie viele darin sind"],
      tun=["Newsletter schreiben und planen", "Segment nach Bedingungen bauen",
           "Empfänger über die Schnittstelle an ein anderes System geben"],
      nutzen="Abmeldungen laufen automatisch – das ist keine Kür, sondern Pflicht."),

    M("automations", "Automationen", "wachstum", "business", "automations",
      "Abläufe aus Auslöser, Bedingung, Wartezeit und Aktion.",
      beleg="app/automationen.php, app/automation.php, lib/Automations.php",
      bild="app-automation",
      sehen=["Alle Abläufe und ihre Läufe"],
      tun=["Ablauf bauen: Auslöser, Bedingung, Wartezeit, Aktion",
           "Ein- und ausschalten"],
      nutzen="Die Willkommensmail nach der ersten Buchung schreibt sich einmal."),

    M("community", "Community", "wachstum", "business", "community",
      "Gruppen, Beiträge, Challenges und Ranglisten.",
      beleg="app/community.php, lib/Community.php, lib/Gamification.php",
      bild="app-community",
      sehen=["Gruppen und Beiträge", "Challenges und Ranglisten"],
      tun=["Gruppe anlegen", "Challenge starten", "Abzeichen vergeben"],
      nutzen="Zwischen den Stunden passiert auch etwas."),

    M("analytics", "Auswertung", "wissen", "business", "analytics",
      "Umsatz, Auslastung, Retention und Websitezahlen.",
      beleg="app/auswertung.php, lib/Analytics.php", bild="app-auswertung",
      sehen=["Umsatz über die Zeit", "Auslastung", "Wiederkehrende Kunden",
             "Besucherzahlen der eigenen Website"],
      tun=["Zeitraum wählen", "Nach Leistung und Trainer aufschlüsseln"],
      nutzen="Die Websitestatistik kommt ohne Cookies und ohne gespeicherte IP-Adresse aus."),

    M("ai", "KI-Assistent", "wissen", "business", "ai",
      "Fragen in normaler Sprache, Empfehlungen, Textentwürfe.",
      beleg="app/ki.php, lib/KI.php", bild="app-ki",
      sehen=["Antworten auf Fragen zu den eigenen Zahlen", "Textvorschläge"],
      tun=["Fragen stellen", "Entwürfe übernehmen oder verwerfen"],
      nutzen="Die KI entscheidet nichts. Preise, Kundendaten, Rechnungen und Versand "
             "laufen immer über eine ausdrückliche Bestätigung. Ohne API-Schlüssel "
             "schreiben die Textwerkzeuge mit einem eingebauten, regelbasierten "
             "Generator weiter."),

    M("settings", "Einstellungen", "system", "starter", "settings",
      "Profil, Team, Standorte, Zahlungen, Recht und Tarif.",
      kern=True, beleg="app/einstellungen.php, app/team.php, app/standorte.php, app/tarif.php",
      bild="app-einstellungen",
      sehen=["Alle Grundeinstellungen des Betriebs", "Team mit Rollen", "Standorte",
             "Welche Bereiche im Menü erscheinen"],
      tun=["Module ein- und ausschalten", "Team einladen und Rollen vergeben",
           "Impressum, Datenschutz und Stornofrist pflegen"],
      nutzen="Wer nur unterrichtet, schaltet ab, was er nicht braucht – und sieht neun "
             "Menüpunkte statt zweiundzwanzig."),
]

MODULE_NACH_KEY = {m["key"]: m for m in MODULE}

GRUPPEN = {
    "": "",
    "kunden": "Kunden & Termine",
    "training": "Training",
    "verkauf": "Verkauf",
    "web": "Website",
    "wachstum": "Wachstum",
    "wissen": "Wissen",
    "system": "System",
}


# ------------------------------------------------------------------ Tarife --
#
# Belegt: lib/Module.php, Module::plaene(). Die Stufen steuern im CMS, welche
# Bereiche einschaltbar sind. Eine Abrechnung ist im Produkt nicht enthalten –
# darum steht auf der Preisseite kein Kaufknopf.

TARIFE = [
    dict(key="starter", name="Starter", preis=29,
         zeile="Website und Buchung – alles, um online zu starten.",
         enthalten=["Website-Baukasten", "Online-Buchung", "Kundenakte", "Kalender", "Blog"]),
    dict(key="pro", name="Pro", preis=59, hervor=True,
         zeile="Das volle Geschäft: Verkauf, Rechnungen, Marketing.",
         enthalten=["Alles aus Starter", "Leads & Pipeline", "Produkte & Pakete",
                    "Zahlungen", "Rechnungen", "Newsletter", "Trainingspläne",
                    "Kurse", "Events"]),
    dict(key="business", name="Business", preis=99,
         zeile="Mit KI, Videoanalyse und vollständiger Auswertung.",
         enthalten=["Alles aus Pro", "KI-Assistent", "Videoanalyse", "Automationen",
                    "Auswertung", "Community", "Smart Pricing"]),
    dict(key="academy", name="Academy", preis=199,
         zeile="Für Akademien: mehrere Trainer, Standorte, eigene Marke.",
         enthalten=["Alles aus Business", "Mehrere Trainer", "Mehrere Standorte",
                    "White Label", "Eigene Domain", "Rollen & Rechte",
                    "Vorrangiger Support"]),
]


# ------------------------------------------------------------ Bildlegenden --
#
# Jede Aufnahme stammt aus einer lokalen Installation des CMS mit dem
# Demo-Workspace, den install.php anlegt. Nichts ist nachgestellt.

BILDER = {
    # --- Anwendung ---
    "app-dashboard":      ("Dashboard", "dashboard", "Umsatz, Auslastung, empfohlene Aktionen und die nächsten Termine."),
    "app-dashboard-mobile": ("Dashboard auf dem Telefon", "dashboard", "Dieselbe Oberfläche, für den Daumen gebaut."),
    "app-kalender":       ("Kalender", "kalender", "Woche über alle Trainer und Standorte."),
    "app-kunden":         ("Kundenliste", "kunden", "Alle Kunden mit Handicap, Status und letztem Termin."),
    "app-kundenakte":     ("Kundenakte", "kunden", "Historie, Pakete, Rechnungen und Notizen an einer Stelle."),
    "app-buchungen":      ("Buchungen", "buchungen", "Termine mit Status, Leistung und Trainer."),
    "app-buchung-detail": ("Termin", "buchungen", "Ein Termin mit Teilnehmern, Paketverbrauch und Erinnerungen."),
    "app-verfuegbarkeit": ("Verfügbarkeiten", "buchungen", "Wann welche Leistung online buchbar ist."),
    "app-leistungen":     ("Leistungen", "buchungen", "Was gebucht werden kann, wie lange es dauert, was es kostet."),
    "app-pakete":         ("Pakete", "buchungen", "Zehnerkarten mit verbrauchten und offenen Einheiten."),
    "app-website":        ("Website", "website", "Alle Seiten der eigenen Website mit Status."),
    "app-baukasten":      ("Baukasten", "website", "Bausteine links, Vorschau in der Mitte, Seiteneinstellungen rechts."),
    "app-design":         ("Design", "website", "Farbe, Schrift und Rundung der eigenen Website."),
    "app-seo":            ("Suchmaschinen", "website", "Titel und Beschreibung je Seite, mit Zeichenzähler."),
    "app-inhalte":        ("Inhalte", "inhalte", "Beiträge mit Status, Kategorie und Aufrufen."),
    "app-medien":         ("Mediathek", "inhalte", "Hochgeladene Bilder und Dokumente."),
    "app-kurse":          ("Kurse", "kurse", "Online-Kurse mit Modulen und Teilnehmern."),
    "app-kurs-detail":    ("Kurs", "kurse", "Module, Lektionen und der Fortschritt der Teilnehmer."),
    "app-training":       ("Training", "training", "Trainingspläne und zugewiesene Schüler."),
    "app-trainingsplan":  ("Trainingsplan", "training", "Wochen, Einheiten und Übungen eines Plans."),
    "app-uebungen":       ("Übungen", "training", "Die eigene Übungsbibliothek."),
    "app-videos":         ("Videos", "training", "Schwungaufnahmen je Kunde."),
    "app-videoanalyse":   ("Videoanalyse", "training", "Einzelbildschritt, Zeichenwerkzeuge, getrennte Blöcke für KI-Hinweise und Pro-Analyse."),
    "app-produkte":       ("Produkte", "verkauf", "Pakete, Gutscheine, Kurse und Merchandise."),
    "app-gutscheine":     ("Gutscheine", "verkauf", "Ausgegebene Gutscheine und ihr Restwert."),
    "app-zahlungen":      ("Zahlungen", "verkauf", "Eingegangene Zahlungen und offene Beträge."),
    "app-rechnungen":     ("Rechnungen", "verkauf", "Rechnungen mit Status, Fälligkeit und offenen Posten."),
    "app-rechnung":       ("Rechnung", "verkauf", "Positionen mit eigenem Titel, Preis und Steuersatz."),
    "app-leads":          ("Leads", "kunden", "Anfragen mit Quelle, Wert und Stufe."),
    "app-segmente":       ("Segmente", "wachstum", "Zielgruppen aus Bedingungen zusammengesetzt."),
    "app-marketing":      ("Marketing", "wachstum", "Kampagnen und Formulare."),
    "app-kampagne":       ("Kampagne", "wachstum", "Eine Kampagne mit Zielgruppe, Inhalt und Ergebnis."),
    "app-newsletter":     ("Newsletter", "wachstum", "Versand, Planung und Auswertung."),
    "app-automationen":   ("Automationen", "wachstum", "Abläufe aus Auslöser, Bedingung, Wartezeit und Aktion."),
    "app-automation":     ("Automation", "wachstum", "Ein Ablauf im Detail."),
    "app-community":      ("Community", "wachstum", "Gruppen, Beiträge und Challenges."),
    "app-auswertung":     ("Auswertung", "auswertung", "Umsatz, Auslastung und Websitezahlen."),
    "app-ki":             ("KI-Assistent", "auswertung", "Fragen zu den eigenen Zahlen, in normaler Sprache."),
    "app-events":         ("Events", "website", "Workshops, Camps und Turniere mit Anmeldungen."),
    "app-reisen":         ("Reisen", "website", "Golfreisen mit Programm, Plätzen und Anmeldungen."),
    "app-einstellungen":  ("Einstellungen", "system", "Grunddaten des Betriebs."),
    "app-tarif":          ("Tarif und Umfang", "system", "Hier legt jeder selbst fest, welche Bereiche im Menü erscheinen."),
    "app-team":           ("Team", "system", "Trainer und Assistenz mit Rollen und Rechten."),
    "app-standorte":      ("Standorte", "system", "Club, Range, Indoor – jeder mit eigenen Zeiten."),
    "app-profil":         ("Profil", "system", "Die eigenen Daten und das Bild für die Website."),
    "app-protokoll":      ("Protokoll", "system", "Wer wann was geändert hat."),
    "app-aufgaben":       ("Aufgaben", "system", "Was noch zu tun ist."),

    # --- Öffentlich ---
    "pub-site-start":     ("Website: Startseite", "kundensicht", "So sieht die Website aus, die der Baukasten erzeugt."),
    "pub-site-ueber-mich":("Website: Über mich", "kundensicht", "Eine Unterseite aus denselben Bausteinen."),
    "pub-site-preise":    ("Website: Preise", "kundensicht", "Leistungen und Pakete, direkt aus dem CMS."),
    "pub-site-landing":   ("Website: Landingpage", "kundensicht", "Eine Landingpage für einen einzelnen Kurs."),
    "pub-buchen":         ("Online-Buchung", "kundensicht", "Drei Schritte: Zeit wählen, Angaben, Bestätigung."),
    "pub-portal":         ("Kundenportal", "kundensicht", "Termine, Pakete, Rechnungen und Kurse für den Schüler."),
}


# ------------------------------------------------------------- Navigation --

NAV = [
    dict(name="Produkt", typ="mega", breit=True, spalten=[
        dict(titel="Produkt", eintraege=[
            ("/produkt/", "Überblick", "Wie die Bereiche zusammenhängen.", "dashboard"),
            ("/funktionen/", "Alle Funktionen", "Was tatsächlich drin ist.", "grid"),
            ("/funktionen/dashboard/", "Dashboard", "Alles Wichtige auf einen Blick.", "dashboard"),
            ("/funktionen/website/", "Website", "Deine professionelle Online-Präsenz.", "website"),
        ]),
        dict(titel="Bereiche", eintraege=[
            ("/funktionen/kurse/", "Kurse & Training", "Angebote und Trainings verwalten.", "courses"),
            ("/funktionen/buchungen/", "Buchungen", "Termine und Buchungen im Überblick.", "bookings"),
            ("/vorteile/", "Vorteile", "Was sich im Alltag ändert.", "check"),
            ("/preise/", "Stufen & Umfang", "Was in welcher Stufe enthalten ist.", "euro"),
        ]),
    ]),
    dict(name="Für wen?", typ="mega", breit=False, spalten=[
        dict(titel="Für wen", eintraege=[
            ("/fuer-golfpros/", "Golfpros", "Eigenes Business, eigener Auftritt.", "customers"),
            ("/fuer-golflehrer/", "Golflehrer", "Mehr Unterricht, weniger Technik.", "training"),
            ("/fuer-golfakademien/", "Golfakademien", "Mehrere Trainer und Standorte.", "building"),
        ]),
    ]),
    dict(name="Demo", typ="mega", breit=True, spalten=[
        dict(titel="Selbst ansehen", eintraege=[
            ("/demo/", "Produktdemo", "Klick dich durch die Bereiche.", "play"),
            ("/demo/produkt-tour/", "Produkt-Tour", "Geführter Rundgang in fünf Schritten.", "route"),
        ]),
        dict(titel="Ergebnis", eintraege=[
            ("/demo/beispiel-website/", "Beispiel-Website", "Die Website, die dabei herauskommt.", "website"),
            ("/demo/screenshots/", "Screenshots", "Alle Bereiche in groß.", "image"),
        ]),
    ]),
    dict(name="Vorteile", typ="link", url="/vorteile/"),
    dict(name="Preise", typ="link", url="/preise/"),
    dict(name="Über uns", typ="mega", breit=False, spalten=[
        dict(titel="Über uns", eintraege=[
            ("/ueber-uns/", "Über GolfProCMS", "Warum es das Produkt gibt.", "info"),
            ("/faq/", "Häufige Fragen", "Kurz und ohne Marketing.", "help"),
            ("/kontakt/", "Kontakt", "Demo anfragen oder nachfragen.", "mail"),
        ]),
    ]),
]

FUSS = [
    ("Produkt", [
        ("/produkt/", "Überblick"),
        ("/funktionen/", "Alle Funktionen"),
        ("/funktionen/dashboard/", "Dashboard"),
        ("/funktionen/website/", "Website"),
        ("/funktionen/kurse/", "Kurse & Training"),
        ("/funktionen/buchungen/", "Buchungen"),
    ]),
    ("Ansehen", [
        ("/demo/", "Produktdemo"),
        ("/demo/produkt-tour/", "Produkt-Tour"),
        ("/demo/beispiel-website/", "Beispiel-Website"),
        ("/demo/screenshots/", "Screenshots"),
    ]),
    ("Für wen", [
        ("/fuer-golfpros/", "Golfpros"),
        ("/fuer-golflehrer/", "Golflehrer"),
        ("/fuer-golfakademien/", "Golfakademien"),
        ("/vorteile/", "Vorteile"),
    ]),
    ("Mehr", [
        ("/preise/", "Stufen & Umfang"),
        ("/faq/", "Häufige Fragen"),
        ("/ueber-uns/", "Über uns"),
        ("/kontakt/", "Kontakt"),
    ]),
]
