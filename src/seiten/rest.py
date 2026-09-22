# -*- coding: utf-8 -*-
"""Vorteile, Preise, FAQ, Über uns, Kontakt, Recht, 404."""

import daten as D
from icons import icon
from layout import e
import bausteine as B


# ------------------------------------------------------------- /vorteile/ --

def vorteile():
    faelle = [
        ("Du willst einen neuen Kurs anbieten",
         [("Kurs oder Event anlegen", "Titel, Beschreibung, Plätze, Preis."),
          ("Auf eine Seite stellen", "Baustein „Kurse“ oder „Events“ auf die Seite ziehen."),
          ("Veröffentlichen", "Die Seite geht live, der Kurs erscheint."),
          ("Anmeldungen laufen ein", "Plätze zählt das System, du siehst wer kommt.")],
         "app-kurse"),
        ("Du willst eine Information ändern",
         [("Seite öffnen", "Im Baukasten, mit Vorschau daneben."),
          ("Text ändern", "Direkt an der Stelle, an der er steht."),
          ("Vorschau prüfen", "Desktop, Tablet, Telefon."),
          ("Speichern", "Fertig. Keine Anfrage, kein Warten.")],
         "app-baukasten"),
        ("Eine Anfrage kommt über die Website",
         [("Formular wird abgeschickt", "Der Eingang landet als Lead im CMS."),
          ("Stufe setzen", "Neu, kontaktiert, Angebot, gebucht."),
          ("Nachfassen", "Das Dashboard erinnert, wenn eine Anfrage liegen bleibt."),
          ("In einen Kunden überführen", "Aus dem Lead wird eine Kundenakte.")],
         "app-leads"),
        ("Ein Paket läuft aus",
         [("Hinweis auf dem Dashboard", "„2 Trainingspakete laufen in den nächsten 30 Tagen ab.“"),
          ("Paket öffnen", "Wer betroffen ist und wie viele Einheiten offen sind."),
          ("Termin vorschlagen", "Bevor die Einheiten verfallen."),
          ("Einheit verbucht", "Der Termin zieht automatisch vom Paket ab.")],
         "app-pakete"),
    ]

    bloecke = []
    for i, (titel, schritte, bild) in enumerate(faelle):
        bloecke.append(B.abschnitt(
            '<div class="raster raster--2" style="align-items:center;gap:clamp(32px,5vw,64px)">'
            "<div>"
            '<p class="vorzeile">%s</p><h3 style="font-size:clamp(24px,2.8vw,34px)">%s</h3>'
            '<div class="mt-6">%s</div></div>'
            "<div>%s</div></div>"
            % (['Der erste Fall', 'Der zweite', 'Der dritte', 'Der vierte'][i], e(titel),
               "".join(
                   '<div style="display:flex;gap:var(--r4);padding:var(--r3) 0;'
                   'border-bottom:1px solid var(--rand)">'
                   '<span style="flex:none;width:26px;height:26px;border-radius:50%%;'
                   'background:var(--gruen-hell);color:var(--gruen);display:grid;'
                   'place-items:center;font-size:12px;font-weight:700">%d</span>'
                   '<span><b style="display:block;font-size:15.5px">%s</b>'
                   '<span style="font-size:14.5px;color:var(--tinte-3)">%s</span></span></div>'
                   % (n + 1, e(t), e(x)) for n, (t, x) in enumerate(schritte)),
               B.screenshot_block(bild)),
            art="weiss" if i % 2 else "",
        ))

    nutzen = [
        ("Einfache Verwaltung", "Weniger Zeit für technische Änderungen.",
         "Eine Preisänderung ist ein Textfeld, kein Ticket.", "edit"),
        ("Zentrale Übersicht", "Wichtige Informationen schneller finden.",
         "Kunde, Termine, Pakete und Rechnungen liegen an einer Stelle.", "layers"),
        ("Professioneller Auftritt", "Dein digitales Bild passt zu deinem Unterricht.",
         "Die Website sieht redaktionell aus, nicht nach Verwaltungsportal.", "star"),
        ("Auf dem eigenen Hosting", "Deine Daten bleiben bei dir.",
         "PHP und eine Datenbank. Keine fremde Cloud dazwischen.", "server"),
        ("Am Telefon bedienbar", "Auch zwischen zwei Stunden.",
         "Die Oberfläche ist für kleine Bildschirme gebaut.", "smartphone"),
        ("Datenschutz mitgedacht", "Weniger Sorge um Abmahnungen.",
         "Schriften im eigenen Haus, Websitestatistik ohne Cookies.", "shield"),
    ]

    inhalt = [
        B.seitenkopf(
            "Vorteile", "Für deinen Alltag als Golfpro.",
            "Keine Liste mit Eigenschaften, sondern vier Situationen aus dem "
            "Golfbetrieb – und was in TeePilot dabei tatsächlich passiert.",
            knoepfe=B.knopf("In der Demo ansehen", "/demo/", "primaer", "play",
                            "product_demo_start"),
        ),
    ]
    inhalt += bloecke
    inhalt += [
        '<section class="abschnitt abschnitt--eng abschnitt--beige zeigen">'
        '<div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px);max-width:13ch">'
        "Was bringt dir das?</h2>"
        '<p class="fuehrung" style="margin-top:var(--r5)">Jeder Punkt hier '
        "lässt sich auf eine Funktion zurückführen. Wo das nicht ginge, steht "
        "er nicht.</p></div>"
        "<div>%s</div></div></div></section>"
        % B.typoliste([
            ("Weniger Technik", "Eine Preisänderung ist ein Textfeld, kein Ticket."),
            ("Weniger Suchen", "Kunde, Termine, Pakete und Rechnungen liegen an einer Stelle."),
            ("Ein Auftritt, der passt", "Die Website sieht redaktionell aus, nicht nach Verwaltungsportal."),
            ("Daten bei dir", "PHP und eine Datenbank auf deinem Hosting. Keine fremde Cloud dazwischen."),
            ("Auch zwischen zwei Stunden", "Die Oberfläche ist für kleine Bildschirme gebaut, nicht nur verkleinert."),
            ("Weniger Sorge", "Schriften im eigenen Haus, Websitestatistik ohne Cookies."),
        ]),
        B.abschnitt(
            B.kopfblock("Ehrlich bleiben", "Warum ein spezielles CMS?",
                        "Nicht, weil allgemeine Systeme schlecht wären. Sondern weil "
                        "der Zuschnitt ein anderer ist.")
            + B.tabelle(
                ["Thema", "Allgemeiner Website-Baukasten", "TeePilot"],
                [["Zielgruppe", "Alle Branchen",
                  '<span class="ja">Golfbetriebe</span>'],
                 ["Grundgerüst", "Leere Seite, alles selbst aufbauen",
                  '<span class="ja">Geführte Einrichtung in 9 Schritten, am Ende steht eine veröffentlichte Website</span>'],
                 ["Begriffe", "Produkte, Kategorien, Bestellungen",
                  '<span class="ja">Leistungen, Pakete, Handicap, Platzreife, Trainer</span>'],
                 ["Buchung", "Meist über eine Erweiterung",
                  '<span class="ja">Eingebaut, mit Verfügbarkeiten je Trainer</span>'],
                 ["Zehnerkarten", "In der Regel nicht vorgesehen",
                  '<span class="ja">Pakete mit gezählten Einheiten</span>'],
                 ["Videoanalyse", "Nicht vorgesehen",
                  '<span class="ja">Eingebaut, mit Einzelbildschritt</span>'],
                 ["Funktionsumfang", "Sehr groß, über Erweiterungen",
                  "Zweiundzwanzig Bereiche, einzeln abschaltbar"],
                 ["Erweiterbarkeit", '<span class="ja">Sehr groß</span>',
                  "Auf den Golfbetrieb zugeschnitten"],
                 ["Verbreitung", '<span class="ja">Sehr groß, viele Dienstleister</span>',
                  "Junges Produkt"]]
            )
            + '<p class="mt-5" style="font-size:14.5px;color:var(--tinte-3);max-width:66ch">'
              "Allgemeine Website-Systeme können sehr viel. TeePilot konzentriert sich "
              "auf die Aufgaben, die im Alltag eines Golfpros vorkommen – und bringt sie "
              "fertig mit, statt sie zusammensetzen zu lassen. Wo ein allgemeines System "
              "im Vorteil ist, steht es in der Tabelle.</p>",
            art="weiss",
        ),
        B.schluss_cta(),
    ]

    return {
        "pfad": "/vorteile/",
        "titel": "Vorteile im Alltag",
        "beschreibung": ("Was sich mit TeePilot im Alltag eines Golfpros ändert: "
                         "vier Situationen mit dem tatsächlichen Ablauf im System."),
        "krumen": [("/", "Start"), ("/vorteile/", "Vorteile")],
        "inhalt": "".join(inhalt),
    }


