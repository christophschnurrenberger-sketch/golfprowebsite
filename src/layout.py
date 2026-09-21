# -*- coding: utf-8 -*-
"""Rahmen jeder Seite: Kopf, Navigation, Fuss, Dokumentkopf."""

import html
import daten as D
from icons import icon


def e(text):
    """Text fuer HTML entschaerfen."""
    return html.escape(str(text), quote=True)


def app_ziel(rueckfall="/demo/"):
    """Wohin ein „CMS oeffnen“-Knopf zeigt.

    Solange keine laufende Installation eingetragen ist, fuehrt er in die
    Demo dieser Website – nicht auf einen Login, den es nicht gibt.
    """
    return D.APP_BASIS + "/login.php" if D.APP_BASIS else rueckfall


def demo_ziel(rueckfall="/demo/"):
    return D.DEMO_ZUGANG or rueckfall


# ------------------------------------------------------------ Dokumentkopf --

def kopf_html(seite):
    # Die Überschrift darf lang sein, der Suchmaschinen-Titel nicht.
    titel = seite.get("seo_titel") or seite["titel"]
    voll = titel if seite.get("titel_roh") else "%s – %s" % (titel, D.MARKE)
    url = D.BASIS_URL.rstrip("/") + seite["pfad"]
    og_bild = D.BASIS_URL.rstrip("/") + "/assets/img/og.png"

    zeilen = [
        "<!DOCTYPE html>",
        '<html lang="de">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>%s</title>" % e(voll),
        '<meta name="description" content="%s">' % e(seite["beschreibung"]),
        '<link rel="canonical" href="%s">' % e(url),
        '<meta name="robots" content="%s">' % ("noindex, follow" if seite.get("noindex") else "index, follow"),
        '<meta name="theme-color" content="#0d6b4f">',

        # Open Graph / Social
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="%s">' % e(D.MARKE),
        '<meta property="og:locale" content="de_DE">',
        '<meta property="og:title" content="%s">' % e(seite.get("og_titel") or voll),
        '<meta property="og:description" content="%s">' % e(seite.get("og_text") or seite["beschreibung"]),
        '<meta property="og:url" content="%s">' % e(url),
        '<meta property="og:image" content="%s">' % e(og_bild),
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % e(seite.get("og_titel") or voll),
        '<meta name="twitter:description" content="%s">' % e(seite.get("og_text") or seite["beschreibung"]),
        '<meta name="twitter:image" content="%s">' % e(og_bild),

        # Schriften liegen auf dem eigenen Server – kein Aufruf zu Google.
        # Grund: LG Muenchen I, 20.01.2022, Az. 3 O 17493/20.
        '<link rel="preload" href="/assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>',
        '<link rel="stylesheet" href="/assets/css/schriften.css">',
        '<link rel="stylesheet" href="/assets/css/site.css">',
        '<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">',
        '<link rel="sitemap" type="application/xml" href="/sitemap.xml">',
    ]

    if seite.get("schema"):
        zeilen.append('<script type="application/ld+json">%s</script>' % seite["schema"])

    zeilen += ["</head>", "<body>"]
    return "\n".join(zeilen)


# ----------------------------------------------------------------- Kopfzeile --

def zeichen(groesse=30, hell=False):
    """Das Bildzeichen: ein Fahnenstock, dessen Tuch ein Inhaltsblock ist.

    Zwei Textzeilen im Fahnentuch statt eines Wimpels – Golf und CMS in
    einem Zeichen, statt einer Fahne neben einem Zahnrad. Die Sandlinie
    unten ist der Boden, in dem der Stock steckt; sie ist die einzige
    Stelle, an der die Akzentfarbe im Logo vorkommt.

    Stock und Tuch nehmen die Schriftfarbe an, die Textzeilen darin eine
    eigene Variable. So kann dasselbe Zeichen hell oder dunkel stehen, ohne
    dass es zweimal im Dokument liegt - der Vorhang faerbt es um, waehrend
    er faellt. `hell=True` setzt die Farben fest, fuer Flaechen ohne CSS.
    """
    stock = "#fffefb" if hell else "currentColor"
    tuch = "#fffefb" if hell else "currentColor"
    zeilen = "var(--gruen-tief)" if hell else "var(--zeichen-innen, #fffefb)"
    h = round(groesse * 32 / 30)
    return (
        '<svg width="%d" height="%d" viewBox="0 0 30 32" fill="none" '
        'aria-hidden="true" focusable="false">'
        '<rect x="11" y="3.5" width="15" height="11.5" rx="1.6" fill="%s"/>'
        '<path d="M14.6 7.8h7.8M14.6 11.2h4.8" stroke="%s" stroke-width="1.7" '
        'stroke-linecap="round"/>'
        '<path d="M10 2.5v26.5" stroke="%s" stroke-width="2.5" stroke-linecap="round"/>'
        '<path d="M4.5 29h11" stroke="var(--sand)" stroke-width="2.4" stroke-linecap="round"/>'
        "</svg>" % (groesse, h, tuch, zeilen, stock)
    )


