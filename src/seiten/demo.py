# -*- coding: utf-8 -*-
"""Demo-Bereich: Produktdemo, geführte Tour, Beispiel-Website, Screenshots."""

import daten as D
from icons import icon
from layout import e
import bausteine as B


HINWEIS_DEMO = (
    '<div class="hinweiskasten hinweiskasten--sand">'
    "<h4>Was du hier siehst</h4>"
    "<p>Alle Aufnahmen stammen aus einer laufenden Installation von GolfProCMS mit "
    "dem Demo-Bestand, den der Installer auf Wunsch selbst anlegt: %d Kunden, "
    "%d Termine, %d Rechnungen, Kurse, Kampagnen und eine fertige Website. "
    "Die Namen sind erfunden, die Zahlen passen zueinander – die Paketeinheiten sind "
    "von echten Terminen verbraucht, der Umsatz entspricht den Preisen.</p></div>"
    % (D.DEMO_ZAHLEN["kunden"], D.DEMO_ZAHLEN["termine"], D.DEMO_ZAHLEN["rechnungen"])
)


# ----------------------------------------------------------------- /demo/ --

def demo():
    def cta(text, url, event):
        return '<a class="knopf knopf--zweit knopf--breit" href="%s" data-event="%s">%s</a>' \
               % (e(url), e(event), e(text))

    eintraege = [
        dict(key="dashboard", name="Dashboard", sym="dashboard", bild="app-dashboard",
             titel="Der Morgen",
             text="Umsatz, Auslastung und die nächsten Termine. Darunter Hinweise, die "
                  "aus deinen eigenen Zahlen kommen – offene Anfragen, überfällige "
                  "Rechnungen, Pakete, die auslaufen.",
             punkte=["Umsatz heute, Monat, Jahr – mit Vergleich",
                     "Auslastung der laufenden Woche",
                     "Die nächsten sechs Termine",
                     "Empfohlene Aktionen mit direktem Sprung"],
             cta=cta("Dashboard im Detail", "/funktionen/dashboard/", "feature_detail_click")),
        dict(key="website", name="Website", sym="website", bild="app-baukasten",
             titel="Der Baukasten",
             text="Links die Bausteine, in der Mitte die Vorschau, rechts die "
                  "Einstellungen der Seite. Umsortiert wird per Griff, geändert wird "
                  "an der Stelle, an der es steht.",
             punkte=["27 Bausteintypen",
                     "Vorschau für Desktop, Tablet und Telefon",
                     "Seitentitel und Beschreibung für Suchmaschinen",
                     "Veröffentlichen oder als Entwurf lassen"],
             cta=cta("Website im Detail", "/funktionen/website/", "feature_detail_click")),
        dict(key="bookings", name="Buchungen", sym="bookings", bild="app-buchungen",
             titel="Termine",
             text="Alle Buchungen mit Status, Leistung und Trainer. Daneben die "
                  "Verfügbarkeiten, die entscheiden, was online überhaupt wählbar ist.",
             punkte=["Verfügbarkeiten je Leistung und Trainer",
                     "Warteliste",
                     "Erinnerungen per E-Mail",
                     "Buchung mit Konto oder als Gast"],
             cta=cta("Buchungen im Detail", "/funktionen/buchungen/", "feature_detail_click")),
        dict(key="calendar", name="Kalender", sym="calendar", bild="app-kalender",
             titel="Die Woche",
             text="Wochen- und Tagesansicht über alle Trainer und Standorte. "
                  "Abwesenheiten und Sperrzeiten sind eingerechnet.",
             punkte=["Mehrere Trainer nebeneinander",
                     "Mehrere Standorte",
                     "Termine verschieben",
                     "Nach Trainer filtern"],
             cta=cta("Alle Funktionen", "/funktionen/", "feature_detail_click")),
        dict(key="customers", name="Kunden", sym="customers", bild="app-kundenakte",
             titel="Die Akte",
             text="Handicap, Historie, Pakete, Rechnungen und Notizen – an einer "
                  "Stelle. Vor der Stunde ein Blick hinein, und du weißt wieder, "
                  "woran ihr arbeitet.",
             punkte=["Alle bisherigen Termine",
                     "Pakete mit verbrauchten und offenen Einheiten",
                     "Notizen und Kommunikationshistorie",
                     "Eigene Felder und Etiketten"],
             cta=cta("Alle Funktionen", "/funktionen/", "feature_detail_click")),
        dict(key="courses", name="Kurse", sym="courses", bild="app-kurs-detail",
             titel="Kurse",
             text="Module, Lektionen, Quiz und Zertifikat. Wer wie weit gekommen ist, "
                  "steht direkt daneben.",
             punkte=["Lektionen als Text oder Video",
                     "Quiz mit Auswertung",
                     "Fortschritt je Teilnehmer",
                     "Verkaufen oder direkt zuweisen"],
             cta=cta("Kurse im Detail", "/funktionen/kurse/", "feature_detail_click")),
        dict(key="invoices", name="Rechnungen", sym="invoices", bild="app-rechnung",
             titel="Belege",
             text="Eine Rechnungsposition führt Titel, Preis und Steuersatz als eigene "
                  "Werte. Ändert sich später der Preis der Leistung, bleibt die "
                  "Rechnung, wie sie war.",
             punkte=["Lückenlose Rechnungsnummern",
                     "Gutschrift statt Löschung",
                     "Ausgabe als PDF",
                     "Offene Posten im Blick"],
             cta=cta("Alle Funktionen", "/funktionen/", "feature_detail_click")),
        dict(key="analytics", name="Auswertung", sym="analytics", bild="app-auswertung",
             titel="Zahlen",
             text="Umsatz über die Zeit, Auslastung, wiederkehrende Kunden und die "
                  "Besucherzahlen deiner Website – gezählt ohne Cookies.",
             punkte=["Zeitraum frei wählbar",
                     "Nach Leistung und Trainer aufschlüsseln",
                     "Websitestatistik ohne gespeicherte IP",
                     "Keine Einwilligung nötig"],
             cta=cta("Alle Funktionen", "/funktionen/", "feature_detail_click")),
        dict(key="ai", name="KI-Assistent", sym="ai", bild="app-ki",
             titel="Fragen stellen",
             text="Fragen zu den eigenen Zahlen, in normaler Sprache. Die KI "
                  "entscheidet nichts – Preisänderungen, Kundendaten, Rechnungen und "
                  "Versand laufen immer über eine ausdrückliche Bestätigung.",
             punkte=["Antworten zu den eigenen Daten",
                     "Textentwürfe für Website und Newsletter",
                     "Ohne API-Schlüssel schreibt ein regelbasierter Generator weiter",
                     "Vorschlag, keine Ausführung"],
             cta=cta("Alle Funktionen", "/funktionen/", "feature_detail_click")),
        dict(key="settings", name="Einstellungen", sym="settings", bild="app-tarif",
             titel="Umfang festlegen",
             text="Hier entscheidest du, welche Bereiche im Menü erscheinen. "
                  "Ausgeschaltet heißt nicht gelöscht – die Daten bleiben.",
             punkte=["Module ein- und ausschalten",
                     "Team mit vier Rollen",
                     "Mehrere Standorte",
                     "Impressum, Datenschutz, Stornofrist"],
             cta=cta("Alle Funktionen", "/funktionen/", "feature_detail_click")),
    ]

    inhalt = [
        B.seitenkopf(
            "Produktdemo", "GolfProCMS selbst erleben.",
            "Klick dich durch die wichtigsten Bereiche und sieh dir an, wie "
            "GolfProCMS aufgebaut ist. Keine Anmeldung, keine Eingabe – du siehst "
            "genau das, was ein Golfpro nach dem Anmelden sieht.",
            knoepfe=B.knopf("Lieber geführt? Produkt-Tour starten", "/demo/produkt-tour/",
                            "zweit", "route", "product_tour_start"),
            kompakt=True,
        ),
        B.abschnitt(B.demo_tafel(eintraege) + '<div class="mt-6">%s</div>' % HINWEIS_DEMO,
                    art="beige abschnitt--eng"),
        B.abschnitt(
            B.kopfblock("Und das Ergebnis?", "Am Ende steht eine Website.",
                        "Der Baukasten ist kein Selbstzweck. Was dabei herauskommt, "
                        "ist die öffentliche Seite deiner Golfschule.", mitte=True)
            + B.geraete({
                "desktop": "pub-site-start-full",
                "tablet": "pub-site-start-tablet",
                "mobile": "pub-site-start-mobile",
            }, gruppe="demo_ergebnis")
            + '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div>'
              % (B.knopf("Beispiel-Website ansehen", "/demo/beispiel-website/", "primaer",
                         "eye", "demo_website_open"),
                 B.knopf("Alle Screenshots", "/demo/screenshots/", "zweit", "image",
                         "screenshot_gallery_open")),
        ),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            "<h2>Jetzt selbst ausprobieren.</h2>"
            '<p class="fuehrung mt-5">Ein eigener Zugang mit dem Demo-Bestand ist '
            "schnell eingerichtet. Schreib kurz, für welchen Betrieb – dann melden "
            "wir uns mit den Zugangsdaten.</p>"
            '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div></div>'
            % (B.knopf("Zugang anfragen", "/kontakt/?anliegen=test", "hell", "mail",
                       "trial_click"),
               B.knopf("Stufen und Umfang", "/preise/", "rand-hell")),
            art="dunkel",
        ),
    ]

    return {
        "pfad": "/demo/",
        "titel": "Produktdemo",
        "beschreibung": ("Die interaktive Produktdemo von GolfProCMS: Dashboard, "
                         "Website-Baukasten, Buchungen, Kunden, Kurse und Auswertung – "
                         "mit echten Aufnahmen aus dem laufenden System."),
        "og_text": "Klick dich durch GolfProCMS – ohne Anmeldung.",
        "krumen": [("/", "Start"), ("/demo/", "Demo")],
        "inhalt": "".join(inhalt),
    }