# --------------------------------------------------------------- /preise/ --

def preise():
    inhalt = [
        B.seitenkopf(
            "Stufen und Umfang", "TeePilot kennenlernen.",
            "Vier Stufen legen fest, welche Bereiche du einschalten kannst. Was "
            "tatsächlich im Menü erscheint, entscheidest du danach selbst.",
        ),
        B.abschnitt(
            B.preiskarten()
            + '<div class="hinweiskasten hinweiskasten--sand mt-8" style="max-width:820px;margin-inline:auto">'
              "<h4>Was diese Zahlen sind – und was nicht</h4>"
              "<p>Die vier Stufen sind im Produkt hinterlegt und steuern dort den "
              "Funktionsumfang (Einstellungen → Tarif). Eine automatische Abrechnung "
              "ist im System nicht enthalten: Es gibt keinen Bezahlvorgang für "
              "TeePilot selbst und deshalb hier keinen Kaufknopf. Verbindliche "
              "Konditionen – auch für den Betrieb auf deinem eigenen Webspace – "
              "klären wir im Gespräch.</p></div>",
            art="beige",
        ),
        B.abschnitt(
            B.kopfblock("Noch unsicher?", "Noch nicht sicher, ob TeePilot zu dir passt?",
                        "Dann schau dir einfach die Demo an. Sie zeigt jeden Bereich mit "
                        "echten Aufnahmen – du musst dafür nichts angeben.", mitte=True)
            + '<div class="knopfreihe knopfreihe--mitte">%s%s</div>'
              % (B.knopf("Demo starten", "/demo/", "primaer", "play", "product_demo_start"),
                 B.knopf("Beispiel-Website ansehen", "/demo/beispiel-website/", "zweit",
                         "eye", "demo_website_open")),
        ),
        B.abschnitt(
            B.kopfblock("Was in jeder Stufe steckt", "Bereiche nach Stufe.",
                        "Die Spalte sagt, ab welcher Stufe ein Bereich einschaltbar ist. "
                        "Sechs Bereiche sind immer da.")
            + B.tabelle(
                ["Bereich", "Starter", "Pro", "Business", "Academy"],
                [[e(m["name"])]
                 + ['<span class="ja">✓</span>' if _stufe_ok(m["plan"], s) else "–"
                    for s in ("starter", "pro", "business", "academy")]
                 for m in D.MODULE],
            ),
            art="weiss",
        ),
        '<section class="abschnitt abschnitt--eng abschnitt--beige zeigen">'
        '<div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px);max-width:13ch">'
        "Was du dafür brauchst.</h2></div>"
        "<div>%s"
        '<p style="margin-top:var(--r6);font-size:14.5px;color:var(--tinte-3);'
        'max-width:56ch">Optional: <code>gd</code> oder <code>imagick</code> zum '
        "Verkleinern von Bildern, <code>curl</code> für Stripe und KI. Ohne "
        "Stripe wird auf Rechnung verkauft, ohne KI-Schlüssel schreiben die "
        "Textwerkzeuge mit einem eingebauten Generator weiter, ohne Cronjob "
        "läuft die Wartung beim Öffnen des Dashboards mit.</p>"
        "</div></div></div></section>"
        % B.typoliste([
            ("Ein gewöhnliches Hosting-Paket",
             "PHP 8.1 oder neuer, dazu <code>pdo</code>, <code>pdo_sqlite</code> "
             "oder <code>pdo_mysql</code> und <code>mbstring</code>. Kein "
             "Composer, kein Node, keine Kommandozeile, kein Docker."),
            ("Eine Datenbank – oder eine Datei",
             "SQLite ist eine einzelne Datei und braucht keine Einrichtung. "
             "MySQL geht genauso; das entscheidet ein Auswahlfeld beim "
             "Installieren."),
            ("Zwanzig Minuten",
             "Dateien hochladen, eine Adresse aufrufen, drei Felder ausfüllen. "
             "Danach führen neun Schritte bis zur veröffentlichten Website."),
        ]),
        B.schluss_cta(
            titel="Erst ansehen, dann entscheiden.",
            text="Die Demo kostet nichts und verlangt keine Anmeldung.",
        ),
    ]

    return {
        "pfad": "/preise/",
        "titel": "Stufen und Umfang",
        "beschreibung": ("Die vier Stufen von TeePilot – Starter, Pro, Business und "
                         "Academy – mit dem jeweiligen Funktionsumfang und den "
                         "technischen Voraussetzungen."),
        "krumen": [("/", "Start"), ("/preise/", "Preise")],
        "inhalt": "".join(inhalt),
    }


