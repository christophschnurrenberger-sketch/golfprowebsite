# -*- coding: utf-8 -*-
"""Seiten für Golfpros, Golflehrer und Golfakademien."""

import daten as D
from icons import icon
from layout import e
import bausteine as B


def _zielgruppe(pfad, titel, vorzeile, fuehrung, bereiche, alltag, bilder,
                beschreibung, schluss_titel, zusatz="", seo_titel=None):
    karten = []
    for key, warum in bereiche:
        m = D.MODULE_NACH_KEY[key]
        karten.append(B.karte(m["name"], e(warum), m["icon"],
                              url=m.get("seite") or "/funktionen/#gruppe-" + (m["gruppe"] or "kern"),
                              link_text="Ansehen"))

    inhalt = [
        B.seitenkopf(vorzeile, titel, fuehrung,
                     knoepfe=B.knopf("Produktdemo ansehen", "/demo/", "primaer", "play",
                                     "product_demo_start")
                             + B.knopf("Persönliche Demo anfragen", "/kontakt/?anliegen=demo",
                                       "zweit", "mail"),
                     visual=B.screenshot_block(bilder[0], lazy=False)),
        B.abschnitt(
            B.kopfblock("Im Alltag", "Drei Situationen, die du kennst.", "")
            + B.raster([B.karte(t, x, s) for t, x, s in alltag], 3),
            art="beige",
        ),
        B.abschnitt(
            B.kopfblock("Die Bereiche", "Womit du hier arbeitest.",
                        "Alles davon ist im Produkt vorhanden. Was du davon "
                        "einschaltest, entscheidest du selbst.")
            + B.raster(karten, 3),
            art="weiss",
        ),
    ]
    if len(bilder) > 1:
        inhalt.append(B.abschnitt(
            '<div class="raster raster--2">%s</div>'
            % "".join('<div>%s</div>' % B.screenshot_block(b) for b in bilder[1:3]),
        ))
    if zusatz:
        inhalt.append(zusatz)
    inhalt.append(B.schluss_cta(titel=schluss_titel))

    return {
        "pfad": pfad,
        "titel": titel,
        "seo_titel": seo_titel or vorzeile,
        "beschreibung": beschreibung,
        "krumen": [("/", "Start"), (pfad, titel.split(",")[0])],
        "inhalt": "".join(inhalt),
    }


def golfpros():
    return _zielgruppe(
        "/fuer-golfpros/",
        "Für Golfpros, die ihr Business selbst in der Hand haben.",
        "Für Golfpros",
        "Du unterrichtest selbstständig, hast eigene Angebote und einen Namen, für den "
        "du arbeitest. Der digitale Teil davon – Website, Termine, Kunden, Rechnungen – "
        "soll funktionieren, ohne dein Hauptthema zu werden.",
        [
            ("website", "Deine Seite, in deiner Handschrift – und von dir änderbar."),
            ("bookings", "Zeiten freigeben, Kunden buchen lassen, Kalender bleibt sauber."),
            ("customers", "Wer kommt, woran ihr arbeitet, was noch offen ist."),
            ("packages", "Zehnerkarten mit gezählten Einheiten statt Strichliste."),
            ("invoices", "Rechnungen mit lückenlosen Nummern und Gutschriften."),
            ("content", "Ein Beitrag beantwortet die Frage, die sonst jeder einzeln stellt."),
        ],
        [
            ("Der Preis ändert sich",
             "Du erhöhst die Einzelstunde. Im CMS ein Feld, auf der Website sofort "
             "sichtbar – Preisseite, Buchung und Leistungsliste zugleich.", "euro"),
            ("Jemand fragt nach einem Termin",
             "Statt fünf Nachrichten hin und her schickst du den Link auf deine "
             "Buchungsseite. Dort steht, was frei ist.", "calendar"),
            ("Eine Zehnerkarte ist alle",
             "Das Dashboard sagt es dir, bevor der Kunde fragt – und bevor die "
             "Einheiten verfallen.", "ticket"),
        ],
        ["app-dashboard", "app-baukasten", "app-kundenakte"],
        ("GolfProCMS für selbstständige Golf Professionals: eigene Website, "
         "Online-Buchung, Kundenakte, Pakete und Rechnungen in einer Anwendung."),
        "Dein Business. Dein Auftritt.<br>Dein System.",
    )