# ------------------------------------------------- /demo/produkt-tour/ --

def tour():
    schritte = [
        ("Dashboard", "app-dashboard",
         "Der Morgen beginnt mit Zahlen, nicht mit Suchen.",
         "Umsatz, Auslastung, die nächsten Termine – und Hinweise, die aus deinen "
         "eigenen Daten berechnet sind. Jeder Hinweis führt direkt dorthin, wo er "
         "herkommt.",
         "Du weißt in zehn Sekunden, was heute ansteht."),
        ("Website", "app-baukasten",
         "Die Website baust du selbst.",
         "Links die Bausteine, in der Mitte die Vorschau, rechts die Einstellungen. "
         "Ein neuer Preis ist eine Änderung im Textfeld, keine Anfrage an jemanden, "
         "der Zeit hat.",
         "Eine Änderung dauert Minuten statt Tage."),
        ("Buchungen", "app-verfuegbarkeit",
         "Du gibst Zeiten frei, dein Kunde bucht.",
         "Verfügbarkeiten legst du je Leistung und je Trainer fest. Was frei ist, "
         "erscheint auf deiner Website – buchbar mit Konto oder als Gast.",
         "Weniger Abstimmung über fünf Kanäle."),
        ("Kunden", "app-kundenakte",
         "Alles zu einem Schüler an einer Stelle.",
         "Handicap, Historie, gekaufte Pakete mit offenen Einheiten, Rechnungen und "
         "Notizen. Vor der Stunde ein Blick hinein.",
         "Du erinnerst dich an das, woran ihr zuletzt gearbeitet habt."),
        ("Das Ergebnis", "pub-site-start-full",
         "Am Ende steht eine Website, die nach dir aussieht.",
         "Was du im CMS pflegst, erscheint öffentlich: Leistungen, Preise, Kurse, "
         "freie Termine. Kein zweites System, kein Export.",
         "Ein Auftritt, der zu deinem Unterricht passt."),
    ]

    punkte, tafeln = [], []
    for i, (name, bild, titel, text, nutzen) in enumerate(schritte):
        punkte.append(
            '<button type="button" role="tab" data-tour-punkt aria-selected="%s" '
            'class="wechsel__knopf">'
            '<span class="wechsel__nr">%02d</span>'
            '<span class="wechsel__name">%s</span></button>'
            % ("true" if i == 0 else "false", i + 1, e(name))
        )
        tafeln.append(
            '<div data-schritt data-aktiv="%s" class="wechsel__tafel">'
            '<div class="raster raster--2" style="align-items:center;gap:clamp(32px,5vw,64px)">'
            "<div>%s</div>"
            "<div>"
            '<p class="vorzeile">Schritt %02d · %s</p>'
            '<h3 style="font-size:clamp(24px,2.8vw,34px)">%s</h3>'
            '<p class="fuehrung mt-4">%s</p>'
            '<div class="hinweiskasten mt-5"><p><strong>Was das bringt:</strong> %s</p></div>'
            "</div></div></div>"
            % ("ja" if i == 0 else "nein", B.screenshot_block(bild), i + 1, e(name),
               e(titel), e(text), e(nutzen))
        )

    tourblock = (
        '<div data-tour data-tour-ende="/kontakt/?anliegen=demo">'
        '<div style="display:flex;align-items:center;gap:var(--r5);flex-wrap:wrap;'
        'margin-bottom:var(--r6)">'
        '<span class="demo__zaehler" data-tour-zaehler>01 / 05</span>'
        '<div class="tour-balken"><div data-tour-balken style="width:20%%"></div></div>'
        "</div>"
        '<div class="tour-schritte mb-7" role="tablist" '
        'aria-label="Schritte der Tour">%s</div>'
        '<div style="position:relative">%s</div>'
        '<div class="knopfreihe mt-7">'
        '<button class="knopf knopf--zweit" type="button" data-tour-zurueck>Zurück</button>'
        '<button class="knopf knopf--primaer" type="button" data-tour-weiter>Weiter</button>'
        "</div></div>"
        % ("".join(punkte), "".join(tafeln))
    )

    inhalt = [
        B.seitenkopf(
            "Produkt-Tour", "Ein Rundgang in fünf Schritten.",
            "Der gleiche Stoff wie in der Produktdemo, nur der Reihe nach erzählt: "
            "vom Morgen im Dashboard bis zur fertigen Website.",
            knoepfe=B.knopf("Lieber selbst klicken?", "/demo/", "zweit", "play",
                            "product_demo_start"),
            kompakt=True,
        ),
        B.abschnitt(tourblock + '<div class="mt-7">%s</div>' % HINWEIS_DEMO,
                    art="beige abschnitt--eng"),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            "<h2>Lieber selbst klicken?</h2>"
            '<p class="fuehrung mt-5">Die Produktdemo zeigt zehn Bereiche, '
            "in beliebiger Reihenfolge.</p>"
            '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div></div>'
            % (B.knopf("Zur Produktdemo", "/demo/", "primaer", "play",
                       "product_demo_start"),
               B.knopf("Beispiel-Website", "/demo/beispiel-website/", "zweit", "eye",
                       "demo_website_open")),
        ),
        B.schluss_cta(),
    ]

    return {
        "pfad": "/demo/produkt-tour/",
        "titel": "Produkt-Tour",
        "beschreibung": ("Geführter Rundgang durch GolfProCMS in fünf Schritten: "
                         "Dashboard, Website-Baukasten, Buchungen, Kundenakte und das "
                         "fertige Ergebnis."),
        "krumen": [("/", "Start"), ("/demo/", "Demo"),
                   ("/demo/produkt-tour/", "Produkt-Tour")],
        "inhalt": "".join(inhalt),
    }