def _stufe_ok(noetig, stufe):
    rang = {"starter": 1, "pro": 2, "business": 3, "academy": 4}
    return rang[stufe] >= rang[noetig]


# ------------------------------------------------------------------ /faq/ --

FRAGEN = [
    ("Was ist TeePilot?",
     "<p>Eine Webanwendung für den digitalen Teil eines Golfbetriebs: Website, "
     "Online-Buchung, Kundenakte, Kurse, Trainingspläne, Verkauf, Rechnungen, "
     "Marketing und Auswertung. Sie läuft auf einem gewöhnlichen Webhosting-Paket – "
     "PHP und eine Datenbank, sonst nichts.</p>"),
    ("Für wen ist TeePilot gedacht?",
     "<p>Für selbstständige Golf Professionals, Golflehrer, Coaches und Akademien. "
     "Der Zuschnitt folgt den Aufgaben, die dort anfallen: Leistungen statt Produkte, "
     "Pakete statt Gutscheinhefte, Handicap in der Kundenakte, Verfügbarkeiten je "
     "Trainer und Standort.</p>"),
    ("Brauche ich technische Kenntnisse?",
     "<p>Zum Bedienen nicht. Seiten baust du aus fertigen Bausteinen zusammen und "
     "siehst sofort, wie es aussieht. Für die Einrichtung brauchst du einen Webspace: "
     "Dateien per FTP hochladen, <code>install.php</code> im Browser aufrufen, drei "
     "Felder ausfüllen, die Datei wieder löschen. Eine Seite namens "
     "<code>systemcheck.php</code> sagt jederzeit, was der Server kann und was "
     "fehlt.</p>"),
    ("Was kann ich mit TeePilot verwalten?",
     "<p>Zweiundzwanzig Bereiche, sechs davon immer sichtbar: Dashboard, Website, "
     "Kunden, Kalender, Buchungen und Einstellungen. Dazu einschaltbar: Leads, Pakete, "
     "Training, Videoanalyse, Kurse, Produkte, Zahlungen, Rechnungen, Inhalte, Events, "
     "Reisen, Marketing, Newsletter, Automationen, Community, Auswertung und ein "
     "KI-Assistent. Die vollständige Liste steht unter "
     "<a href='/funktionen/'>Funktionen</a>.</p>"),
    ("Kann ich meine Website selbst aktualisieren?",
     "<p>Das ist der Kern des Produkts. Der Baukasten zeigt links die Bausteine, in "
     "der Mitte die Vorschau und rechts die Einstellungen der Seite. Du sortierst per "
     "Griff um, änderst Texte an Ort und Stelle und veröffentlichst, wenn es passt – "
     "oder lässt es als Entwurf liegen.</p>"),
    ("Kann ich meine bestehenden Inhalte übernehmen?",
     "<p>Texte und Bilder kannst du in die Bausteine übertragen und Bilder in die "
     "Mediathek hochladen. Eine automatische Übernahme aus einem anderen System – "
     "etwa ein Import aus WordPress – ist im Produkt nicht enthalten. Bei überschaubaren "
     "Seitenzahlen ist die Übertragung von Hand meist schneller als jede Umwandlung; "
     "sprich uns an, wenn es um mehr geht.</p>"),
    ("Kann ich TeePilot testen?",
     "<p>Die <a href='/demo/'>Produktdemo</a> auf dieser Website zeigt alle Bereiche "
     "mit echten Aufnahmen, ohne Anmeldung. Für einen eigenen Zugang schreib uns über "
     "das <a href='/kontakt/'>Kontaktformular</a> – dann richten wir einen Bereich mit "
     "Demo-Bestand ein.</p>"),
    ("Gibt es eine Demo mit Daten?",
     "<p>Ja. Der Installer legt auf Wunsch einen zweiten, vollständig getrennten "
     "Bereich an: 40 Kunden, über tausend Termine, Rechnungen, Trainingspläne, "
     "Videoanalysen, Kurse, Kampagnen und eine fertige Website. Die Zahlen passen "
     "zueinander – die Paketeinheiten sind von echten Terminen verbraucht, der Umsatz "
     "entspricht den Preisen. Gut, um alles auszuprobieren, ohne die eigenen Daten "
     "anzufassen.</p>"),
    ("Kann ich meine eigene Domain verwenden?",
     "<p>Ja. Das System erkennt die aufgerufene Domain und liefert die dazugehörige "
     "Website aus. Läuft nur ein Betrieb auf der Installation, geht es auch ohne "
     "jede Zuordnung.</p>"),
    ("Was kostet TeePilot?",
     "<p>Im Produkt sind vier Stufen hinterlegt – Starter, Pro, Business und Academy – "
     "die dort den Funktionsumfang steuern. Ein Bezahlvorgang für TeePilot selbst "
     "ist nicht eingebaut, deshalb steht auf der <a href='/preise/'>Preisseite</a> kein "
     "Kaufknopf. Verbindliche Konditionen klären wir im Gespräch.</p>"),
    ("Wie bekomme ich Unterstützung?",
     "<p>Über das <a href='/kontakt/'>Kontaktformular</a>. Im Repository liegen "
     "außerdem vier Dokumente: Architektur, Betrieb (Sicherung, Umzug, Cronjob, "
     "Stripe, Fehlersuche), Deployment und die Schnittstellenbeschreibung.</p>"),
    ("Wo liegen meine Daten?",
     "<p>Auf deinem eigenen Webspace. TeePilot ist eine Anwendung, die du "
     "installierst – keine gehostete Plattform, bei der die Daten woanders liegen. "
     "Die Datenbank ist eine SQLite-Datei oder eine MySQL-Datenbank deiner Wahl.</p>"),
    ("Werden Schriften von Google geladen?",
     "<p>In der Standardeinstellung nicht. Archivo und Caveat liegen als Dateien auf "
     "deinem Server, zusammen rund 180 KB. Grund ist das Urteil des Landgerichts "
     "München I vom 20. Januar 2022 (Az. 3 O 17493/20), wonach die Einbindung von "
     "Google Fonts die IP-Adresse des Besuchers ohne Einwilligung überträgt. Wählst "
     "du im Backend eine andere Schrift, wird sie von Google geladen – dann aber als "
     "bewusste Entscheidung, auf die der Datenschutzbereich hinweist.</p>"),
    ("Brauche ich einen Cookie-Banner?",
     "<p>Für die eingebaute Websitestatistik nicht: Sie bildet aus IP-Adresse und "
     "einem täglich wechselnden Zufallswert eine Prüfsumme. Wiederkehrende Besuche "
     "eines Tages sind damit erkennbar, eine Person nicht; die IP wird nirgends "
     "gespeichert. Bindest du zusätzlich fremde Dienste ein, gelten deren Regeln – "
     "das ist dann deine Entscheidung.</p>"),
    ("Was passiert, wenn ich einen Bereich nicht brauche?",
     "<p>Du schaltest ihn unter Einstellungen → Tarif ab. Er verschwindet aus dem Menü, "
     "die Daten bleiben vollständig erhalten. Einschalten geht jederzeit wieder, und "
     "alles ist da, wo es war.</p>"),
    ("Brauche ich ein Stripe-Konto?",
     "<p>Nein. Mit hinterlegten Stripe-Schlüsseln sind Kartenzahlung, SEPA, Apple Pay "
     "und Abos möglich. Ohne Stripe wird auf Rechnung verkauft – der Verkauf "
     "funktioniert, nur eben ohne Sofortzahlung.</p>"),
]


