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

    `hell=True` fuer dunkle Flaechen: Stock und Tuch werden weiss, die
    Textzeilen nehmen die Farbe des Untergrunds an.
    """
    stock = "#fffefb" if hell else "var(--gruen)"
    tuch = "#fffefb" if hell else "var(--gruen)"
    zeilen = "var(--gruen-tief)" if hell else "#fffefb"
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


def _mega(punkt, kennung):
    """Das Mega-Menue.

    Links die Eintraege als typografische Liste ohne Symbole, rechts eine
    Vorschau: Wer einen Eintrag ueberfaehrt, sieht die Aufnahme des
    Bereichs, um den es geht. Eine Navigation, die das Produkt zeigt,
    statt es zu beschriften – und die 68 echten Aufnahmen liegen ohnehin da.
    """
    import daten as _D
    spalten, bilder = [], []
    erstes = punkt.get("vorschau")

    for spalte in punkt["spalten"]:
        eintraege = []
        for eintrag in spalte["eintraege"]:
            url, name, zeile, _sym = eintrag[:4]
            bild = eintrag[4] if len(eintrag) > 4 else None
            daten_attr = ' data-vorschau="%s"' % e(bild) if bild else ""
            eintraege.append(
                '<a class="mega__eintrag" href="%s"%s>'
                '<span class="mega__name">%s</span>'
                '<span class="mega__zeile">%s</span></a>'
                % (e(url), daten_attr, e(name), e(zeile))
            )
            if bild and bild not in bilder:
                bilder.append(bild)
        spalten.append(
            '<div class="mega__spalte"><p class="mega__titel">%s</p>%s</div>'
            % (e(spalte["titel"]), "".join(eintraege))
        )

    vorschau = ""
    if erstes:
        tafeln = "".join(
            '<img src="/assets/img/shots/%s-sm.webp" alt="" %s data-bild="%s" '
            'loading="lazy" decoding="async">'
            % (e(b), "" if b == erstes else "hidden", e(b))
            for b in bilder
        )
        beschriftung = "".join(
            '<span data-bildtext="%s"%s>%s</span>'
            % (e(b), "" if b == erstes else " hidden",
               e(_D.BILDER.get(b, (b, "", ""))[0]))
            for b in bilder
        )
        # Unter der Vorschau ein Weg in die Demo: Der Platz waere sonst leer,
        # und wer hier schaut, will ohnehin sehen statt lesen.
        vorschau = (
            '<div class="mega__vorschau">'
            '<div class="mega__rahmen" aria-hidden="true">%s</div>'
            '<p class="mega__bildtext" aria-hidden="true">%s</p>'
            '<a class="mega__weg" href="/demo/" data-event="menu_demo_click">'
            "Alles in der Demo ansehen</a></div>" % (tafeln, beschriftung)
        )

    return (
        '<div class="mega mega--%s" id="%s">'
        '<div class="mega__spalten">%s</div>%s</div>'
        % ("breit" if punkt.get("breit") else "schmal", e(kennung),
           "".join(spalten), vorschau)
    )


def _nav(aktiv):
    teile = []
    for i, punkt in enumerate(D.NAV):
        if punkt["typ"] == "link":
            hier = ' aria-current="page"' if aktiv == punkt["url"] else ""
            teile.append(
                '<div class="nav__punkt">'
                '<a class="nav__knopf" href="%s"%s>%s</a></div>'
                % (e(punkt["url"]), hier, e(punkt["name"]))
            )
        else:
            # Breite Menues bekommen eine eigene Klasse: Sie richten sich
            # am Seitencontainer aus, nicht am eigenen Menuepunkt. Sonst
            # haengt ein 1000px breites Menue ueber einem Punkt, der weit
            # links sitzt, aus dem Bild.
            breit = " nav__punkt--breit" if punkt.get("breit") else ""
            teile.append(
                '<div class="nav__punkt%s" data-offen="nein">'
                '<button class="nav__knopf" type="button" aria-expanded="false" '
                'aria-controls="mega-%d">%s %s</button>%s</div>'
                % (breit, i, e(punkt["name"]), icon("chevron-down", 15),
                   _mega(punkt, "mega-%d" % i))
            )
    return '<nav class="nav" aria-label="Hauptnavigation">%s</nav>' % "".join(teile)


def _mobil():
    """Vollbildmenue fuer kleine Bildschirme.

    Es liegt ueber dem Kopf, nicht darunter, und bringt eine eigene
    Kopfzeile mit Logo und Schliessen mit. Der Grund ist handfest: Der Kopf
    traegt ein backdrop-filter und legt sich sonst ueber den ersten
    Menuepunkt, der dann nicht mehr anklickbar ist.
    """
    gruppen = []
    for i, punkt in enumerate(D.NAV):
        if punkt["typ"] == "link":
            gruppen.append(
                '<div class="mobil__gruppe">'
                '<a class="mobil__schalter" href="%s">%s</a></div>'
                % (e(punkt["url"]), e(punkt["name"]))
            )
            continue
        links = []
        for spalte in punkt["spalten"]:
            for eintrag in spalte["eintraege"]:
                url, name, zeile = eintrag[0], eintrag[1], eintrag[2]
                # Auf dem Telefon traegt die Unterzeile mehr als ein Symbol:
                # Sie sagt, was hinter dem Eintrag steckt.
                links.append(
                    '<a class="mobil__link" href="%s">'
                    '<span class="mobil__link-name">%s</span>'
                    '<span class="mobil__link-zeile">%s</span></a>'
                    % (e(url), e(name), e(zeile))
                )
        gruppen.append(
            '<div class="mobil__gruppe">'
            '<button class="mobil__schalter" type="button" aria-expanded="false" '
            'aria-controls="mobil-%d">%s %s</button>'
            '<div class="mobil__inhalt" id="mobil-%d" data-offen="nein">%s</div></div>'
            % (i, e(punkt["name"]), icon("chevron-down", 19), i, "".join(links))
        )

    return (
        '<div class="mobil" id="mobilmenue" data-offen="nein">'
        '<div class="mobil__kopf">%s'
        '<button class="mobil__zu" type="button" aria-label="Menü schließen">%s</button>'
        "</div>"
        '<div class="mobil__koerper">%s'
        '<div class="mobil__ctas">'
        '<a class="knopf knopf--primaer knopf--breit" href="/demo/" '
        'data-event="hero_demo_click">Demo ansehen</a>'
        '<a class="knopf knopf--zweit knopf--breit" href="/kontakt/" '
        'data-event="trial_click">Persönlich sprechen</a>'
        "</div></div></div>"
        % (_logo(), icon("x", 21), "".join(gruppen))
    )


def kopfzeile(aktiv, band=True):
    teile = []
    if band:
        teile.append(
            '<div class="band">Du willst nicht lesen, sondern sehen? '
            '<a href="/demo/" data-event="band_demo_click">Produktdemo öffnen →</a></div>'
        )
    teile.append(
        '<header class="kopf" data-gescrollt="nein"><div class="kopf__innen">%s%s'
        '<div class="kopf__ctas">'
        '<a class="knopf knopf--zweit knopf--klein" href="/demo/" data-event="hero_demo_click">Demo ansehen</a>'
        '<a class="knopf knopf--primaer knopf--klein" href="/kontakt/" data-event="trial_click">Jetzt testen</a>'
        "</div>"
        '<button class="menue-knopf" type="button" aria-expanded="false" '
        'aria-controls="mobilmenue" aria-label="Menü öffnen">%s</button>'
        "</div></header>%s"
        # Das Mobilmenue steht bewusst NEBEN dem Kopf, nicht darin: Der Kopf
        # traegt ein backdrop-filter, und das macht ihn zum Bezugsrahmen fuer
        # position:fixed. Innerhalb waere das Menue auf Kopfhoehe eingesperrt.
        % (_logo(), _nav(aktiv), icon("menu", 21), _mobil())
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
