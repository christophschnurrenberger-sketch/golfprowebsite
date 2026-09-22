# -*- coding: utf-8 -*-
"""
Startseite.

Aufbau nach einer Regel: Keine zwei Abschnitte hintereinander sehen gleich
aus. Aufmacher, Aussage, Produkt über die volle Breite, fünf nummerierte
Kapitel, Gegenüberstellung, Ablauf, dunkler Markenmoment, Beispielwebsite,
Liste, Fragen, Schluss. Kachelraster kommt darin nicht vor.
"""

import daten as D
from icons import icon
from layout import e
import bausteine as B


# ------------------------------------------------------------- Aufmacher --

def hero():
    """Asymmetrisch: Text links, Produkt rechts und tiefer gesetzt.

    Das Produktbild schiebt sich über die Kante des nächsten Abschnitts –
    Tiefe über Position statt über Schatten.
    """
    foto = B.foto_flaeche("hero", "hoch",
                          "Golfprofessional beim Training auf der Range")
    nebenspalte = foto if foto else B.rahmen("app-dashboard", lazy=False)

    return (
        '<section style="padding-block:clamp(56px,7vw,104px) 0">'
        '<div class="huelle huelle--weit">'
        '<div class="paar paar--unten" style="--paar:minmax(0,5fr) minmax(0,6fr)">'
        "<div>"
        "<h1>Mehr Zeit für deine Schüler.<br>"
        "Weniger Zeit für <mark>deine Website</mark>.</h1>"
        '<p class="fuehrung" style="margin-top:var(--r6);max-width:48ch">'
        "TeePilot ist ein Content-Management-System für Golfpros. Du "
        "pflegst deine Website selbst, gibst Trainingszeiten zur Buchung "
        "frei und hast deine Schüler, Pakete und Rechnungen an einer "
        "Stelle.</p>"
        '<div class="knopfreihe" style="margin-top:var(--r7)">'
        '<a class="knopf knopf--primaer" href="/demo/" data-event="hero_demo_click">'
        "Demo ansehen</a>"
        '<a class="knopf knopf--zweit" href="/produkt/">Produkt ansehen</a>'
        "</div></div>"
        '<div style="padding-bottom:clamp(8px,2vw,28px)">%s</div>'
        "</div></div></section>"
        % nebenspalte
    )


def hero_produkt():
    """Das Produkt gleich im ersten Bildschirm, groß und angeschnitten."""
    return (
        '<section style="padding-block:clamp(40px,5vw,72px) 0">'
        '<div class="huelle huelle--weit">'
        '<div class="ueberlappt">%s</div>'
        "</div></section>"
        % B.bild_mit_legende(
            "app-dashboard", "01", "Dashboard",
            "Umsatz, Auslastung und die nächsten Termine – beim Öffnen, ohne Suchen.",
            lazy=False)
    ) if B.hat_foto("hero") else ""


# --------------------------------------------------------------- Aussage --

def aussage_problem():
    return B.aussage(
        "Software sollte<br>Arbeit abnehmen.",
        "Nicht neue erzeugen. Sechs Bereiche sind deshalb immer da. "
        "Sechzehn weitere schaltest du ein, wenn du sie brauchst. Wer nur "
        "unterrichtet, sieht neun Menüpunkte statt zweiundzwanzig.",
        weit=True,
    )


def band_foto():
    """Breiter Bildstreifen als Zäsur – nur wenn ein Foto hinterlegt ist."""
    f = B.foto_flaeche("band", "breit", "Blick über die Driving Range", rund=False)
    if not f:
        return ""
    return '<section class="voll" style="padding-block:0">%s</section>' % f


# ------------------------------------------------- Produkt, volle Breite --