def faq():
    inhalt = [
        B.seitenkopf("Häufige Fragen", "Kurz und ohne Marketing.",
                     "Wenn eine Antwort lautet „geht nicht“, steht das hier auch so."),
        B.abschnitt(B.faq(FRAGEN), art="beige"),
        B.abschnitt(
            '<div class="kopfblock kopfblock--mitte">'
            "<h2>Noch Fragen?</h2>"
            '<p class="fuehrung mt-5">Sprich direkt mit uns. Ein kurzes Gespräch klärt '
            "meist mehr als eine lange Seite.</p>"
            '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div></div>'
            % (B.knopf("Kontakt aufnehmen", "/kontakt/", "primaer", "mail"),
               B.knopf("Erst die Demo", "/demo/", "zweit", "play",
                       "product_demo_start")),
        ),
    ]
    return {
        "pfad": "/faq/",
        "titel": "Häufige Fragen",
        "beschreibung": ("Häufige Fragen zu TeePilot: Funktionsumfang, technische "
                         "Voraussetzungen, Datenschutz, Domain, Demo und Kosten."),
        "krumen": [("/", "Start"), ("/faq/", "FAQ")],
        "schema": B.faq_schema(FRAGEN),
        "inhalt": "".join(inhalt),
    }


# ------------------------------------------------------------- /ueber-uns/ --