# --------------------------------------------- /demo/beispiel-website/ --

def beispiel():
    seiten_liste = [
        ("pub-site-start-full", "Startseite",
         "Titelbereich, Leistungen, Stimmen, Buchungskalender und Kontakt – aus "
         "elf Bausteinen zusammengesetzt."),
        ("pub-site-ueber-mich-full", "Über mich",
         "Eine Unterseite aus denselben Bausteinen, mit anderer Reihenfolge."),
        ("pub-site-preise-full", "Preise",
         "Leistungen und Pakete mit Preisen – gepflegt im CMS, nicht im Text."),
        ("pub-site-landing", "Landingpage",
         "Eine eigene Seite für einen einzelnen Kurs, ohne Navigation."),
    ]
    karten = "".join(
        '<div>%s</div>' % B.screenshot_block(b, etikett=None) for b, _n, _z in seiten_liste
    )

    inhalt = [
        B.seitenkopf(
            "Beispiel-Website", "So könnte deine Website aussehen.",
            "Diese Website hat GolfProCMS selbst erzeugt – aus dem Demo-Bestand, den "
            "der Installer anlegt. Golf Academy Bergmann ist ein erfundener Betrieb; "
            "die Seiten sind echt gerendert.",
            knoepfe=B.knopf("Wie der Baukasten funktioniert", "/funktionen/website/",
                            "primaer", "website")
                    + B.knopf("Eigene Demo anfragen", "/kontakt/?anliegen=demo", "zweit",
                              "mail", "trial_click"),
        ),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            '<p class="vorzeile" style="justify-content:center">'
            "Desktop · Tablet · Smartphone</p>"
            "<h2>Auf jedem Bildschirm.</h2>"
            '<p class="fuehrung mt-5">Wechsle die Ansicht – die Aufnahmen entstanden '
            "in genau diesen Breiten, nicht am Schieberegler.</p></div>"
            + '<p class="bildunter" style="justify-content:center;margin:0 0 var(--r5)"><span class="marke-etikett marke-etikett--grau">Bildflächen</span><span>Die schraffierten Flächen sind Platzhalter – so zeigt der Baukasten eine Bildfläche, solange kein Foto hochgeladen ist. Dort stehen später deine eigenen Aufnahmen.</span></p>'
            + B.geraete({
                "desktop": "pub-site-start-full",
                "tablet": "pub-site-start-tablet",
                "mobile": "pub-site-start-mobile",
            }, gruppe="beispiel_geraete")
            + '<div class="mt-7" style="max-width:760px;margin-inline:auto">%s</div>'
              % ('<div class="hinweiskasten hinweiskasten--sand">'
                 "<h4>Beispieldaten</h4><p>„Golf Academy Bergmann“, „Daniel Bergmann“ "
                 "und alle Namen auf diesen Seiten sind erfunden. Sie stammen aus dem "
                 "Demo-Bestand, den GolfProCMS bei der Einrichtung auf Wunsch selbst "
                 "anlegt: ein zweiter, vollständig getrennter Bereich, in dem sich "
                 "alles ausprobieren lässt, ohne eigene Daten anzufassen. Auch die "
                 "Preise stammen von dort, damit Text und System zusammenpassen.</p>"
                 "</div>"),
            art="beige",
        ),
        B.abschnitt(
            B.kopfblock("Die Seiten", "Vier Seiten, ein Baukasten.",
                        "Jede dieser Seiten ist aus denselben Bausteinen gebaut. Was "
                        "sie unterscheidet, ist die Reihenfolge und der Inhalt.")
            + '<div class="raster raster--2">%s</div>' % karten,
            art="weiss",
        ),
        # Was auf so einer Seite tatsaechlich steht – Leistungen und Preise
        # aus dem Demo-Bestand, damit Text und System zusammenpassen.
        '<section class="abschnitt abschnitt--eng zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<p class="vorzeile">Die Inhalte</p>'
        '<h2 style="font-size:clamp(28px,3.4vw,44px);max-width:13ch">'
        "Was so eine Seite trägt.</h2>"
        '<p class="fuehrung" style="margin-top:var(--r5)">Leistungen und Preise '
        "kommen aus dem CMS, nicht aus dem Fließtext. Änderst du einen Preis "
        "im Bereich Buchungen, steht er hier sofort richtig.</p></div>"
        "<div>%s</div></div></div></section>"
        % B.typoliste([
            ("Einzeltraining 60 Minuten", "89 € · Eine Stunde nur für dich."),
            ("Gruppentraining 90 Minuten", "39 € · Höchstens sechs Teilnehmer."),
            ("Platzreifekurs", "349 € · Acht Einheiten bis zur Prüfung."),
            ("Videoanalyse 60 Minuten", "119 € · Schwung Bild für Bild."),
            ("Platztraining 9 Löcher", "149 € · Entscheidungen auf der Runde."),
            ("Golf Starter 5", "399 € · Fünf Einzelstunden als Paket."),
        ]),

        B.abschnitt(
            B.kopfblock("Die Haltung dahinter", "Warum das nicht nach Portal aussieht.",
                        "", mitte=True)
            + '<div class="fliess mitte" style="margin-inline:auto">'
              '<p class="fuehrung" style="margin-inline:auto">Der Renderer setzt bewusst '
              "keine Kachelraster, sondern eine redaktionelle Ordnung: eine Titelzeile "
              "über dem Bild, Listen mit Haarlinien, versetzte Zitate, ein "
              "handschriftlicher Einwurf dort, wo eine Person spricht.</p>"
              '<p class="hand mt-6" style="font-size:2em">Kunden buchen Unterricht bei '
              "einem Menschen.</p>"
              '<p class="fuehrung mt-5" style="margin-inline:auto">Zwölf gleiche Kacheln '
              "erzählen das Gegenteil.</p></div>",
        ),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            "<h2>So könnte deine Website aussehen.</h2>"
            '<p class="fuehrung mt-5">Schreib kurz, was du anbietest und wo du '
            "unterrichtest – dann richten wir eine Demo mit deinen Angaben ein, damit "
            "du es nicht am fremden Beispiel beurteilen musst.</p>"
            '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div></div>'
            % (B.knopf("Meine Demo anfragen", "/kontakt/?anliegen=demo", "hell", "mail",
                       "personal_demo_click"),
               B.knopf("Erst die Produktdemo", "/demo/", "rand-hell")),
            art="dunkel",
        ),
    ]

    return {
        "pfad": "/demo/beispiel-website/",
        "titel": "Beispiel-Website eines Golfpros",
        "beschreibung": ("Eine vollständige Golfpro-Website, erzeugt vom "
                         "Website-Baukasten in GolfProCMS – auf Desktop, Tablet und "
                         "Smartphone."),
        "og_text": "So könnte deine eigene Golfpro-Website aussehen.",
        "krumen": [("/", "Start"), ("/demo/", "Demo"),
                   ("/demo/beispiel-website/", "Beispiel-Website")],
        "inhalt": "".join(inhalt),
    }


