# -*- coding: utf-8 -*-
"""Produktübersicht und Funktionsseiten."""

import daten as D
from icons import icon
from layout import e
import bausteine as B


# ------------------------------------------------------------- /produkt/ --

def _modulzeile(m, links):
    """Ein Modul als breiter Abschnitt: Aufnahme und Erklärung nebeneinander."""
    sehen = "".join("<li>%s</li>" % e(x) for x in m["sehen"])
    tun = "".join("<li>%s</li>" % e(x) for x in m["tun"])
    text = (
        '<p class="vorzeile">%s</p>'
        "<h3 style=\"font-size:clamp(26px,3vw,36px)\">%s</h3>"
        '<p class="fuehrung mt-4">%s</p>'
        '<div class="raster raster--2 mt-6" style="gap:var(--r5)">'
        "<div><h4 style=\"margin-bottom:8px\">Was du siehst</h4>"
        '<ul style="font-size:15px;color:var(--tinte-2)">%s</ul></div>'
        "<div><h4 style=\"margin-bottom:8px\">Was du tun kannst</h4>"
        '<ul style="font-size:15px;color:var(--tinte-2)">%s</ul></div></div>'
        '<div class="hinweiskasten mt-6"><p><strong>Warum das hilft:</strong> %s</p></div>'
        '<div class="knopfreihe mt-6">%s%s</div>'
        % (e(D.GRUPPEN.get(m["gruppe"], "") or "Kern"), e(m["name"]), e(m["kurz"]),
           sehen, tun, e(m["nutzen"]),
           B.knopf("In der Demo ansehen", "/demo/#" + m["key"], "zweit", "play"),
           (B.knopf("Detailseite", m["seite"], "primaer") if m.get("seite") else ""))
    )
    bild = B.screenshot_block(m["bild"]) if m.get("bild") else ""
    if links:
        inhalt = "<div>%s</div><div>%s</div>" % (text, bild)
    else:
        inhalt = "<div>%s</div><div>%s</div>" % (bild, text)
    return ('<div class="raster raster--2" style="align-items:center;gap:clamp(32px,5vw,72px)">%s</div>'
            % inhalt)