def golflehrer():
    return _zielgruppe(
        "/fuer-golflehrer/",
        "Mehr Fokus auf Unterricht. Weniger Aufwand mit Technik.",
        "Für Golflehrer",
        "Du gibst Stunden. Die Website ist Mittel zum Zweck und soll sich nicht wie "
        "ein zweiter Beruf anfühlen. GolfProCMS ist darauf ausgelegt, dass du neun "
        "Menüpunkte siehst und nicht zweiundzwanzig.",
        [
            ("website", "Seiten aus Bausteinen. Ändern heißt: Text anklicken, tippen, speichern."),
            ("bookings", "Freie Zeiten stehen online. Der Rest kommt von allein."),
            ("calendar", "Woche und Tag, auch wenn mehrere Trainer eingetragen sind."),
            ("customers", "Kurze Notiz nach der Stunde – beim nächsten Mal weißt du es wieder."),
            ("training", "Was bis zur nächsten Stunde geübt werden soll, schriftlich."),
            ("video", "Schwunganalyse mit Einzelbildschritt und Zeichenwerkzeugen."),
        ],
        [
            ("Zwischen zwei Stunden",
             "Zehn Minuten auf dem Telefon: Notiz zur letzten Stunde, Blick auf den "
             "Nachmittag. Die Oberfläche ist dafür gebaut, nicht nur verkleinert.", "smartphone"),
            ("Nach dem Training",
             "Trainingsplan zuweisen, damit dein Schüler weiß, woran er arbeitet – "
             "aus deiner eigenen Übungsbibliothek.", "training"),
            ("Video vom Abschlag",
             "Aufnahme hochladen, Linie ziehen, Analyse freigeben. KI-Hinweise und "
             "deine Bewertung stehen getrennt nebeneinander.", "video"),
        ],
        ["app-dashboard-mobile", "app-trainingsplan", "app-videoanalyse"],
        ("GolfProCMS für Golflehrer: Website ohne Technikaufwand, Online-Buchung, "
         "Trainingspläne und Videoanalyse."),
        "Weniger Website-Arbeit.<br>Mehr Golfunterricht.",
        zusatz=B.abschnitt(
            B.kopfblock("Der Umfang", "Du bestimmst, was du siehst.",
                        "Sechs Bereiche sind immer da: Dashboard, Website, Kunden, "
                        "Kalender, Buchungen, Einstellungen. Alles Weitere schaltest du "
                        "ein, wenn du es brauchst – und wieder aus, wenn nicht. "
                        "Ausgeschaltet heißt nicht gelöscht.")
            + B.screenshot_block("app-tarif"),
            art="beige",
        ),
    )


def golfakademien():
    return _zielgruppe(
        "/fuer-golfakademien/",
        "Eine digitale Basis für deine Golfakademie.",
        "Für Golfakademien",
        "Mehrere Trainer, mehrere Standorte, gemeinsame Angebote – und trotzdem eine "
        "Website und ein Kalender. GolfProCMS kennt Rollen, Standorte und getrennte "
        "Verfügbarkeiten.",
        [
            ("settings", "Vier Rollen: Inhaber, Head Pro, Trainer, Assistenz."),
            ("calendar", "Alle Trainer nebeneinander, über mehrere Standorte."),
            ("bookings", "Verfügbarkeiten je Leistung, je Trainer, je Standort."),
            ("courses", "Kurse und Lehrgänge mit Modulen, Quiz und Zertifikat."),
            ("events", "Camps, Workshops und Turniere mit Plätzen und Anmeldungen."),
            ("analytics", "Umsatz und Auslastung, nach Leistung und Trainer aufgeschlüsselt."),
        ],
        [
            ("Ein Trainer meldet sich an",
             "Er sieht seine Termine, nicht den Umsatz des Betriebs. Die Rolle "
             "entscheidet, was im Menü steht.", "customers"),
            ("Zwei Standorte, andere Zeiten",
             "Club und Indoor-Studio haben eigene Öffnungszeiten und eigene "
             "Verfügbarkeiten – im selben Kalender.", "building"),
            ("Ein Camp füllt sich",
             "Anmeldungen laufen über die Website, die Plätze zählt das System.", "events"),
        ],
        ["app-kalender", "app-team", "app-standorte"],
        ("GolfProCMS für Golfakademien: mehrere Trainer und Standorte, Rollen und "
         "Rechte, gemeinsame Website, Kurse und Events."),
        "Eine Akademie.<br>Ein System.",
        zusatz=B.abschnitt(
            B.kopfblock("Mandanten", "Mehrere Betriebe auf einer Installation.",
                        "Jeder Datenbankzugriff läuft im Produkt über eine Klasse, die "
                        "die Zuordnung zum Betrieb selbst in jede Bedingung setzt. Man "
                        "kann den Filter nicht vergessen, weil man ihn nie schreibt – "
                        "ein fremder Datensatz kommt nicht zurück, auch nicht "
                        "versehentlich.")
            + B.raster([
                B.karte("Getrennte Bereiche",
                        "Der Demo-Bestand liegt in einem zweiten, vollständig "
                        "getrennten Bereich. Ausprobieren, ohne eigene Daten "
                        "anzufassen.", "layers"),
                B.karte("Eigene Domain je Betrieb",
                        "Das System erkennt die Domain und liefert die dazugehörige "
                        "Website aus.", "globe"),
                B.karte("Rollen und Rechte",
                        "Was jemand sehen und ändern darf, hängt an der Rolle – nicht "
                        "an der Absprache.", "lock"),
            ], 3),
            art="weiss",
        ),
    )