# --------------------------------------------------- /demo/screenshots/ --

def screenshots():
    bereiche = [
        ("alle", "Alle"),
        ("dashboard", "Dashboard"),
        ("website", "Website"),
        ("buchungen", "Buchungen"),
        ("kunden", "Kunden"),
        ("kurse", "Kurse"),
        ("training", "Training"),
        ("verkauf", "Verkauf"),
        ("wachstum", "Marketing"),
        ("auswertung", "Auswertung"),
        ("inhalte", "Inhalte"),
        ("system", "System"),
        ("kundensicht", "Kundensicht"),
    ]
    filter_knoepfe = "".join(
        '<button type="button" data-filter="%s" aria-pressed="%s">%s</button>'
        % (e(k), "true" if k == "alle" else "false", e(n)) for k, n in bereiche
    )

    stuecke = []
    for schluessel, (name, bereich, zeile) in D.BILDER.items():
        if not bereich:
            continue
        stuecke.append(
            '<button class="galerie__stueck" type="button" data-bereich="%s" '
            'data-lupe="%s">'
            '<span class="galerie__bild">'
            '<img src="/assets/img/shots/%s-sm.webp" data-gross="/assets/img/shots/%s.webp" '
            'alt="%s: %s" loading="lazy" decoding="async"></span>'
            '<span><span class="galerie__name">%s %s</span>'
            '<span class="galerie__zeile">%s</span></span></button>'
            % (e(bereich), e("%s – %s" % (name, zeile)), e(schluessel), e(schluessel),
               e(name), e(zeile), e(name), icon("zoom", 14), e(zeile))
        )

    inhalt = [
        B.seitenkopf(
            "Screenshots", "Sieh dir GolfProCMS genauer an.",
            "%d Aufnahmen aus einer laufenden Installation. Nichts nachgestellt, "
            "nichts hübsch gerechnet – so sieht das System aus."
            % len(stuecke),
            knoepfe=B.knopf("Zur Produktdemo", "/demo/", "zweit", "play",
                            "product_demo_start"),
            kompakt=True,
        ),
        B.abschnitt(
            '<div class="filter" role="group" aria-label="Nach Bereich filtern">%s</div>'
            '<div class="galerie" data-galerie>%s</div>' % (filter_knoepfe, "".join(stuecke))
            + '<div class="mt-8">%s</div>' % HINWEIS_DEMO,
            art="beige abschnitt--eng",
        ),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            "<h2>Wie funktioniert das?</h2>"
            '<p class="fuehrung mt-5">Die Produktdemo erklärt zu jedem Bereich, was '
            "du siehst und was du tun kannst.</p>"
            '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div></div>'
            % (B.knopf("Zur Produktdemo", "/demo/", "primaer", "play",
                       "product_demo_start"),
               B.knopf("Alle Funktionen", "/funktionen/", "zweit")),
        ),
        B.lupe(),
    ]

    return {
        "pfad": "/demo/screenshots/",
        "titel": "Screenshots",
        "beschreibung": ("Alle Bereiche von GolfProCMS als Screenshots: Dashboard, "
                         "Website-Baukasten, Buchungen, Kunden, Kurse, Rechnungen, "
                         "Auswertung und die öffentliche Website."),
        "krumen": [("/", "Start"), ("/demo/", "Demo"),
                   ("/demo/screenshots/", "Screenshots")],
        "inhalt": "".join(inhalt),
    }