def produkt():
    kern = ["dashboard", "website", "bookings", "customers"]
    abschnitte = []
    for i, key in enumerate(kern):
        m = D.MODULE_NACH_KEY[key]
        abschnitte.append(B.abschnitt(
            _modulzeile(m, links=(i % 2 == 0)),
            art="weiss" if i % 2 else "",
        ))

    inhalt = [
        B.seitenkopf(
            "Produktübersicht", "GolfProCMS im Überblick",
            "Eine Anwendung für den digitalen Teil deines Golfbusiness. "
            "Sechs Bereiche sind immer da, sechzehn weitere schaltest du ein, "
            "wenn du sie brauchst.",
            knoepfe=B.knopf("Produktdemo starten", "/demo/", "primaer", "play",
                            "product_demo_start")
                    + B.knopf("Alle Funktionen", "/funktionen/", "zweit"),
            visual=B.screenshot_block("app-dashboard", lazy=False),
        ),
        B.abschnitt(
            B.kopfblock("Der Zuschnitt", "Einfach im Standard, mehr auf Wunsch.",
                        "Das ist die wichtigste Entscheidung im Produkt – und sie "
                        "steht im Code: Sechs Bereiche sind Kern und immer sichtbar. "
                        "Alles Weitere ist ein Modul, das du einschaltest. Ein "
                        "Einsteiger sieht neun Menüpunkte, keine zweiundzwanzig.")
            + '<div class="raster raster--2" style="align-items:center;gap:clamp(32px,5vw,64px)">'
              "<div>%s</div>"
              "<div>%s</div></div>"
              % (B.screenshot_block("app-tarif"),
                 "".join([
                     '<p class="hand mb-5">Ausgeschaltet heißt nicht gelöscht.</p>',
                     "<p>Schaltest du einen Bereich ab, verschwindet er aus dem Menü – "
                     "die Daten bleiben vollständig erhalten. Schaltest du ihn wieder "
                     "ein, ist alles da, wo es war.</p>",
                     "<p>Das ist der Unterschied zwischen einem Produkt, das mitwächst, "
                     "und einem, bei dem man sich zu Beginn festlegen muss.</p>",
                     '<div class="knopfreihe mt-6">%s</div>'
                     % B.knopf("Alle 22 Bereiche ansehen", "/funktionen/", "zweit"),
                 ])),
            art="beige",
        ),
    ]
    inhalt += abschnitte
    inhalt += [
        B.abschnitt(
            B.kopfblock("Unter der Oberfläche", "Entscheidungen, die man erst später merkt.",
                        "Vier Dinge, die im Alltag den Unterschied machen – und die "
                        "man beim ersten Ansehen nicht sieht.", mitte=True)
            + B.raster([
                B.karte("Belege sind Dokumente, keine Ansichten",
                        "Eine Rechnungsposition führt Titel, Preis und Steuersatz als "
                        "eigene Werte. Änderst du später den Preis der Leistung, bleibt "
                        "die Rechnung, wie sie war. Rechnungsnummern haben keine Lücken; "
                        "korrigiert wird mit einer Gutschrift.", "invoices"),
                B.karte("Geld ist immer eine Ganzzahl",
                        "399,00 € sind intern 39900 Cent. Gerundet wird an genau einer "
                        "Stelle, und Beträge werden so aufgeteilt, dass die Summe der "
                        "Teile den Gesamtbetrag ergibt – auf den Cent.", "euro"),
                B.karte("Die KI entscheidet nichts",
                        "Sie schlägt vor, fasst zusammen und beantwortet Fragen zu deinen "
                        "Zahlen. Preisänderungen, Kundendaten, Rechnungen und Versand "
                        "laufen immer über eine ausdrückliche Bestätigung.", "ai"),
                B.karte("Zählen ohne Cookies",
                        "Die Websitestatistik bildet aus IP-Adresse und einem täglich "
                        "wechselnden Zufallswert eine Prüfsumme. Wiederkehrende Besuche "
                        "eines Tages sind erkennbar, eine Person nicht. Die IP wird "
                        "nirgends gespeichert.", "shield"),
            ], 2),
            art="weiss",
        ),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            "<h2>Nicht nur darüber lesen – selbst ausprobieren.</h2>"
            '<p class="fuehrung mt-5">Die Demo zeigt jeden Bereich mit echten '
            "Aufnahmen aus einer laufenden Installation.</p>"
            '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div></div>'
            % (B.knopf("Demo starten", "/demo/", "primaer", "play", "product_demo_start"),
               B.knopf("Geführte Tour", "/demo/produkt-tour/", "zweit", "route",
                       "product_tour_start")),
            art="beige",
        ),
        B.schluss_cta(),
    ]

    return {
        "pfad": "/produkt/",
        "titel": "GolfProCMS im Überblick",
        "beschreibung": ("Website-Baukasten, Online-Buchung, Kundenakte und Dashboard: "
                         "die Bereiche von GolfProCMS mit echten Aufnahmen aus dem "
                         "laufenden System."),
        "krumen": [("/", "Start"), ("/produkt/", "Produkt")],
        "inhalt": "".join(inhalt),
    }


# ---------------------------------------------------------- /funktionen/ --