def ueber_uns():
    """Über uns – linksbündig erzählt, mit genau einem zentrierten Moment.

    Zwei zentrierte Abschnitte hintereinander sehen aus wie eine Vorlage.
    Deshalb läuft hier alles links, bis auf die eine Aussage am Ende.
    """
    story = [
        ("Golf spielen",
         "Auf dem Platz fällt auf, wie unterschiedlich Golfpros aufgestellt "
         "sind – fachlich hervorragend, digital oft allein gelassen."),
        ("Golfpros erleben",
         "Die Website macht ein Bekannter. Termine laufen über WhatsApp. "
         "Die Zehnerkarte ist ein Zettel im Ordner."),
        ("Das Problem erkennen",
         "Es fehlt nicht an Software. Es fehlt an Software, die den Zuschnitt "
         "eines Golfbetriebs kennt."),
        ("Eine Lösung bauen",
         "Kein Baukasten für alle Branchen, sondern die Bereiche, die hier "
         "tatsächlich gebraucht werden."),
        ("Weiterentwickeln",
         "Was Golfpros zurückmelden, bestimmt, was als Nächstes gebaut wird."),
    ]

    person = B.foto_flaeche("person", "hoch",
                            "Der Entwickler von TeePilot auf dem Golfplatz")

    inhalt = [
        B.seitenkopf(
            "Über uns", "Die Idee hinter TeePilot",
            "Keine Firmengründung mit Investorenrunde, sondern ein Produkt, "
            "das aus einem beobachteten Problem gewachsen ist.",
            kompakt=True,
        ),

        # Fließtext, schmal gesetzt – kein Kasten, keine Karte.
        '<section class="abschnitt abschnitt--eng"><div class="huelle">'
        '<div style="max-width:var(--breite-text)">'
        '<p style="font-size:clamp(19px,1.9vw,24px);line-height:1.5;'
        'letter-spacing:-0.012em">Golfpros sind Handwerker mit einem Namen '
        "daran. Sie unterrichten, bauen Vertrauen auf und leben davon, dass "
        "Leute wiederkommen. Der digitale Teil dieses Geschäfts ist bei vielen "
        "ein Nebenschauplatz.</p>"
        '<p style="margin-top:var(--r6);color:var(--tinte-2)">Ein allgemeiner '
        "Website-Baukasten kann sehr viel. Er kennt aber keine Platzreife, "
        "keine Zehnerkarte, keine Verfügbarkeit je Trainer und keinen "
        "Handicap-Eintrag in der Kundenakte. Alles davon lässt sich nachbauen – "
        "und genau das ist die Arbeit, für die ein Golfpro keine Zeit hat.</p>"
        "</div></div></section>",

        # Die Person. Zwischen Idee und Weg, nicht am Anfang: Das Produkt ist
        # das Thema, nicht der Gründer.
        '<section class="abschnitt abschnitt--eng abschnitt--beige zeigen">'
        '<div class="huelle"><div class="person">'
        "<div>%s</div>"
        "<div>"
        '<h2 style="font-size:clamp(26px,3.2vw,42px);max-width:14ch">'
        "Warum ich TeePilot gebaut habe.</h2>"
        '<p class="fuehrung" style="margin-top:var(--r5)">Weil mir beim Golfen '
        "immer wieder dasselbe aufgefallen ist: hervorragende Trainer, deren "
        "digitaler Auftritt nicht zu ihrer Arbeit passt. Nicht aus "
        "Desinteresse – sondern weil die verfügbaren Werkzeuge entweder zu "
        "groß, zu allgemein oder zu teuer sind.</p>"
        '<p style="margin-top:var(--r5);color:var(--tinte-2);max-width:52ch">'
        "TeePilot ist der Versuch, genau dazwischen etwas zu bauen: klein "
        "genug, dass es auf ein gewöhnliches Hosting-Paket passt, und "
        "spezifisch genug, dass es Platzreife, Zehnerkarte und Verfügbarkeit "
        "je Trainer von Anfang an kennt.</p>"
        '<div style="margin-top:var(--r7);padding-top:var(--r5);'
        'border-top:1px solid var(--linie)">'
        '<p class="person__name">[Name eintragen]</p>'
        '<p class="person__rolle">Entwickler von TeePilot</p></div>'
        "</div></div></div></section>"
        % (person or '<div style="border-left:2px solid var(--salbei);'
                     'padding-left:var(--r5)"><p class="notiz" '
                     'style="font-size:1.9em;line-height:1.3">Warum gibt es für '
                     "Golfpros so viele allgemeine Systeme – und so wenig, das "
                     "zu ihrem Alltag passt?</p></div>"),

        # Der Weg als Kette, linksbündig.
        '<section class="abschnitt abschnitt--eng zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px);max-width:12ch">'
        "Wie es dazu kam.</h2></div>"
        "<div>%s</div></div></div></section>" % B.kette(
            [(t, e(x)) for t, x in story]),

        # Der eine zentrierte Moment der Seite.
        B.aussage(
            "Ein junges Produkt.",
            "TeePilot ist kein Softwarekonzern mit tausend Kunden, und diese "
            "Website tut auch nicht so. Es gibt hier keine erfundenen "
            "Nutzerzahlen, keine ausgedachten Kundenstimmen und keine Logos von "
            "Clubs, die nichts davon wissen. Was hier steht, lässt sich im "
            "Produkt nachsehen – und die Aufnahmen stammen aus einer laufenden "
            "Installation, nicht aus einem Entwurfsprogramm.",
            weit=True,
        ),

        '<section class="abschnitt abschnitt--dunkel"><div class="huelle">'
        '<div class="paar paar--unten" style="--paar:minmax(0,6fr) minmax(0,5fr)">'
        '<div class="aussage aussage--weit">'
        "<h2>Werde einer der ersten, die es ausprobieren.</h2>"
        '<p class="aussage__nach" style="color:#b9c8bf">TeePilot wird '
        "gemeinsam mit Golfpros weiterentwickelt. Deshalb suchen wir "
        "Professionals, die es ausprobieren und ehrlich sagen, was fehlt.</p>"
        "</div>"
        '<div class="knopfreihe" style="padding-bottom:6px">'
        '<a class="knopf knopf--hell" href="/kontakt/?anliegen=beta" '
        'data-event="trial_click">Zugang anfragen</a>'
        '<a class="knopf knopf--rand-hell" href="/demo/">Erst die Demo</a>'
        "</div></div></div></section>",
    ]

    return {
        "pfad": "/ueber-uns/",
        "titel": "Über TeePilot",
        "beschreibung": ("Warum TeePilot entstanden ist: ein CMS, das die "
                         "Begriffe eines Golfbetriebs von Anfang an kennt – und "
                         "auf gewöhnlichem Webhosting läuft."),
        "krumen": [("/", "Start"), ("/ueber-uns/", "Über uns")],
        "inhalt": "".join(inhalt),
    }


