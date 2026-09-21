# -*- coding: utf-8 -*-
"""Startseite – die Seite, die in zehn Sekunden funktionieren muss."""

import daten as D
from icons import icon
from layout import e
import bausteine as B


def hero():
    karte = (
        '<div class="hero__karte">'
        '<p class="hero__karte-titel">Auslastung diese Woche</p>'
        '<p class="hero__karte-wert">74 %</p>'
        '<p class="hero__karte-zeile">37 Termine</p></div>'
    )
    return (
        '<section class="hero"><div class="huelle huelle--weit">'
        '<div class="hero__raster">'
        "<div>"
        '<p class="vorzeile">Das CMS für Golfpros</p>'
        "<h1>Mehr Zeit für deine Schüler.<br>"
        "Weniger Zeit für <mark>deine Website.</mark></h1>"
        '<p class="hero__fuehrung">GolfProCMS ist eine Anwendung für den '
        "digitalen Teil deines Golfbusiness: Website, Online-Buchung, Kundenakte, "
        "Kurse, Rechnungen. Du pflegst deine Seite selbst – ohne jemanden zu fragen, "
        "der Zeit hat.</p>"
        '<div class="knopfreihe">'
        '<a class="knopf knopf--primaer" href="/demo/" data-event="hero_demo_click">%s Produktdemo ansehen</a>'
        '<a class="knopf knopf--zweit" href="/demo/beispiel-website/" data-event="demo_website_open">'
        "So sieht die Website aus</a>"
        "</div>"
        '<p class="hero__fuss">Läuft auf einem gewöhnlichen Webhosting-Paket. '
        "Kein Abo nötig, um es anzusehen.</p>"
        "</div>"
        '<div class="hero__visual">%s%s</div>'
        "</div></div></section>"
        % (icon("play", 17), B.rahmen("app-dashboard", lazy=False), karte)
    )


def vertrauen():
    return (
        '<section><div class="huelle">%s</div></section>' % B.vertrauen()
    )


def problem():
    karten = [
        B.karte("Eine Zeile ändern dauert drei Tage",
                "Neuer Preis, neuer Termin, neuer Text – und du schreibst erst jemandem, "
                "der es einbaut, wenn er dazu kommt.", "clock"),
        B.karte("Die Kurse stehen an vier Stellen",
                "Auf der Website, im Aushang, in der Mail an die Stammkunden und im Kopf. "
                "Drei davon sind veraltet.", "list"),
        B.karte("Buchungen kommen über fünf Kanäle",
                "WhatsApp, Telefon, Mail, Zuruf auf der Range. Wer wann kommt, weiß nur "
                "dein Kalender – wenn du ihn gepflegt hast.", "calendar"),
        B.karte("Die Zehnerkarte liegt im Ordner",
                "Wie viele Einheiten offen sind, weiß am Ende meistens der Kunde besser "
                "als du.", "ticket"),
    ]
    return B.abschnitt(
        B.kopfblock("Der Alltag",
                    "Deine Website sollte dir Arbeit abnehmen.<br>Nicht machen.",
                    "Das hier ist kein erfundenes Problem. Es ist der Grund, warum "
                    "GolfProCMS überhaupt entstanden ist.")
        + B.raster(karten, 4),
        art="beige",
    )


def loesung():
    heute = [
        "Website beim Dienstleister",
        "Termine per WhatsApp",
        "Kurse in einer Excel-Tabelle",
        "Zehnerkarten auf Papier",
        "Rechnungen in Word",
        "Adressen im Telefon",
    ]
    mit = [
        "Website selbst bearbeiten",
        "Online-Buchung auf der eigenen Seite",
        "Kurse und Events an einer Stelle",
        "Pakete mit gezählten Einheiten",
        "Rechnungen mit lückenloser Nummer",
        "Kundenakte mit Historie",
    ]
    return B.abschnitt(
        B.kopfblock("Die Idee", "Ein System für deinen digitalen Golfalltag.",
                    "GolfProCMS wurde nicht für irgendein Unternehmen gebaut. Der "
                    "Zuschnitt folgt den Aufgaben, die bei einem Golfpro tatsächlich "
                    "anfallen.")
        + B.gegenueber(heute, mit)
        + '<p class="mt-6" style="font-size:14.5px;color:var(--tinte-3);max-width:62ch">'
          "Beispielhafte Darstellung einer typischen Situation. Was GolfProCMS bei dir "
          "ersetzt, hängt davon ab, womit du heute arbeitest.</p>"
    )