def funktionen():
    gruppen_reihenfolge = ["", "kunden", "training", "verkauf", "web", "wachstum",
                           "wissen", "system"]
    bloecke = []
    for g in gruppen_reihenfolge:
        module = [m for m in D.MODULE if m["gruppe"] == g]
        if not module:
            continue
        karten = []
        for m in module:
            etikett = "Kern" if m["kern"] else None
            karten.append(B.karte(
                m["name"], e(m["kurz"]), m["icon"],
                url=m.get("seite") or "/demo/#" + m["key"],
                link_text="Detailseite" if m.get("seite") else "In der Demo ansehen",
                etikett=etikett,
            ))
        titel = D.GRUPPEN.get(g) or "Immer dabei"
        bloecke.append(
            '<div class="mt-8" id="gruppe-%s"><h3 class="mb-5">%s</h3>%s</div>'
            % (e(g or "kern"), e(titel), B.raster(karten, 3))
        )

    tabelle = B.tabelle(
        ["Bereich", "Ab Stufe", "Immer sichtbar", "Im CMS belegt durch"],
        [[e(m["name"]),
          e(dict(starter="Starter", pro="Pro", business="Business",
                 academy="Academy")[m["plan"]]),
          '<span class="ja">ja</span>' if m["kern"] else "–",
          '<code style="font-size:12.5px;color:var(--tinte-3)">%s</code>' % e(m["beleg"])]
         for m in D.MODULE]
    )

    inhalt = [
        B.seitenkopf(
            "Funktionen", "Was kann GolfProCMS?",
            "Zweiundzwanzig Bereiche, sechs davon immer sichtbar. Jeder Eintrag hier "
            "entspricht einem Bereich, den es im System tatsächlich gibt – die letzte "
            "Spalte der Tabelle weiter unten nennt die Datei dazu.",
            knoepfe=B.knopf("In der Demo ansehen", "/demo/", "primaer", "play",
                            "product_demo_start"),
        ),
        B.abschnitt("".join(bloecke), art="beige"),
        B.abschnitt(
            B.kopfblock("Nachweis", "Woher diese Liste kommt.",
                        "Kein Marketingversprechen, sondern ein Abgleich: Jeder Bereich "
                        "steht im Produkt in <code>lib/Module.php</code>, jede Aufnahme "
                        "auf dieser Website stammt aus einer laufenden Installation.")
            + tabelle
            + '<p class="mt-5" style="font-size:14px;color:var(--tinte-3)">'
              "Die Stufe legt fest, was einschaltbar <em>ist</em>. Was im Menü "
              "tatsächlich erscheint, entscheidet jeder selbst.</p>",
            art="weiss",
        ),
        B.schluss_cta(),
    ]

    return {
        "pfad": "/funktionen/",
        "titel": "Alle Funktionen",
        "beschreibung": ("Alle 22 Bereiche von GolfProCMS im Überblick: Website, "
                         "Buchungen, Kunden, Kurse, Rechnungen, Auswertung und mehr – "
                         "mit Nachweis, wo sie im System stehen."),
        "krumen": [("/", "Start"), ("/produkt/", "Produkt"), ("/funktionen/", "Funktionen")],
        "inhalt": "".join(inhalt),
    }


# --------------------------------------------------- Einzelne Funktionen --