# -------------------------------------------------------------- /kontakt/ --

def kontakt():
    anliegen = [
        ("demo", "Ich möchte eine Demo sehen"),
        ("test", "Ich möchte TeePilot testen"),
        ("beta", "Ich möchte Feedback geben (Beta)"),
        ("frage", "Ich habe eine Frage"),
        ("sonstiges", "Etwas anderes"),
    ]
    optionen = "".join('<option value="%s">%s</option>' % (e(w), e(t)) for w, t in anliegen)

    endpunkt = (' data-endpunkt="%s"' % e(D.FORMULAR_ENDPUNKT)) if D.FORMULAR_ENDPUNKT else ""

    formular = (
        '<form class="formular" data-formular%s novalidate>'
        '<div class="feldpaar">'
        '<div class="feld"><label for="vorname">Vorname <span class="feld__pflicht">*</span></label>'
        '<input id="vorname" name="vorname" type="text" autocomplete="given-name" required '
        'data-leer="Bitte gib deinen Vornamen ein.">'
        '<span class="feld__fehler"></span></div>'
        '<div class="feld"><label for="nachname">Nachname</label>'
        '<input id="nachname" name="nachname" type="text" autocomplete="family-name"></div>'
        "</div>"
        '<div class="feld"><label for="email">E-Mail <span class="feld__pflicht">*</span></label>'
        '<input id="email" name="email" type="email" autocomplete="email" required '
        'data-leer="Bitte gib deine E-Mail-Adresse ein." '
        'data-ungueltig="Diese E-Mail-Adresse sieht noch nicht richtig aus.">'
        '<span class="feld__fehler"></span></div>'
        '<div class="feldpaar">'
        '<div class="feld"><label for="club">Golfclub oder Betrieb</label>'
        '<input id="club" name="club" type="text" autocomplete="organization">'
        '<span class="feld__hinweis">Hilft uns, die Demo passend einzurichten.</span></div>'
        '<div class="feld"><label for="website">Aktuelle Website</label>'
        '<input id="website" name="website" type="url" inputmode="url" '
        'placeholder="https://" autocomplete="url"></div>'
        "</div>"
        '<div class="feld"><label for="anliegen">Worum geht es?</label>'
        '<select id="anliegen" name="anliegen">%s</select></div>'
        '<div class="feld"><label for="nachricht">Nachricht</label>'
        '<textarea id="nachricht" name="nachricht" '
        'placeholder="Was machst du, und was soll einfacher werden?"></textarea></div>'
        '<div hidden data-sendefehler class="hinweiskasten" '
        'style="border-color:#e8b4b1;background:#fceceb">'
        "<p>Das Senden hat gerade nicht geklappt. Schreib uns bitte direkt an "
        "<strong>%s</strong>.</p></div>"
        '<div><button class="knopf knopf--primaer" type="submit">%s Anfrage senden</button>'
        '<p class="feld__hinweis mt-4">Mit dem Absenden erklärst du dich damit '
        "einverstanden, dass wir deine Angaben zur Beantwortung deiner Anfrage "
        'verwenden. Mehr dazu in der <a href="/datenschutz/">Datenschutzerklärung</a>.</p>'
        "</div>"
        "</form>"
        % (endpunkt, optionen, e(D.KONTAKT_MAIL), icon("send", 17))
    )

    erfolgskasten = (
        '<div class="erfolg" data-an="nein">%s<div>'
        "<h3 style=\"font-size:19px;margin-bottom:6px\">Fast geschafft</h3>"
        "<p>Diese Website hat noch kein angeschlossenes Formular-Backend – deine "
        "Angaben wurden deshalb <strong>nicht</strong> verschickt. Damit nichts "
        "verlorengeht: Schreib uns bitte kurz an <strong>%s</strong>. "
        "Wir melden uns dann mit einem Demo-Zugang.</p></div></div>"
        % (icon("info", 21), e(D.KONTAKT_MAIL))
    )

    inhalt = [
        B.seitenkopf("Kontakt", "TeePilot kennenlernen",
                     "Du möchtest das System testen oder kurz darüber sprechen? "
                     "Ein paar Zeilen reichen."),
        B.abschnitt(
            '<div class="raster raster--2" style="gap:clamp(32px,5vw,72px);align-items:start">'
            "<div>%s%s</div>"
            "<div>%s</div></div>"
            % (formular, erfolgskasten,
               "".join([
                   '<div class="hinweiskasten"><h4>Was passiert danach?</h4>'
                   "<p>Wir melden uns mit einem Zugang zu einem Bereich mit Demo-Bestand "
                   "oder einem Terminvorschlag – je nachdem, was du angekreuzt hast. "
                   "Kein Vertrieb im Hintergrund, keine Mailserie.</p></div>",
                   '<div class="hinweiskasten hinweiskasten--sand mt-5">'
                   "<h4>Lieber erst allein ansehen?</h4>"
                   "<p>Die Produktdemo braucht weder Anmeldung noch Angaben.</p>"
                   '<div class="knopfreihe mt-5">%s</div></div>'
                   % B.knopf("Zur Produktdemo", "/demo/", "zweit", "play",
                             "product_demo_start"),
                   '<div style="margin-top:var(--r6);padding-top:var(--r5);'
                   'border-top:1px solid var(--linie)">'
                   '<h4 style="margin-bottom:6px">Direkt schreiben</h4>'
                   '<p style="font-size:15px;color:var(--tinte-2)">%s</p></div>'
                   % e(D.KONTAKT_MAIL),
               ])),
            art="beige",
        ),
        '<section class="abschnitt abschnitt--eng zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(26px,3vw,40px);max-width:14ch">'
        "Vielleicht steht die Antwort schon da.</h2></div>"
        "<div>%s</div></div></div></section>"
        % B.typoliste([
            ('<a href="/faq/">Häufige Fragen</a>',
             "Funktionsumfang, Technik, Datenschutz, Domain und Kosten – kurz beantwortet."),
            ('<a href="/funktionen/">Alle Funktionen</a>',
             "Zweiundzwanzig Bereiche mit Nachweis, wo sie im System stehen."),
            ('<a href="/demo/beispiel-website/">Beispiel-Website</a>',
             "Wie die Website aussieht, die der Baukasten erzeugt."),
        ]),
    ]

    return {
        "pfad": "/kontakt/",
        "titel": "Kontakt",
        "beschreibung": ("Demo anfragen, TeePilot testen oder eine Frage stellen – "
                         "kurz und unkompliziert."),
        "krumen": [("/", "Start"), ("/kontakt/", "Kontakt")],
        "sticky": False,
        "inhalt": "".join(inhalt),
    }