def module():
    """Nur die Bereiche, die es im CMS tatsaechlich gibt."""
    zeigen = ["website", "bookings", "customers", "courses", "invoices", "analytics"]
    karten = []
    for key in zeigen:
        m = D.MODULE_NACH_KEY[key]
        karten.append(B.karte(
            m["name"], e(m["kurz"]), m["icon"],
            url=m.get("seite") or "/funktionen/#" + m["key"],
            link_text="Ansehen",
        ))
    return B.abschnitt(
        B.kopfblock("Die Bereiche", "Was GolfProCMS mitbringt.",
                    "Sechs Bereiche sind immer da. Alles Weitere schaltest du ein, "
                    "wenn du es brauchst – und wieder aus, wenn nicht. "
                    '<a href="/funktionen/">Alle %d Bereiche ansehen →</a>'
                    % D.SYSTEMZAHLEN["module"])
        + B.raster(karten, 3)
        + '<div class="knopfreihe mt-7">%s</div>'
          % B.knopf("Alle Funktionen im Überblick", "/funktionen/", "zweit"),
        art="weiss",
    )


def grosser_screenshot():
    return B.abschnitt(
        '<div class="kopfblock kopfblock--mitte">'
        '<p class="vorzeile" style="justify-content:center">Sieh es dir an</p>'
        "<h2>Alles Wichtige auf einen Blick.</h2>"
        '<p class="fuehrung mt-5">Das ist der erste Bildschirm nach dem Anmelden: '
        "Umsatz, Auslastung, die nächsten Termine – und Hinweise, die aus deinen "
        "eigenen Zahlen kommen.</p></div>"
        + B.screenshot_block("app-dashboard")
        + '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div>'
          % (B.knopf("Produktdemo starten", "/demo/", "primaer", "play",
                     "product_demo_start"),
             B.knopf("Dashboard im Detail", "/funktionen/dashboard/", "zweit")),
        art="beige",
    )


def wechsel_abschnitt():
    eintraege = [
        ("website", "Website", "Seiten aus Bausteinen, mit Vorschau.", "app-baukasten"),
        ("buchungen", "Buchungen", "Verfügbarkeiten, Termine, Warteliste.", "app-buchungen"),
        ("kunden", "Kunden", "Akte mit Historie, Paketen und Notizen.", "app-kundenakte"),
        ("kurse", "Kurse", "Module, Lektionen, Fortschritt.", "app-kurs-detail"),
        ("rechnungen", "Rechnungen", "Positionen, Gutschriften, offene Posten.", "app-rechnung"),
    ]
    return B.abschnitt(
        B.kopfblock("Im Detail", "Fünf Bereiche, fünf Aufnahmen.",
                    "Klick dich durch. Jedes Bild kommt aus einer laufenden "
                    "Installation mit dem Demo-Bestand, den das CMS selbst anlegt.")
        + B.wechsel(eintraege),
        art="weiss",
    )