def _detailseite(key, titel, vorzeile, fuehrung, bilder, ablauf_schritte,
                 zusatz="", faq_paare=None, beschreibung=""):
    m = D.MODULE_NACH_KEY[key]
    sehen = "".join("<li>%s</li>" % e(x) for x in m["sehen"])
    tun = "".join("<li>%s</li>" % e(x) for x in m["tun"])

    inhalt = [
        B.seitenkopf(vorzeile, titel, fuehrung,
                     knoepfe=B.knopf("In der Demo ansehen", "/demo/#" + key, "primaer",
                                     "play", "feature_demo_click")
                             + B.knopf("Alle Funktionen", "/funktionen/", "zweit")),
        B.abschnitt(B.screenshot_block(bilder[0], lazy=False), art="beige"),
        B.abschnitt(
            '<div class="raster raster--3">'
            '<div><h3 class="mb-4">Was du siehst</h3>'
            '<ul style="color:var(--tinte-2)">%s</ul></div>'
            '<div><h3 class="mb-4">Was du tun kannst</h3>'
            '<ul style="color:var(--tinte-2)">%s</ul></div>'
            '<div><h3 class="mb-4">Warum es nützt</h3><p style="color:var(--tinte-2)">%s</p></div>'
            "</div>" % (sehen, tun, e(m["nutzen"])),
        ),
    ]

    if len(bilder) > 1:
        weitere = "".join(
            '<div>%s</div>' % B.screenshot_block(b) for b in bilder[1:]
        )
        inhalt.append(B.abschnitt(
            B.kopfblock("Mehr davon", "Weitere Ansichten.", "")
            + '<div class="raster raster--%d">%s</div>' % (min(len(bilder) - 1, 2), weitere),
            art="weiss",
        ))

    if ablauf_schritte:
        inhalt.append(B.abschnitt(
            B.kopfblock("Ein Ablauf", "So geht es der Reihe nach.", "")
            + B.ablauf(ablauf_schritte),
            art="beige",
        ))

    if zusatz:
        inhalt.append(zusatz)

    if faq_paare:
        inhalt.append(B.abschnitt(
            B.kopfblock("Fragen", "Dazu häufig gefragt.", "") + B.faq(faq_paare),
            art="weiss",
        ))

    inhalt.append(B.schluss_cta(
        titel="Sieh dir das im laufenden System an.",
        text="Die Produktdemo zeigt jeden Bereich mit echten Aufnahmen.",
    ))

    return {
        "pfad": m.get("seite"),
        "titel": titel,
        "beschreibung": beschreibung,
        "krumen": [("/", "Start"), ("/produkt/", "Produkt"),
                   ("/funktionen/", "Funktionen"), (m.get("seite"), m["name"])],
        "inhalt": "".join(inhalt),
    }


def dashboard():
    return _detailseite(
        "dashboard", "Alles Wichtige auf einen Blick.", "Dashboard",
        "Der erste Bildschirm nach dem Anmelden. Er beantwortet eine einzige Frage: "
        "Was muss ich heute wissen?",
        ["app-dashboard", "app-dashboard-mobile", "app-auswertung"],
        [("Öffnen", "Umsatz, Auslastung und die nächsten Termine stehen oben."),
         ("Lesen", "Darunter: Hinweise, die aus deinen eigenen Zahlen berechnet sind."),
         ("Springen", "Jeder Hinweis führt direkt in den Bereich, der ihn ausgelöst hat."),
         ("Erledigen", "Termin anlegen, Rechnung öffnen, Anfrage beantworten.")],
        beschreibung=("Das Dashboard von GolfProCMS: Umsatz, Auslastung, die nächsten "
                      "Termine und Empfehlungen aus den eigenen Daten."),
        faq_paare=[
            ("Woher kommen die „empfohlenen Aktionen“?",
             "<p>Sie werden aus dem eigenen Datenbestand berechnet – offene Anfragen, "
              "überfällige Rechnungen, Pakete, die bald auslaufen, Kunden ohne Termin "
              "seit über 60 Tagen. Es ist keine Vorhersage, sondern eine Auswertung "
              "dessen, was da ist.</p>"),
            ("Sieht ein Trainer dieselben Zahlen wie ich?",
             "<p>Nein. GolfProCMS kennt vier Rollen – Inhaber, Head Pro, Trainer und "
              "Assistenz. Ein Trainer sieht seine eigenen Termine; Umsatzzahlen des "
              "Betriebs bleiben dem Inhaber vorbehalten.</p>"),
        ],
    )