# ------------------------------------------------------------- Rechtliches --

_PLATZHALTER = (
    '<div class="hinweiskasten hinweiskasten--sand mb-7">'
    "<h4>Noch auszufüllen</h4>"
    "<p>Die Angaben in eckigen Klammern sind Platzhalter und müssen vor der "
    "Veröffentlichung durch die tatsächlichen Daten ersetzt werden. Bis dahin ist "
    "diese Seite nicht rechtsgültig. Diese Vorlage ersetzt keine Rechtsberatung.</p></div>"
)


def impressum():
    inhalt = [
        B.seitenkopf("Rechtliches", "Impressum", "Angaben gemäß § 5 DDG."),
        B.abschnitt(
            _PLATZHALTER
            + '<div class="fliess">'
              "<h3>Diensteanbieter</h3>"
              "<p>[Name des Unternehmens oder der Person]<br>"
              "[Straße und Hausnummer]<br>[PLZ und Ort]<br>[Land]</p>"
              "<h3 class=\"mt-7\">Kontakt</h3>"
              "<p>E-Mail: [E-Mail-Adresse]<br>Telefon: [Telefonnummer]</p>"
              "<h3 class=\"mt-7\">Vertretungsberechtigte Person</h3>"
              "<p>[Vor- und Nachname]</p>"
              "<h3 class=\"mt-7\">Registereintrag</h3>"
              "<p>[Registergericht und Registernummer, falls vorhanden]</p>"
              "<h3 class=\"mt-7\">Umsatzsteuer-Identifikationsnummer</h3>"
              "<p>[USt-IdNr. gemäß § 27 a UStG, falls vorhanden]</p>"
              "<h3 class=\"mt-7\">Verantwortlich für den Inhalt</h3>"
              "<p>[Vor- und Nachname]<br>[Anschrift wie oben]</p>"
              "<h3 class=\"mt-7\">Verbraucherstreitbeilegung</h3>"
              "<p>Wir sind nicht bereit und nicht verpflichtet, an "
              "Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle "
              "teilzunehmen.</p>"
              "<h3 class=\"mt-7\">Haftung für Inhalte und Links</h3>"
              "<p>Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten "
              "nach den allgemeinen Gesetzen verantwortlich. Für Inhalte externer Links "
              "ist der jeweilige Anbieter verantwortlich. Zum Zeitpunkt der Verlinkung "
              "waren keine Rechtsverstöße erkennbar.</p>"
              "<h3 class=\"mt-7\">Urheberrecht</h3>"
              "<p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen "
              "Seiten unterliegen dem deutschen Urheberrecht.</p>"
              "</div>",
        ),
    ]
    return {
        "pfad": "/impressum/", "titel": "Impressum",
        "beschreibung": "Impressum und Anbieterkennzeichnung.",
        "krumen": [("/", "Start"), ("/impressum/", "Impressum")],
        "noindex": True, "sticky": False, "band": False,
        "inhalt": "".join(inhalt),
    }