def produkt_voll():
    return (
        '<section class="abschnitt abschnitt--eng zeigen">'
        '<div class="huelle"><div class="aussage" >'
        '<h2 style="font-size:clamp(30px,3.9vw,54px);max-width:16ch">Ein Blick ins System.</h2>'
        '<p class="fuehrung mt-5">Das siehst du nach dem Anmelden. Kein '
        "Startbildschirm, den du erst einrichten musst.</p>"
        "</div></div>"
        '<div class="huelle huelle--weit" style="margin-top:var(--r8)">%s</div>'
        "</section>"
        % B.bild_mit_legende(
            "app-dashboard", "01", "Dashboard",
            "Umsatz, Auslastung, die nächsten Termine – und Hinweise, die aus "
            "den eigenen Zahlen kommen.", lazy=False)
    )


# ------------------------------------------------------ Nummerierte Kapitel --

def kapitel():
    """Fünf Bereiche, jeder mit eigener Doppelseite statt eigener Kachel."""
    eintraege = [
        ("01", "Website",
         "Seiten entstehen aus Bausteinen. Du sortierst sie per Griff, änderst "
         "Texte an der Stelle, an der sie stehen, und siehst sofort, wie es "
         "aussieht.",
         "app-baukasten",
         ["27 Bausteine vom Titelbereich bis zum Buchungskalender",
          "Vorschau für Desktop, Tablet und Telefon",
          "Veröffentlichen oder als Entwurf liegen lassen"],
         "/funktionen/website/", False),

        ("02", "Buchungen",
         "Du gibst frei, wann du Zeit hast. Deine Kunden buchen selbst – mit "
         "Konto oder ohne. Der Termin steht danach in deinem Kalender.",
         "app-verfuegbarkeit",
         ["Verfügbarkeiten je Leistung, Trainer und Standort",
          "Warteliste und Erinnerungen per E-Mail",
          "Pakete mit gezählten Einheiten statt Strichliste"],
         "/funktionen/buchungen/", True),

        ("03", "Kunden",
         "Handicap, Historie, gekaufte Pakete, Rechnungen und Notizen liegen "
         "an einer Stelle. Vor der Stunde ein Blick hinein – und du weißt "
         "wieder, woran ihr arbeitet.",
         "app-kundenakte",
         ["Alle bisherigen Termine auf einen Blick",
          "Offene Einheiten je Paket",
          "Eigene Felder und Etiketten"],
         "/produkt/", False),

        ("04", "Kurse",
         "Theorie einmal aufnehmen statt fünfzigmal erzählen. Module, "
         "Lektionen, Quiz – und daneben Trainingspläne für die Zeit zwischen "
         "zwei Stunden.",
         "app-kurs-detail",
         ["Lektionen als Text oder Video",
          "Fortschritt je Teilnehmer",
          "Eigene Übungsbibliothek für Trainingspläne"],
         "/funktionen/kurse/", True),

        ("05", "Rechnungen",
         "Eine Rechnungsposition führt Titel, Preis und Steuersatz als eigene "
         "Werte. Ändert sich später der Preis der Leistung, bleibt die "
         "Rechnung, wie sie war.",
         "app-rechnung",
         ["Rechnungsnummern ohne Lücken",
          "Korrigiert wird mit einer Gutschrift, gelöscht wird nie",
          "Ausgabe als PDF"],
         "/funktionen/", False),
    ]
    teile = []
    for nr, titel, text, bild, punkte, url, gedreht in eintraege:
        teile.append(B.kapitel(
            nr, titel, e(text), bild, punkte=punkte, gedreht=gedreht,
            fuss=B.pfeil_link("Mehr dazu", url),
        ))
    return (
        '<section class="abschnitt abschnitt--eng"><div class="huelle">'
        '<div class="aussage" style="margin-bottom:var(--r8)">'
        '<h2 style="font-size:clamp(30px,3.8vw,52px)">Was du damit machst.</h2>'
        '<p class="fuehrung mt-5">Fünf von zweiundzwanzig. Die übrigen '
        'stehen unter <a href="/funktionen/">Funktionen</a>.</p>'
        "</div>%s</div></section>" % "".join(teile)
    )


# ----------------------------------------------------------- Split-Screen --