def website():
    zusatz = B.abschnitt(
        '<div class="kopfblock kopfblock--mitte">'
        '<p class="vorzeile" style="justify-content:center">Desktop, Tablet, Telefon</p>'
        "<h2>Eine Website, drei Bildschirmgrößen.</h2>"
        '<p class="fuehrung mt-5">Der Baukasten hat eine Vorschau für jede Größe. '
        "Die Aufnahmen hier sind in genau diesen Breiten entstanden.</p></div>"
        + B.geraete({
            "desktop": "pub-site-ueber-mich-full",
            "tablet": "pub-site-ueber-mich-tablet",
            "mobile": "pub-site-ueber-mich-mobile",
        }, gruppe="website_geraete"),
        art="beige",
    )
    return _detailseite(
        "website", "Deine Website. Dein Auftritt.", "Website",
        "Seiten entstehen aus Bausteinen: Titelbereich, Leistungen, Preise, Häufige "
        "Fragen, Buchungskalender, Kontakt. Du sortierst sie per Griff, änderst Texte "
        "und siehst sofort, wie es aussieht.",
        ["app-baukasten", "app-website", "app-design"],
        [("Baustein wählen", "Aus 25 Typen – vom Titelbereich bis zum Buchungskalender."),
         ("Inhalt ändern", "Überschrift, Text, Bild. Direkt an der Stelle, an der es steht."),
         ("Vorschau prüfen", "Desktop, Tablet und Telefon, ohne die Seite zu verlassen."),
         ("Veröffentlichen", "Oder als Entwurf liegen lassen, bis es passt.")],
        zusatz=zusatz,
        beschreibung=("Der Website-Baukasten von GolfProCMS: Seiten aus Bausteinen, "
                      "Vorschau für Desktop, Tablet und Telefon, eigene Domain."),
        faq_paare=[
            ("Wie sieht das Ergebnis aus?",
             "<p>Der Renderer setzt bewusst keine Kachelraster, sondern eine "
              "redaktionelle Ordnung: eine Titelzeile über dem Bild, Listen mit "
              "Haarlinien, versetzte Zitate. Kunden buchen Unterricht bei einem "
              "Menschen – zwölf gleiche Kacheln erzählen das Gegenteil. "
              "<a href='/demo/beispiel-website/'>Sieh dir die Beispiel-Website an</a>.</p>"),
            ("Kann ich Farbe und Schrift ändern?",
             "<p>Ja. Markenfarbe, Akzent, Schrift und Rundung stellst du im Bereich "
              "Design ein. Die Rundung ist ein Regler von 0 bis 28 – von strengen "
              "Kanten bis zu weichen Flächen.</p>"),
            ("Werden Schriften von Google geladen?",
             "<p>In der Standardeinstellung nicht. Archivo und Caveat liegen als "
              "Dateien auf deinem Server. Grund ist das Urteil des Landgerichts "
              "München I vom 20.01.2022 (Az. 3 O 17493/20) zu Google Fonts. Wählst du "
              "eine andere Schrift, weist der Datenschutzbereich darauf hin.</p>"),
            ("Kann ich Suchmaschinen-Angaben je Seite setzen?",
             "<p>Ja, Seitentitel und Beschreibung mit Zeichenzähler, dazu die "
              "Entscheidung, ob eine Seite indexiert werden soll.</p>"),
        ],
    )


