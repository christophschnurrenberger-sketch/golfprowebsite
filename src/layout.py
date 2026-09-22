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
        '<meta name="theme-color" content="#12513f">',

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
        '<link rel="preload" href="/assets/fonts/schibsted-grotesk-400-900-latin.woff2" as="font" type="font/woff2" crossorigin>',
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

def zeichen(groesse=28, hell=False):
    """Das Bildzeichen von TeePilot: ein Punkt und eine Linie.

    Der Ball auf dem Tee und die Bahn, die er nimmt. Dieselbe Form liest
    sich auf einer Karte als Standort mit geplanter Route - beides stimmt,
    und beides meint dasselbe.

    Uebernommen aus lib/Marke.php des Produkts, Pfad fuer Pfad. Es nimmt
    die Schriftfarbe an (`currentColor`), damit dasselbe Zeichen hell auf
    Pine und dunkel auf Chalk stehen kann, ohne zweimal im Dokument zu
    liegen. Unter 18 Pixeln nicht verwenden - dann nimmt man das Monogramm.
    """
    del hell  # Die Farbe kommt jetzt vom Elternelement, nicht vom Aufruf.
    return (
        '<svg viewBox="0 0 100 100" fill="none" aria-hidden="true" '
        'focusable="false" width="%d" height="%d" style="display:block">'
        '<circle class="marke__ball" cx="23" cy="71" r="14" fill="currentColor"/>'
        '<path d="M42 59C52 41 65 28 86 20" stroke="currentColor" '
        'stroke-width="9" stroke-linecap="round"/>'
        "</svg>" % (groesse, groesse)
    )


def monogramm(groesse=32):
    """Das TP-Monogramm im abgerundeten Quadrat.

    T und P teilen sich einen Stamm; die Schale des P ist derselbe Bogen
    wie im Bildzeichen. Fuer Favicon und Social-Karte - ueberall dort, wo
    es sehr klein wird und trotzdem erkennbar bleiben muss.
    """
    return (
        '<svg viewBox="0 0 100 100" aria-hidden="true" focusable="false" '
        'width="%d" height="%d" style="display:block">'
        '<rect width="100" height="100" rx="26" fill="#0b2b22"/>'
        '<path d="M39 22V78" stroke="#f6f5f0" stroke-width="11" '
        'stroke-linecap="round" fill="none"/>'
        '<path d="M20 22H39" stroke="#f6f5f0" stroke-width="11" '
        'stroke-linecap="round" fill="none"/>'
        '<path d="M39 22C66 22 80 30 80 39.5C80 49 66 56 39 56" '
        'stroke="#c3e35c" stroke-width="11" stroke-linecap="round" fill="none"/>'
        "</svg>" % (groesse, groesse)
    )


def _logo(klasse="", hell=False, groesse=28):
    """Wortmarke mit Bildzeichen.

    Abstand 0,3 x Zeichenhoehe, Schriftgrad 0,78 x, Gewicht 700, Laufweite
    eng - so steht es im Markenhandbuch, und so muss es auch hier stehen,
    sonst weicht die Website vom Handbuch ab. Ein Wort in einem Gewicht:
    Die frueher zweigeteilte Marke („GolfPro" fett, „CMS" leicht) gibt es
    nicht mehr, weil „TeePilot" ein Wort ist.
    """
    del hell
    return (
        '<a class="logo %s" href="/" aria-label="%s \u2013 zur Startseite">'
        '<span class="logo__zeichen">%s</span>'
        '<span class="logo__wort">%s</span>'
        "</a>" % (klasse, e(D.MARKE), zeichen(groesse), e(D.MARKE))
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


def sticky_cta(text="TeePilot selbst ansehen", knopf="Demo", url="/demo/"):
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