# ------------------------------------------------------ /demo/golfpro/ --
# Reduzierte Seite fuer Links aus LinkedIn: ein Bildschirm, eine Aussage,
# ein Knopf. Kein Menue-Band, kein klebender Hinweis.

def linkedin():
    inhalt = [
        '<section class="hero"><div class="huelle huelle--weit">'
        '<div class="hero__raster"><div>'
        '<p class="vorzeile">Für Golfpros</p>'
        "<h1>Vielleicht suchst du <mark>genau das.</mark></h1>"
        '<p class="hero__fuehrung">Eine Anwendung für den digitalen Teil deiner '
        "Golfschule: Website selbst pflegen, Termine online buchen lassen, Kunden und "
        "Pakete im Blick. Kein Baukasten für alle Branchen – zugeschnitten auf das, "
        "was bei einem Golfpro anfällt.</p>"
        '<div class="knopfreihe">%s%s</div>'
        '<p class="hero__fuss">Zwei Minuten reichen für den ersten Eindruck.</p>'
        "</div>"
        '<div class="hero__visual">%s</div></div></div></section>'
        % (B.knopf("Schau es dir an", "/demo/", "primaer", "play", "linkedin_demo_click"),
           B.knopf("So sieht die Website aus", "/demo/beispiel-website/", "zweit"),
           B.rahmen("app-dashboard", lazy=False)),

        '<section class="abschnitt abschnitt--eng abschnitt--beige zeigen">'
        '<div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<p class="vorzeile">In Kürze</p>'
        '<h2 style="font-size:clamp(28px,3.4vw,44px);max-width:12ch">'
        "Drei Dinge, die es kann.</h2></div>"
        "<div>%s</div></div></div></section>"
        % B.typoliste([
            ('<a href="/funktionen/website/">Website selbst pflegen</a>',
             "Seiten aus Bausteinen, Vorschau für Telefon und Desktop. "
             "Eine Preisänderung dauert Minuten."),
            ('<a href="/funktionen/buchungen/">Online buchen lassen</a>',
             "Du gibst Zeiten frei, dein Kunde bucht selbst – mit Konto oder ohne."),
            ('<a href="/produkt/">Kunden und Pakete</a>',
             "Akte mit Historie, Zehnerkarten mit gezählten Einheiten, "
             "Rechnungen ohne Nummernlücken."),
        ]),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            "<h2>Und so sieht die Website aus, die dabei herauskommt.</h2></div>"
            + B.geraete({
                "desktop": "pub-site-start-full",
                "tablet": "pub-site-start-tablet",
                "mobile": "pub-site-start-mobile",
            }, gruppe="linkedin_geraete")
            + '<div class="knopfreihe knopfreihe--mitte mt-7">%s</div>'
              % B.knopf("Produktdemo öffnen", "/demo/", "primaer", "play",
                        "linkedin_demo_click"),
        ),
        B.schluss_cta(
            titel="Kurz reinsehen?",
            text="Die Demo braucht keine Anmeldung. Wenn es nicht passt, hast du "
                 "zwei Minuten verloren.",
        ),
    ]

    return {
        "pfad": "/demo/golfpro/",
        "titel": "GolfProCMS für Golfpros",
        "beschreibung": ("Website, Online-Buchung und Kundenverwaltung für Golf "
                         "Professionals – in zwei Minuten angesehen."),
        "band": False,
        "sticky": False,
        "noindex": True,
        "inhalt": "".join(inhalt),
    }