def vom_cms_zur_website():
    return (
        '<section class="abschnitt abschnitt--beige zeigen"><div class="huelle">'
        '<div class="aussage" style="margin-bottom:var(--r8)">'
        '<h2 style="font-size:clamp(30px,3.8vw,52px)">Vom CMS direkt auf deine Website.</h2>'
        '<p class="aussage__nach">Was du anlegst, erscheint öffentlich. '
        "Ein Kurs, ein Preis, ein freier Termin – dieselbe Angabe, zwei "
        "Ansichten.</p></div>"
        "%s</div></section>"
        % B.split("Du verwaltest", "app-leistungen",
                  "Dein Kunde sieht", "pub-buchen",
                  links_nr="CMS · Leistungen", rechts_nr="Website · Buchung")
    )


# ---------------------------------------------------------------- Ablauf --

def ablauf_kurs():
    return (
        '<section class="abschnitt zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,5fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px)">Du hast einen neuen Kurs.</h2>'
        '<p class="fuehrung" style="margin-top:var(--r5)">Vier Schritte, und er '
        "steht auf deiner Website. Keine Anfrage, kein Warten, keine zweite "
        "Liste.</p></div>"
        "<div>%s</div></div></div></section>"
        % B.kette([
            ("Kurs anlegen",
             "Titel, Beschreibung, Plätze, Preis. Einmal, im Bereich Kurse."),
            ("Auf eine Seite stellen",
             "Den Baustein „Kurse“ auf die Seite ziehen, an die Stelle, "
             "an der er stehen soll."),
            ("Veröffentlichen",
             "Die Seite geht live. Der Kurs erscheint mit Preis und "
             "freien Plätzen."),
            ("Anmeldungen laufen ein",
             "Die Plätze zählt das System. Du siehst, wer kommt."),
        ])
    )


# ----------------------------------------------------------- Markenmoment --

def dunkler_moment():
    return (
        '<section class="abschnitt abschnitt--dunkel zeigen"><div class="huelle">'
        '<div class="aussage aussage--weit">'
        "<h2>Du kennst dein Golfbusiness.<br>"
        "Jetzt sollte auch deine Website so funktionieren.</h2>"
        '<p class="aussage__nach" style="color:#b9c8bf">Nicht umgekehrt: '
        "Du passt dich nicht einem System an, das für alle Branchen gebaut "
        "wurde.</p></div>"
        '<div style="max-width:880px;margin-top:var(--r9)">%s</div>'
        "</div></section>"
        % B.rahmen("app-kalender")
    )


# ------------------------------------------------------- Beispielwebsite --

def beispielwebsite():
    return (
        '<section class="abschnitt zeigen"><div class="huelle">'
        '<div style="display:flex;justify-content:space-between;'
        'align-items:flex-end;gap:var(--r6);flex-wrap:wrap;margin-bottom:var(--r8)">'
        '<div class="aussage">'
        '<h2 style="font-size:clamp(30px,3.8vw,52px)">Und so sieht deine Seite aus.</h2>'
        "</div>"
        '<p style="max-width:40ch;font-size:15.5px;color:var(--tinte-2)">'
        "Diese Website hat TeePilot selbst erzeugt. Die schraffierten "
        "Flächen sind Bildplätze – dort stehen später deine eigenen "
        "Aufnahmen.</p></div>"
        "%s"
        '<div class="knopfreihe" style="margin-top:var(--r8)">%s%s</div>'
        "</div></section>"
        % (B.geraete({
               "desktop": "pub-site-start-full",
               "tablet": "pub-site-start-tablet",
               "mobile": "pub-site-start-mobile",
           }, gruppe="start_beispiel"),
           B.knopf("Beispiel-Website ansehen", "/demo/beispiel-website/",
                   "primaer", event="demo_website_open"),
           B.knopf("Wie der Baukasten funktioniert", "/funktionen/website/", "zweit"))
    )


# ------------------------------------------------------ Heute / mit CMS --