def kundensicht():
    """Der wichtigste Erklaerbaustein: Backend links, Kundensicht rechts."""
    return B.abschnitt(
        '<div class="kopfblock kopfblock--mitte">'
        '<p class="vorzeile" style="justify-content:center">Zwei Seiten derselben Sache</p>'
        "<h2>Du verwaltest. Deine Kunden sehen.</h2>"
        '<p class="fuehrung mt-5">Was du im CMS anlegst, erscheint auf deiner Website. '
        "Ein Kurs, ein Preis, ein freier Termin – dieselbe Angabe, zwei Ansichten.</p></div>"
        '<div class="raster raster--2" style="align-items:start">'
        "<div>"
        '<p class="marke-etikett mb-5">Du im CMS</p>%s</div>'
        "<div>"
        '<p class="marke-etikett marke-etikett--sand mb-5">Dein Kunde auf der Website</p>%s</div>'
        "</div>"
        '<div class="mt-8">%s</div>'
        % (B.screenshot_block("app-leistungen"),
           B.screenshot_block("pub-buchen"),
           B.ablauf([
               ("Du legst eine Leistung an",
                "Name, Dauer, Preis, wer sie gibt – einmal. "
                "<span style='color:var(--tinte-4)'>Bereich: Buchungen</span>"),
               ("Du gibst Zeiten frei",
                "Pro Leistung und pro Trainer, als wiederkehrende Zeiten. "
                "<span style='color:var(--tinte-4)'>Bereich: Verfügbarkeiten</span>"),
               ("Dein Kunde bucht selbst",
                "Zeit wählen, Angaben, Bestätigung. Mit Konto oder ohne."),
               ("Der Termin steht im Kalender",
                "Bei dir, mit Erinnerung für beide Seiten."),
           ])),
    )


def beispielwebsite():
    return B.abschnitt(
        '<div class="kopfblock kopfblock--mitte">'
        '<p class="vorzeile" style="justify-content:center">Das Ergebnis</p>'
        "<h2>So könnte deine eigene Golfpro-Website aussehen.</h2>"
        '<p class="fuehrung mt-5">GolfProCMS ist nicht nur Verwaltung im Hintergrund. '
        "Der Baukasten erzeugt die öffentliche Website – diese hier hat das System "
        "selbst gebaut.</p></div>"
        + '<p class="bildunter" style="justify-content:center;margin:0 0 var(--r5)"><span class="marke-etikett marke-etikett--grau">Bildflächen</span><span>Die schraffierten Flächen sind Platzhalter – so zeigt der Baukasten eine Bildfläche, solange kein Foto hochgeladen ist. Dort stehen später deine eigenen Aufnahmen.</span></p>'
        + B.geraete({
            "desktop": "pub-site-start-full",
            "tablet": "pub-site-start-tablet",
            "mobile": "pub-site-start-mobile",
        }, gruppe="start_beispiel")
        + '<div class="knopfreihe knopfreihe--mitte mt-7">%s%s</div>'
          % (B.knopf("Beispiel-Website öffnen", "/demo/beispiel-website/", "primaer",
                     "eye", "demo_website_open"),
             B.knopf("Wie der Baukasten funktioniert", "/funktionen/website/", "zweit")),
        art="beige",
    )


def fuer_wen():
    karten = [
        B.karte("Golfpros",
                "Du arbeitest selbstständig, hast eigene Angebote und willst online "
                "so auftreten, wie du unterrichtest.", "customers",
                url="/fuer-golfpros/", link_text="Für Golfpros"),
        B.karte("Golflehrer",
                "Du gibst Unterricht und willst dich nicht mit Technik beschäftigen. "
                "Website pflegen soll fünf Minuten dauern.", "training",
                url="/fuer-golflehrer/", link_text="Für Golflehrer"),
        B.karte("Golfakademien",
                "Mehrere Trainer, mehrere Standorte, gemeinsame Angebote – mit Rollen "
                "und getrennten Kalendern.", "building",
                url="/fuer-golfakademien/", link_text="Für Akademien"),
    ]
    return B.abschnitt(
        B.kopfblock("Für wen", "Gebaut für den Golfbetrieb.",
                    "Der Zuschnitt ist überall derselbe. Was sich unterscheidet, ist, "
                    "welche Bereiche du einschaltest.")
        + B.raster(karten, 3),
        art="weiss",
    )