def _logo(klasse="", hell=False, groesse=27):
    """Wortmarke mit Bildzeichen.

    „GolfPro" traegt das Gewicht, „CMS" steht leichter daneben: Der Betrieb
    ist die Hauptsache, die Software das Werkzeug. Deshalb auch kein
    abgerundetes Quadrat um das Zeichen – das ist die Form eines
    App-Symbols, nicht die einer Marke.
    """
    return (
        '<a class="logo %s" href="/" aria-label="%s – zur Startseite">'
        '<span class="logo__zeichen">%s</span>'
        '<span class="logo__wort">GolfPro<span class="logo__leicht">CMS</span></span>'
        "</a>" % (klasse, e(D.MARKE), zeichen(groesse, hell))
    )


def _nav(aktiv):
    """Die Leiste im Kopf.

    Kein Klappmenue mehr. Wer auf einen Punkt tippt, bekommt den Vorhang -
    die ganze Seite. Dreimal stand hier eine weisse Box mit einer Nutzlast
    rechts: ein Bildschirmfoto, ein Ausschnitt daraus, ein Grundriss. Jedes
    Mal war die Nutzlast das, was getauscht wurde, und jedes Mal blieb der
    Kasten. Der Kasten war das Problem.
    """
    teile = []
    for i, punkt in enumerate(D.NAV):
        if punkt["typ"] == "link":
            hier = ' aria-current="page"' if aktiv == punkt["url"] else ""
            teile.append('<a class="nav__knopf" href="%s"%s>%s</a>'
                         % (e(punkt["url"]), hier, e(punkt["name"])))
        else:
            teile.append(
                '<button class="nav__knopf nav__knopf--vorhang" type="button" '
                'aria-expanded="false" aria-controls="vorhang" '
                'data-teil="%d">%s</button>' % (i, e(punkt["name"]))
            )
    return '<nav class="nav" aria-label="Hauptnavigation">%s</nav>' % "".join(teile)


def _vorhang(aktiv):
    """Der Vorhang: die Navigation als ganze Seite, nicht als Klappbox.

    Tiefes Gruen ueber alles, das Inhaltsverzeichnis gross gesetzt,
    durchnummeriert, mit Haarlinien getrennt - eine Inhaltsseite, keine
    Oberflaeche.
    Auf grossen Schirmen zeigt der Vorhang einen Abschnitt, den der Kopf
    anwaehlt. Auf kleinen zeigt er alle untereinander - dasselbe Bauteil,
    zwei Groessen. Vorher waren es zwei Bauteile mit zwei Fehlerquellen.

    Er liegt bewusst NEBEN dem Kopf, nicht darin: Der Kopf traegt ein
    backdrop-filter, und das macht ihn zum Bezugsrahmen fuer
    position:fixed. Innerhalb waere der Vorhang auf Kopfhoehe eingesperrt.
    """
    teile = []
    for i, punkt in enumerate(D.NAV):
        if punkt["typ"] == "link":
            continue
        zeilen = []
        for n, (url, name, satz) in enumerate(punkt["eintraege"], 1):
            hier = ' aria-current="page"' if aktiv == url else ""
            zeilen.append(
                '<li class="vorhang__posten" style="--i:%d">'
                '<a class="vorhang__zeile" href="%s"%s>'
                '<span class="vorhang__nr">%02d</span>'
                '<span class="vorhang__name">%s</span>'
                '<span class="vorhang__satz">%s</span></a></li>'
                % (n, e(url), hier, n, e(name), e(satz))
            )
        teile.append(
            '<section class="vorhang__teil" data-teil="%d" aria-label="%s">'
            '<p class="vorhang__marke">%s</p>'
            '<ol class="vorhang__index">%s</ol>'
            '<p class="vorhang__fuss">%s</p>'
            "</section>"
            % (i, e(punkt["name"]), e(punkt["name"]), "".join(zeilen),
               e(punkt["satz"]))
        )

    # Die Punkte ohne eigenen Abschnitt fehlen auf dem Telefon sonst ganz:
    # Dort ist der Vorhang das einzige Menue.
    einzeln = [p for p in D.NAV if p["typ"] == "link"]
    if einzeln:
        zeilen = "".join(
            '<li class="vorhang__posten" style="--i:%d">'
            '<a class="vorhang__zeile" href="%s"><span class="vorhang__nr">%02d</span>'
            '<span class="vorhang__name">%s</span></a></li>'
            % (n, e(p["url"]), n, e(p["name"]))
            for n, p in enumerate(einzeln, 1)
        )
        teile.append(
            '<section class="vorhang__teil vorhang__teil--rest" aria-label="Mehr">'
            '<p class="vorhang__marke">Mehr</p>'
            '<ol class="vorhang__index">%s</ol></section>' % zeilen
        )

    return (
        '<div class="vorhang" id="vorhang" data-offen="nein" data-alle="nein">'
        '<div class="vorhang__koerper">%s'
        '<div class="vorhang__ctas">'
        '<a class="knopf knopf--hell knopf--breit" href="/demo/" '
        'data-event="hero_demo_click">Demo ansehen</a>'
        '<a class="knopf knopf--rand-hell knopf--breit" href="/kontakt/" '
        'data-event="trial_click">Persönlich sprechen</a>'
        "</div></div></div>" % "".join(teile)
    )