def gegenueber():
    heute = [
        ("Website", "Änderung beim Dienstleister anfragen und warten."),
        ("Termine", "WhatsApp, Telefon, Mail, Zuruf auf der Range."),
        ("Kurse", "In einer Tabelle, auf der Website und im Aushang – drei Stände."),
        ("Zehnerkarten", "Auf Papier. Wie viele offen sind, weiß meist der Kunde besser."),
        ("Rechnungen", "In Word, mit selbst vergebener Nummer."),
    ]
    mit = [
        ("Website", "Text anklicken, ändern, speichern."),
        ("Termine", "Freie Zeiten stehen online, der Kunde bucht selbst."),
        ("Kurse", "Einmal angelegt, überall aktuell."),
        ("Zehnerkarten", "Pakete mit gezählten Einheiten, Hinweis vor Ablauf."),
        ("Rechnungen", "Lückenlose Nummern, Gutschrift statt Löschung."),
    ]
    return (
        '<section class="abschnitt abschnitt--beige zeigen"><div class="huelle">'
        '<div class="aussage" style="margin-bottom:var(--r8)">'
        '<h2 style="font-size:clamp(30px,3.8vw,52px)">Heute und danach.</h2></div>'
        '<div class="split">'
        '<div><span class="split__marke">Heute</span>%s</div>'
        '<div class="split__linie" aria-hidden="true"></div>'
        '<div><span class="split__marke split__marke--gruen">Mit TeePilot</span>%s</div>'
        "</div>"
        '<p style="margin-top:var(--r6);font-size:14px;color:var(--tinte-3);'
        'max-width:60ch">Beispielhafte Darstellung. Was TeePilot bei dir '
        "ersetzt, hängt davon ab, womit du heute arbeitest.</p>"
        "</div></section>"
        % (B.typoliste([(t, e(x)) for t, x in heute]),
           B.typoliste([(t, e(x)) for t, x in mit]))
    )


# -------------------------------------------------------------- Für wen --

def fuer_wen():
    return (
        '<section class="abschnitt zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px)">Gebaut für den Golfbetrieb.</h2>'
        '<p class="fuehrung" style="margin-top:var(--r5)">Der Zuschnitt ist '
        "überall derselbe. Was sich unterscheidet, ist, welche Bereiche du "
        "einschaltest.</p></div>"
        "<div>%s</div></div></div></section>"
        % B.typoliste([
            ('<a href="/fuer-golfpros/">Golfpros</a>',
             "Eigene Angebote, eigener Auftritt, alles selbst in der Hand."),
            ('<a href="/fuer-golflehrer/">Golflehrer</a>',
             "Unterricht steht im Vordergrund. Website pflegen dauert fünf Minuten."),
            ('<a href="/fuer-golfakademien/">Golfakademien</a>',
             "Mehrere Trainer, mehrere Standorte, Rollen und getrennte Kalender."),
        ])
    )


# ---------------------------------------------------------------- Preise --

def preise_kurz():
    return (
        '<section class="abschnitt abschnitt--beige zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,5fr) minmax(0,5fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px)">Vier Stufen, ein Produkt.</h2>'
        '<p class="fuehrung" style="margin-top:var(--r5)">Die Stufe legt fest, '
        "welche Bereiche du einschalten <em>kannst</em>. Was tatsächlich im "
        "Menü steht, entscheidest du selbst.</p>"
        '<div class="knopfreihe" style="margin-top:var(--r7)">%s</div></div>'
        "<div>%s"
        '<p style="margin-top:var(--r5);font-size:14px;color:var(--tinte-3);'
        'max-width:46ch">Die Stufen steuern im CMS den Funktionsumfang. Eine '
        "automatische Abrechnung ist nicht eingebaut – deshalb steht hier kein "
        "Kaufknopf.</p></div>"
        "</div></div></section>"
        % (B.knopf("Stufen im Detail", "/preise/", "zweit"),
           B.typoliste([
               ("Starter · 29 €", "Website, Online-Buchung, Kundenakte, Kalender, Blog."),
               ("Pro · 59 €", "Dazu Verkauf, Rechnungen, Kurse, Events, Newsletter."),
               ("Business · 99 €", "Dazu KI-Assistent, Videoanalyse, Automationen, Auswertung."),
               ("Academy · 199 €", "Dazu mehrere Trainer und Standorte, eigene Domain."),
           ]))
    )


# ----------------------------------------------------------------- Fragen --

