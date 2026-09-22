# -*- coding: utf-8 -*-
"""Seiten für Golfpros, Golflehrer und Golfakademien."""

import daten as D
from icons import icon
from layout import e
import bausteine as B


def _zielgruppe(pfad, titel, vorzeile, fuehrung, bereiche, alltag, bilder,
                beschreibung, schluss_titel, zusatz="", seo_titel=None,
                fotoschluessel=None):
    """Eine Zielgruppenseite: Aufmacher, drei Situationen, Bereiche als Liste.

    Bewusst ohne Kachelraster – die drei Situationen sind eine Erzählung,
    keine Produktmatrix.
    """
    zeilen = []
    for key, warum in bereiche:
        m = D.MODULE_NACH_KEY[key]
        ziel = m.get("seite") or "/funktionen/#gruppe-" + (m["gruppe"] or "kern")
        zeilen.append(('<a href="%s">%s</a>' % (e(ziel), e(m["name"])), e(warum)))

    foto = B.foto_flaeche(fotoschluessel, "quer",
                          "Golfprofessional bei der Arbeit") if fotoschluessel else ""

    inhalt = [
        B.seitenkopf(vorzeile, titel, fuehrung,
                     knoepfe=B.knopf("Demo ansehen", "/demo/", "primaer",
                                     event="product_demo_start")
                             + B.knopf("Persönlich sprechen",
                                       "/kontakt/?anliegen=demo", "zweit"),
                     kompakt=True),
        # Aufmacher: Foto wenn vorhanden, sonst die Produktaufnahme.
        '<section style="padding-block:0 clamp(48px,6vw,96px)">'
        '<div class="huelle huelle--weit">%s</div></section>'
        % (foto if foto else B.bild_mit_legende(bilders[0] if False else bilder[0],
                                                "01", lazy=False)),

        # Drei Situationen als Kette, nicht als drei gleiche Kacheln.
        '<section class="abschnitt abschnitt--eng abschnitt--beige zeigen">'
        '<div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px);max-width:13ch">'
        "Drei Situationen, die du kennst.</h2></div>"
        "<div>%s</div></div></div></section>"
        % B.kette([(t, e(x)) for t, x, _sym in alltag]),

        # Bereiche als Liste.
        '<section class="abschnitt abschnitt--eng zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px);max-width:13ch">'
        "Womit du hier arbeitest.</h2>"
        '<p class="fuehrung" style="margin-top:var(--r5)">Alles davon ist im '
        "Produkt vorhanden. Was du einschaltest, entscheidest du selbst.</p></div>"
        "<div>%s</div></div></div></section>" % B.typoliste(zeilen),
    ]

    # Zwei weitere Aufnahmen, versetzt gesetzt statt nebeneinander gerastert.
    if len(bilder) > 1:
        inhalt.append(
            '<section class="abschnitt abschnitt--eng zeigen">'
            '<div class="huelle huelle--weit">'
            '<div class="paar paar--unten" style="--paar:minmax(0,7fr) minmax(0,5fr)">'
            "<div>%s</div><div style=\"padding-bottom:clamp(16px,4vw,56px)\">%s</div>"
            "</div></div></section>"
            % (B.bild_mit_legende(bilder[1], "02"),
               B.bild_mit_legende(bilder[2], "03") if len(bilder) > 2 else "")
        )

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
        ("TeePilot für selbstständige Golf Professionals: eigene Website, "
         "Online-Buchung, Kundenakte, Pakete und Rechnungen in einer Anwendung."),
        "Dein Business. Dein Auftritt.<br>Dein System.",
        fotoschluessel="golfpros",
    )


def golflehrer():
    return _zielgruppe(
        "/fuer-golflehrer/",
        "Mehr Fokus auf Unterricht. Weniger Aufwand mit Technik.",
        "Für Golflehrer",
        "Du gibst Stunden. Die Website ist Mittel zum Zweck und soll sich nicht wie "
        "ein zweiter Beruf anfühlen. TeePilot ist darauf ausgelegt, dass du neun "
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
        ("TeePilot für Golflehrer: Website ohne Technikaufwand, Online-Buchung, "
         "Trainingspläne und Videoanalyse."),
        "Weniger Website-Arbeit.<br>Mehr Golfunterricht.",
        fotoschluessel="golflehrer",
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
        "Website und ein Kalender. TeePilot kennt Rollen, Standorte und getrennte "
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
        ("TeePilot für Golfakademien: mehrere Trainer und Standorte, Rollen und "
         "Rechte, gemeinsame Website, Kurse und Events."),
        "Eine Akademie.<br>Ein System.",
        fotoschluessel="golfakademien",
        zusatz='<section class="abschnitt abschnitt--eng zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,44px);max-width:13ch">'
        "Mehrere Betriebe auf einer Installation.</h2>"
        '<p class="fuehrung" style="margin-top:var(--r5)">Jeder Datenbankzugriff '
        "läuft über eine Klasse, die die Zuordnung zum Betrieb selbst in jede "
        "Bedingung setzt. Man kann den Filter nicht vergessen, weil man ihn nie "
        "schreibt.</p></div>"
        "<div>%s</div></div></div></section>"
        % B.typoliste([
            ("Getrennte Bereiche",
             "Der Demo-Bestand liegt in einem zweiten, vollständig getrennten "
             "Bereich. Ausprobieren, ohne eigene Daten anzufassen."),
            ("Eigene Domain je Betrieb",
             "Das System erkennt die aufgerufene Domain und liefert die "
             "dazugehörige Website aus."),
            ("Rollen und Rechte",
             "Was jemand sehen und ändern darf, hängt an der Rolle – nicht an "
             "der Absprache."),
        ]),
    )