def kopfzeile(aktiv, band=True):
    teile = []
    if band:
        teile.append(
            '<div class="band">Du willst nicht lesen, sondern sehen? '
            '<a href="/demo/" data-event="band_demo_click">Produktdemo öffnen →</a></div>'
        )
    teile.append(
        '<header class="kopf" data-gescrollt="nein" data-vorhang="nein"><div class="kopf__innen">%s%s'
        '<div class="kopf__ctas">'
        '<a class="knopf knopf--zweit knopf--klein" href="/demo/" data-event="hero_demo_click">Demo ansehen</a>'
        '<a class="knopf knopf--primaer knopf--klein" href="/kontakt/" data-event="trial_click">Jetzt testen</a>'
        "</div>"
        '<button class="menue-knopf" type="button" aria-expanded="false" '
        'aria-controls="vorhang" aria-label="Menü">'
        '<span class="menue-knopf__auf">%s</span>'
        '<span class="menue-knopf__zu">%s</span></button>'
        "</div></header>%s"
        # Der Vorhang steht bewusst NEBEN dem Kopf, nicht darin: Der Kopf
        # traegt ein backdrop-filter, und das macht ihn zum Bezugsrahmen fuer
        # position:fixed. Innerhalb waere er auf Kopfhoehe eingesperrt.
        % (_logo(), _nav(aktiv), icon("menu", 21), icon("x", 21),
           _vorhang(aktiv))
    )
    return "".join(teile)


# ------------------------------------------------------------- Brotkrumen --

def krumen(pfade):
    """pfade: Liste aus (url, name); der letzte Eintrag ist die aktuelle Seite."""
    if not pfade:
        return ""
    stuecke = []
    for i, (url, name) in enumerate(pfade):
        letzter = i == len(pfade) - 1
        if letzter:
            stuecke.append('<li><span aria-current="page">%s</span></li>' % e(name))
        else:
            stuecke.append('<li><a href="%s">%s</a></li>' % (e(url), e(name)))
    return (
        '<nav class="krumen" aria-label="Brotkrumen"><div class="huelle">'
        "<ol>%s</ol></div></nav>" % "".join(stuecke)
    )


# ----------------------------------------------------------------- Fusszeile --

def fusszeile():
    spalten = []
    for titel, links in D.FUSS:
        eintraege = "".join('<li><a href="%s">%s</a></li>' % (e(u), e(n)) for u, n in links)
        spalten.append("<div><h4>%s</h4><ul>%s</ul></div>" % (e(titel), eintraege))

    return (
        '<footer class="fuss"><div class="huelle">'
        '<div class="fuss__raster">'
        '<div class="fuss__marke">%s'
        '<p class="fuss__zeile">%s Website, Buchung, Kunden und Verkauf in '
        "einer Anwendung. Läuft auf einem gewöhnlichen Webhosting-Paket.</p></div>"
        "%s</div>"
        '<div class="fuss__unten">'
        "<span>© %s %s</span>"
        "<span>"
        '<a href="/impressum/">Impressum</a> · '
        '<a href="/datenschutz/">Datenschutz</a>'
        "</span></div>"
        "</div></footer>"
        % (_logo(hell=True), e(D.TAGLINE), "".join(spalten), 2026, e(D.MARKE))
    )


def sticky_cta(text="GolfProCMS selbst ansehen", knopf="Demo", url="/demo/"):
    return (
        '<div class="sticky-cta" data-sichtbar="nein">'
        '<span class="sticky-cta__text">%s</span>'
        '<a class="knopf knopf--hell knopf--klein" href="%s" data-event="sticky_cta_click">%s</a>'
        '<button class="sticky-cta__zu" type="button" aria-label="Hinweis schließen">%s</button>'
        "</div>" % (e(text), e(url), e(knopf), icon("x", 16))
    )


def fuss_html(mit_sticky=True):
    teile = []
    if mit_sticky:
        teile.append(sticky_cta())
    teile.append(fusszeile())
    teile.append('<script src="/assets/js/site.js" defer></script>')
    teile.append("</body>\n</html>")
    return "\n".join(teile)