def fragen():
    paare = [
        ("Brauche ich technische Kenntnisse?",
         "<p>Zum Bedienen nicht. Seiten baust du aus fertigen Bausteinen und "
         "siehst sofort, wie es aussieht. Für die Einrichtung brauchst du einen "
         "Webspace mit PHP: Dateien hochladen, eine Adresse aufrufen, drei "
         "Felder ausfüllen.</p>"),
        ("Wo liegen meine Daten?",
         "<p>Auf deinem eigenen Webspace. TeePilot ist eine Anwendung, die du "
         "installierst – keine Plattform, bei der die Daten woanders liegen.</p>"),
        ("Kann ich meine eigene Domain verwenden?",
         "<p>Ja. Das System erkennt die aufgerufene Domain und liefert die "
         "dazugehörige Website aus.</p>"),
        ("Kann ich das vorher ausprobieren?",
         "<p>Die <a href='/demo/'>Produktdemo</a> zeigt alle Bereiche mit echten "
         "Aufnahmen, ohne Anmeldung. Für einen eigenen Zugang schreib uns kurz "
         "über das <a href='/kontakt/'>Kontaktformular</a>.</p>"),
    ]
    return (
        '<section class="abschnitt zeigen"><div class="huelle">'
        '<div class="paar" style="--paar:minmax(0,4fr) minmax(0,7fr)">'
        "<div>"
        '<h2 style="font-size:clamp(28px,3.4vw,46px)">Kurz beantwortet.</h2>'
        '<p class="fuehrung" style="margin-top:var(--r5)">Ausführlicher steht es '
        'in den <a href="/faq/">häufigen Fragen</a>.</p></div>'
        "<div>%s</div></div></div></section>" % B.faq(paare)
    )


# ---------------------------------------------------------------- Schluss --

def schluss():
    return (
        '<section class="abschnitt abschnitt--dunkel"><div class="huelle">'
        '<div class="paar paar--unten" style="--paar:minmax(0,6fr) minmax(0,5fr)">'
        '<div class="aussage aussage--weit">'
        "<h2>Sieh es dir an.</h2>"
        '<p class="aussage__nach" style="color:#b9c8bf">Die Demo braucht keine '
        "Anmeldung und keine Angaben. Wenn es nicht passt, hast du zwei Minuten "
        "verloren.</p></div>"
        '<div class="knopfreihe" style="padding-bottom:6px">'
        '<a class="knopf knopf--hell" href="/demo/" data-event="footer_demo_click">'
        "Demo ansehen</a>"
        '<a class="knopf knopf--rand-hell" href="/kontakt/" data-event="footer_contact_click">'
        "Persönlich sprechen</a></div>"
        "</div></div></section>"
    )


# ------------------------------------------------------------------ Seite --

def bauen():
    return {
        "pfad": "/",
        "titel": "TeePilot – Das CMS für Golfpros",
        "titel_roh": True,
        "beschreibung": ("TeePilot unterstützt Golfpros, Golflehrer und "
                         "Golfakademien bei ihrer digitalen Präsenz: Website, "
                         "Online-Buchung, Kundenakte und Kurse in einer Anwendung."),
        "og_titel": "TeePilot – Das CMS für Golfpros",
        "og_text": "Mehr Zeit für deine Schüler. Weniger Zeit für deine Website.",
        "schema": """{"@context":"https://schema.org","@type":"SoftwareApplication",
"name":"TeePilot","applicationCategory":"BusinessApplication",
"operatingSystem":"Webbrowser, PHP 8.1+",
"description":"CMS und Verwaltung für Golf Professionals: Website-Baukasten, Online-Buchung, Kundenakte, Kurse, Rechnungen."}""",
        "inhalt": "".join([
            hero(),
            hero_produkt(),
            aussage_problem(),
            band_foto(),
            produkt_voll(),
            kapitel(),
            vom_cms_zur_website(),
            ablauf_kurs(),
            dunkler_moment(),
            beispielwebsite(),
            gegenueber(),
            fuer_wen(),
            preise_kurz(),
            fragen(),
            schluss(),
        ]),
    }