def preise_kurz():
    return B.abschnitt(
        B.kopfblock("Umfang", "Vier Stufen, ein Produkt.",
                    "Die Stufe legt fest, welche Bereiche du einschalten "
                    "<em>kannst</em>. Was tatsächlich im Menü steht, entscheidest du "
                    "selbst – unter Einstellungen → Tarif.", mitte=True)
        + B.preiskarten()
        + '<div class="hinweiskasten hinweiskasten--sand mt-7" style="max-width:760px;margin-inline:auto">'
          "<h4>Noch kein Selbstabschluss</h4>"
          "<p>Die Stufen sind im CMS hinterlegt und steuern dort den Funktionsumfang. "
          "Eine automatische Abrechnung ist im Produkt nicht enthalten, deshalb steht "
          "hier kein Kaufknopf. Verbindliche Konditionen klären wir im Gespräch – "
          'oder du siehst dir vorher in Ruhe die <a href="/demo/">Demo</a> an.</p></div>',
    )


def faq_kurz():
    paare = [
        ("Brauche ich technische Kenntnisse?",
         "<p>Zum Bedienen nicht. Die Seiten baust du aus fertigen Bausteinen zusammen "
          "und siehst sofort, wie es aussieht. Für die Einrichtung brauchst du einen "
          "Webspace mit PHP – Dateien hochladen, eine Adresse aufrufen, drei Felder "
          "ausfüllen.</p>"),
        ("Kann ich meine eigene Domain verwenden?",
         "<p>Ja. Das CMS erkennt die Domain und liefert die dazugehörige Website aus. "
          "Die Zuordnung steht in den Einstellungen.</p>"),
        ("Was passiert, wenn ich einen Bereich nicht brauche?",
         "<p>Du schaltest ihn ab. Die Daten bleiben vollständig erhalten, der Bereich "
          "verschwindet nur aus dem Menü. Einschalten geht jederzeit wieder.</p>"),
        ("Kann ich das System vorher ausprobieren?",
         "<p>Die <a href='/demo/'>Produktdemo</a> auf dieser Website zeigt alle Bereiche "
          "mit echten Aufnahmen. Für einen eigenen Zugang schreib uns kurz über das "
          "<a href='/kontakt/'>Kontaktformular</a>.</p>"),
    ]
    return B.abschnitt(
        B.kopfblock("Fragen", "Kurz beantwortet.",
                    "Ausführlicher steht es in den "
                    '<a href="/faq/">häufigen Fragen</a>.')
        + B.faq(paare),
        art="beige",
    )


def bauen():
    return {
        "pfad": "/",
        "titel": "GolfProCMS – Das CMS für Golfpros",
        "titel_roh": True,
        "beschreibung": ("GolfProCMS unterstützt Golfpros, Golflehrer und Golfakademien "
                         "bei ihrer digitalen Präsenz: Website, Online-Buchung, "
                         "Kundenakte und Kurse in einer Anwendung."),
        "og_titel": "GolfProCMS – Das CMS für Golfpros",
        "og_text": "Mehr Zeit für deine Schüler. Weniger Zeit für deine Website.",
        "schema": """{"@context":"https://schema.org","@type":"SoftwareApplication",
"name":"GolfProCMS","applicationCategory":"BusinessApplication",
"operatingSystem":"Webbrowser, PHP 8.1+",
"description":"CMS und Verwaltung für Golf Professionals: Website-Baukasten, Online-Buchung, Kundenakte, Kurse, Rechnungen."}""",
        "inhalt": "".join([
            hero(), vertrauen(), problem(), loesung(), module(),
            grosser_screenshot(), wechsel_abschnitt(), kundensicht(),
            beispielwebsite(), fuer_wen(), preise_kurz(), faq_kurz(),
            B.schluss_cta(),
        ]),
    }