def kurse():
    return _detailseite(
        "courses", "Deine Kurse übersichtlich verwalten.", "Kurse & Training",
        "Online-Kurse mit Modulen, Lektionen, Quiz und Zertifikat – und daneben "
        "Trainingspläne für die Arbeit zwischen zwei Stunden.",
        ["app-kurs-detail", "app-kurse", "app-trainingsplan"],
        [("Kurs anlegen", "Titel, Beschreibung, Preis."),
         ("Module und Lektionen", "Als Text oder Video, in der Reihenfolge, die du willst."),
         ("Freigeben", "Verkaufen oder einem Kunden direkt zuweisen."),
         ("Fortschritt sehen", "Wer wie weit ist, und wie die Quizfragen ausgingen.")],
        zusatz=B.abschnitt(
            B.kopfblock("Daneben", "Trainingspläne und Übungsbibliothek.",
                        "Ein Kurs ist Theorie zum Selbstlernen. Ein Trainingsplan ist "
                        "das, was dein Schüler bis zur nächsten Stunde üben soll – mit "
                        "Wochen, Einheiten und Übungen aus deiner eigenen Bibliothek.")
            + '<div class="raster raster--2">%s%s</div>'
              % (B.screenshot_block("app-training"), B.screenshot_block("app-uebungen")),
            art="weiss",
        ),
        beschreibung=("Kursverwaltung in GolfProCMS: Module, Lektionen, Quiz, Zertifikat "
                      "und Trainingspläne mit eigener Übungsbibliothek."),
        faq_paare=[
            ("Was ist der Unterschied zwischen Kurs und Event?",
             "<p>Ein Kurs ist ein Online-Angebot mit Modulen und Lektionen, das jemand "
              "in seinem Tempo durchgeht. Ein Event ist ein Termin mit Plätzen – Camp, "
              "Workshop, Turnier. Beides gibt es, beides erscheint auf der Website.</p>"),
            ("Bekommen Teilnehmer ein Zertifikat?",
             "<p>Ja, das ist im Kursmodul vorgesehen.</p>"),
        ],
    )


def buchungen():
    return _detailseite(
        "bookings", "Termine und Buchungen im Blick.", "Buchungen",
        "Du legst fest, was buchbar ist und wann. Deine Kunden buchen selbst – mit "
        "Konto oder ohne. Der Termin landet in deinem Kalender.",
        ["app-buchungen", "app-verfuegbarkeit", "app-leistungen"],
        [("Leistung anlegen", "Name, Dauer, Preis, wer sie gibt."),
         ("Zeiten freigeben", "Je Leistung, je Trainer, je Standort."),
         ("Kunde bucht", "Drei Schritte: Zeit wählen, Angaben, Bestätigung."),
         ("Termin steht", "Im Kalender, mit Erinnerung für beide Seiten.")],
        zusatz=B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            '<p class="vorzeile" style="justify-content:center">Die andere Seite</p>'
            "<h2>So sieht es dein Kunde.</h2>"
            '<p class="fuehrung mt-5">Die Online-Buchung liegt auf deiner eigenen '
            "Website – als Baustein auf einer Seite, die du selbst gebaut hast. "
            "Ein Konto ist möglich, aber kein Zwang.</p></div>"
            + B.geraete({
                "desktop": "pub-buchen-full",
                "tablet": "pub-buchen-tablet",
                "mobile": "pub-buchen-mobile",
            }, gruppe="buchen_geraete")
            + '<div class="raster raster--2 mt-8">%s%s</div>'
              % (B.screenshot_block("app-pakete"), B.screenshot_block("pub-portal")),
            art="weiss",
        ),
        beschreibung=("Online-Buchung mit GolfProCMS: Verfügbarkeiten je Leistung und "
                      "Trainer, Buchung in drei Schritten, Pakete mit gezählten "
                      "Einheiten und ein Kundenportal."),
        faq_paare=[
            ("Muss mein Kunde ein Konto anlegen?",
             "<p>Nein. Die Buchung geht angemeldet oder als Gast. Wer ein Konto hat, "
              "sieht im Kundenportal seine Termine, Pakete, Rechnungen und Kurse.</p>"),
            ("Was passiert mit Zehnerkarten?",
             "<p>Pakete sind ein eigener Bereich. Eine gekaufte Zehnerkarte hat "
              "gezählte Einheiten; ein Termin verbraucht eine davon. Auf dem Dashboard "
              "steht, wessen Paket bald ausläuft.</p>"),
            ("Gibt es eine Warteliste?",
             "<p>Ja, die Warteliste ist Teil des Buchungsbereichs.</p>"),
            ("Werden Erinnerungen verschickt?",
             "<p>Ja, per E-Mail. SMS und WhatsApp sind vorgesehen, brauchen aber ein "
              "Konto bei einem Anbieter – ohne das gehen Erinnerungen per E-Mail raus.</p>"),
        ],
    )
