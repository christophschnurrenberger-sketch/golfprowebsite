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
    tiefe = seite["pfad"].strip("/").count("/") + 1 if seite["pfad"] != "/" else 0
    wurzel = "../" * tiefe if tiefe else "./"

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
        '<link rel="preload" href="%sassets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>' % wurzel,
        '<link rel="stylesheet" href="%sassets/css/schriften.css">' % wurzel,
        '<link rel="stylesheet" href="%sassets/css/site.css">' % wurzel,
        '<link rel="icon" href="%sassets/img/favicon.svg" type="image/svg+xml">' % wurzel,
        '<link rel="sitemap" type="application/xml" href="/sitemap.xml">',
    ]

    if seite.get("schema"):
        zeilen.append('<script type="application/ld+json">%s</script>' % seite["schema"])

    zeilen += ["</head>", "<body>"]
    return "\n".join(zeilen)


# ----------------------------------------------------------------- Kopfzeile --

def _logo(klasse=""):
    return (
        '<a class="logo %s" href="/" aria-label="%s – zur Startseite">'
        '<span class="logo__zeichen" aria-hidden="true">%s</span>'
        "<span>%s</span></a>"
        % (klasse, e(D.MARKE), icon("flag", 17, 2), e(D.MARKE))
    )


def _mega(punkt):
    spalten = []
    for spalte in punkt["spalten"]:
        eintraege = []
        for url, name, zeile, sym in spalte["eintraege"]:
            eintraege.append(
                '<a class="mega__eintrag" href="%s">'
                '<span class="mega__symbol">%s</span>'
                '<span><span class="mega__name">%s</span>'
                '<span class="mega__zeile">%s</span></span></a>'
                % (e(url), icon(sym, 17), e(name), e(zeile))
            )
        spalten.append(
            '<div><p class="mega__titel">%s</p>%s</div>'
            % (e(spalte["titel"]), "".join(eintraege))
        )
    return (
        '<div class="mega mega--%s"><div class="mega__spalten">%s</div></div>'
        % ("breit" if punkt.get("breit") else "schmal", "".join(spalten))
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
            teile.append(
                '<div class="nav__punkt" data-offen="nein">'
                '<button class="nav__knopf" type="button" aria-expanded="false" '
                'aria-controls="mega-%d">%s %s</button>%s</div>'
                % (i, e(punkt["name"]), icon("chevron-down", 15), _mega(punkt))
            )
    return '<nav class="nav" aria-label="Hauptnavigation">%s</nav>' % "".join(teile)


def _mobil():
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
            for url, name, zeile, sym in spalte["eintraege"]:
                links.append(
                    '<a class="mobil__link" href="%s">%s<span>%s</span></a>'
                    % (e(url), icon(sym, 17), e(name))
                )
        gruppen.append(
            '<div class="mobil__gruppe">'
            '<button class="mobil__schalter" type="button" aria-expanded="false" '
            'aria-controls="mobil-%d">%s %s</button>'
            '<div class="mobil__inhalt" id="mobil-%d" data-offen="nein">%s</div></div>'
            % (i, e(punkt["name"]), icon("chevron-down", 19), i, "".join(links))
        )

    return (
        '<div class="mobil" id="mobilmenue" data-offen="nein">%s'
        '<div class="mobil__ctas">'
        '<a class="knopf knopf--primaer knopf--breit" href="/demo/" data-event="hero_demo_click">%s Demo ansehen</a>'
        '<a class="knopf knopf--zweit knopf--breit" href="/kontakt/" data-event="trial_click">GolfProCMS testen</a>'
        "</div></div>"
        % ("".join(gruppen), icon("play", 17))
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
        "</div>%s</header>"
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
        '<p class="fuss__zeile">%s Eine Anwendung für Website, Buchung, Kunden '
        "und Verkauf – auf einem gewöhnlichen Webhosting-Paket.</p></div>"
        "%s</div>"
        '<div class="fuss__unten">'
        "<span>© %s %s</span>"
        "<span>"
        '<a href="/impressum/">Impressum</a> · '
        '<a href="/datenschutz/">Datenschutz</a>'
        "</span></div>"
        "</div></footer>"
        % (_logo(), e(D.TAGLINE), "".join(spalten), 2026, e(D.MARKE))
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