def datenschutz():
    inhalt = [
        B.seitenkopf("Rechtliches", "Datenschutzerklärung",
                     "Wie diese Website mit personenbezogenen Daten umgeht."),
        B.abschnitt(
            _PLATZHALTER
            + '<div class="fliess">'
              "<h3>1. Verantwortlicher</h3>"
              "<p>[Name]<br>[Anschrift]<br>E-Mail: [E-Mail-Adresse]</p>"

              "<h3 class=\"mt-7\">2. Hosting und Server-Logfiles</h3>"
              "<p>Diese Website wird bei [Hosting-Anbieter] gehostet. Beim Aufruf "
              "erhebt der Anbieter technisch notwendige Zugriffsdaten (unter anderem "
              "IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, übertragene "
              "Datenmenge). Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO – unser "
              "berechtigtes Interesse am sicheren und störungsfreien Betrieb. "
              "Die Speicherdauer beträgt [Anzahl] Tage.</p>"

              "<h3 class=\"mt-7\">3. Schriftarten</h3>"
              "<p>Die verwendeten Schriften Archivo und Caveat werden von diesem "
              "Server ausgeliefert. Es findet <strong>keine</strong> Verbindung zu "
              "Servern von Google statt, und es wird keine IP-Adresse an Dritte "
              "übertragen.</p>"

              "<h3 class=\"mt-7\">4. Cookies</h3>"
              "<p>Diese Website setzt keine Cookies zu Analyse- oder Werbezwecken. "
              "Für einen ausgeblendeten Hinweis am unteren Bildschirmrand wird ein "
              "Eintrag im <code>sessionStorage</code> deines Browsers gespeichert. "
              "Er enthält keine personenbezogenen Daten, verlässt dein Gerät nicht "
              "und wird beim Schließen des Browser-Tabs gelöscht.</p>"

              "<h3 class=\"mt-7\">5. Kontaktformular</h3>"
              "<p>Wenn du uns über das Kontaktformular schreibst, verarbeiten wir die "
              "angegebenen Daten (Name, E-Mail-Adresse, Betrieb, Website und deine "
              "Nachricht) zur Bearbeitung deiner Anfrage. Rechtsgrundlage ist "
              "Art. 6 Abs. 1 lit. b DSGVO beziehungsweise lit. f DSGVO. Die Daten "
              "werden gelöscht, sobald die Anfrage abschließend bearbeitet ist und "
              "keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>"

              "<h3 class=\"mt-7\">6. Reichweitenmessung</h3>"
              "<p>[Falls eine Reichweitenmessung eingesetzt wird, ist sie hier zu "
              "beschreiben. Solange keine eingebunden ist, findet keine "
              "Reichweitenmessung statt.]</p>"

              "<h3 class=\"mt-7\">7. Deine Rechte</h3>"
              "<p>Du hast das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung "
              "(Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung "
              "(Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). "
              "Außerdem steht dir ein Beschwerderecht bei einer Aufsichtsbehörde zu "
              "(Art. 77 DSGVO). Wende dich dafür an die oben genannte Adresse.</p>"

              "<h3 class=\"mt-7\">8. Hinweis zum Produkt TeePilot</h3>"
              "<p>Diese Datenschutzerklärung gilt für diese Website. Betreibst du "
              "selbst eine Installation von TeePilot, bist du für die dort "
              "verarbeiteten Daten verantwortlich; die Anwendung bringt dafür einen "
              "eigenen Datenschutzbereich mit.</p>"
              "</div>",
        ),
    ]
    return {
        "pfad": "/datenschutz/", "titel": "Datenschutzerklärung",
        "beschreibung": "Wie diese Website mit personenbezogenen Daten umgeht.",
        "krumen": [("/", "Start"), ("/datenschutz/", "Datenschutz")],
        "noindex": True, "sticky": False, "band": False,
        "inhalt": "".join(inhalt),
    }


# ------------------------------------------------------------------- 404 --

def vierhundertvier():
    inhalt = [
        '<section class="abschnitt"><div class="huelle">'
        '<div class="vierhundert"><div>'
        '<p class="vierhundert__zahl">Aus dem Fairway.</p>'
        "<h1 style=\"font-size:clamp(30px,4vw,48px)\">Hier ist kein Fairway.</h1>"
        '<p class="fuehrung mt-5" style="margin-inline:auto">Die gesuchte Seite '
        "konnte nicht gefunden werden. Vielleicht wurde sie verschoben – oder es "
        "hat sich ein Tippfehler in die Adresse geschlichen.</p>"
        '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div>'
        '<p class="mt-8" style="font-size:14.5px;color:var(--tinte-3)">'
        'Oder direkt zu: <a href="/produkt/">Produkt</a> · '
        '<a href="/funktionen/">Funktionen</a> · <a href="/demo/">Demo</a> · '
        '<a href="/preise/">Preise</a> · <a href="/kontakt/">Kontakt</a></p>'
        "</div></div></div></section>"
        % (B.knopf("Zur Startseite", "/", "primaer"),
           B.knopf("Produktdemo ansehen", "/demo/", "zweit", "play")),
    ]
    return {
        "pfad": "/404.html", "titel": "Seite nicht gefunden",
        "beschreibung": "Die gesuchte Seite konnte nicht gefunden werden.",
        "noindex": True, "sticky": False, "band": False,
        "inhalt": "".join(inhalt),
    }
