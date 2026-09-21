# -*- coding: utf-8 -*-
"""
Wiederverwendbare Abschnitte.

Jeder Baustein gibt HTML zurueck. Keiner kennt eine Seite; zusammengesetzt
wird in src/seiten/.
"""

import daten as D
from icons import icon
from layout import e


# ------------------------------------------------------------- Screenshots --

def bild_daten(schluessel):
    name, bereich, zeile = D.BILDER.get(
        schluessel, (schluessel, "", "Aufnahme aus GolfProCMS")
    )
    return name, bereich, zeile


def rahmen(schluessel, adresse=None, klein=False, lazy=True, klasse=""):
    """Ein Screenshot im Browserrahmen.

    Der Rahmen ist kein Schmuck: Er sagt dem Auge in einem Sechstelsekunde,
    dass hier Software zu sehen ist und kein Bild von Software.
    """
    name, _bereich, zeile = bild_daten(schluessel)
    datei = "/assets/img/shots/%s%s.webp" % (schluessel, "-sm" if klein else "")
    if adresse is None:
        adresse = ("golfprocms · " + name) if schluessel.startswith("app-") \
                  else "golf-academy-bergmann.de"
    return (
        '<figure class="rahmen %s" style="margin:0">'
        '<div class="rahmen__leiste">'
        '<span class="rahmen__ampel" aria-hidden="true"><i></i><i></i><i></i></span>'
        '<span class="rahmen__adresse">%s</span></div>'
        '<img class="rahmen__bild" src="%s" alt="%s: %s" %s width="1600" height="1000">'
        "</figure>"
        % (klasse, e(adresse), e(datei), e(name), e(zeile),
           'loading="lazy" decoding="async"' if lazy else 'fetchpriority="high" decoding="async"')
    )


def bildunter(text, etikett=None):
    marke = ""
    if etikett:
        marke = '<span class="marke-etikett marke-etikett--grau">%s</span>' % e(etikett)
    return '<figcaption class="bildunter">%s<span>%s</span></figcaption>' % (marke, e(text))


def screenshot_block(schluessel, etikett="Echte Aufnahme", klein=False, lazy=True):
    """Screenshot plus Bildunterschrift – die uebliche Kombination."""
    name, _b, zeile = bild_daten(schluessel)
    return (
        '<div>%s%s</div>'
        % (rahmen(schluessel, klein=klein, lazy=lazy),
           bildunter("%s – %s" % (name, zeile), etikett))
    )


# ------------------------------------------------------------- Kopfbereiche --

def kopfblock(vorzeile, titel, fuehrung="", mitte=False, stufe=2, extra=""):
    teile = ['<div class="kopfblock%s">' % (" kopfblock--mitte" if mitte else "")]
    if vorzeile:
        teile.append('<p class="vorzeile">%s</p>' % e(vorzeile))
    teile.append("<h%d>%s</h%d>" % (stufe, titel, stufe))
    if fuehrung:
        teile.append('<p class="fuehrung">%s</p>' % fuehrung)
    if extra:
        teile.append(extra)
    teile.append("</div>")
    return "".join(teile)


def seitenkopf(vorzeile, titel, fuehrung, knoepfe="", visual="", kompakt=False):
    """Der Kopf einer Unterseite.

    `kompakt` ist fuer Seiten gedacht, deren Hauptsache sofort sichtbar sein
    soll – die Demo ist kein Nebenelement, sie darf nicht unter einer
    bildschirmhohen Ueberschrift verschwinden.
    """
    if kompakt:
        return (
            '<section class="kopf-kompakt"><div class="huelle">'
            '<div class="kopf-kompakt__raster">'
            '<div><p class="vorzeile">%s</p><h1>%s</h1>'
            '<p class="fuehrung mt-4">%s</p></div>'
            "%s</div></div></section>"
            % (e(vorzeile), titel, fuehrung,
               ('<div class="knopfreihe">%s</div>' % knoepfe) if knoepfe else "<div></div>")
        )
    if visual:
        return (
            '<section class="abschnitt abschnitt--eng"><div class="huelle">'
            '<div class="hero__raster"><div>%s%s</div><div>%s</div></div>'
            "</div></section>"
            % (kopfblock(vorzeile, titel, fuehrung, stufe=1),
               ('<div class="knopfreihe mt-6">%s</div>' % knoepfe) if knoepfe else "",
               visual)
        )
    return (
        '<section class="abschnitt abschnitt--eng"><div class="huelle">%s%s</div></section>'
        % (kopfblock(vorzeile, titel, fuehrung, stufe=1),
           ('<div class="knopfreihe mt-6">%s</div>' % knoepfe) if knoepfe else "")
    )


# ------------------------------------------------------------------ Knoepfe --

def knopf(text, url, art="primaer", sym=None, event=None, klasse=""):
    s = (icon(sym, 17) + " ") if sym else ""
    ev = ' data-event="%s"' % e(event) if event else ""
    return '<a class="knopf knopf--%s %s" href="%s"%s>%s%s</a>' % (
        art, klasse, e(url), ev, s, e(text))


def pfeil_link(text, url, event=None):
    ev = ' data-event="%s"' % e(event) if event else ""
    return '<a class="pfeil" href="%s"%s>%s</a>' % (e(url), ev, e(text))


# ------------------------------------------------------------------- Karten --

def karte(titel, text, sym=None, url=None, link_text="Mehr erfahren", sand=False,
          etikett=None):
    inhalt = []
    if sym:
        inhalt.append('<span class="karte__symbol%s">%s</span>'
                      % (" karte__symbol--sand" if sand else "", icon(sym, 21)))
    kopf = e(titel)
    if etikett:
        kopf += ' <span class="marke-etikett marke-etikett--sand">%s</span>' % e(etikett)
    inhalt.append("<h3>%s</h3>" % kopf)
    inhalt.append("<p>%s</p>" % text)
    if url:
        inhalt.append('<p class="karte__fuss"><span class="pfeil">%s</span></p>' % e(link_text))
        return '<a class="karte karte--link" href="%s">%s</a>' % (e(url), "".join(inhalt))
    return '<div class="karte">%s</div>' % "".join(inhalt)


def raster(karten, spalten=3, klasse=""):
    return '<div class="raster raster--%d %s">%s</div>' % (spalten, klasse, "".join(karten))


# ---------------------------------------------------------------- Abschnitt --

def abschnitt(inhalt, art="", huelle="huelle", zeigen=True, ident=None):
    klassen = "abschnitt"
    if art:
        klassen += " abschnitt--" + art
    if zeigen:
        klassen += " zeigen"
    kennung = ' id="%s"' % e(ident) if ident else ""
    return '<section class="%s"%s><div class="%s">%s</div></section>' % (
        klassen, kennung, huelle, inhalt)


# ------------------------------------------------------------ Vertrauensband --

def vertrauen():
    punkte = [
        ("shield", "Deine Daten auf deinem Hosting",
         "PHP und eine Datenbank, sonst nichts. Keine fremde Cloud dazwischen."),
        ("smartphone", "Am Telefon bedienbar",
         "Die Oberfläche ist für kleine Bildschirme gebaut, nicht nur verkleinert."),
        ("lock", "Schriften im eigenen Haus",
         "Kein Aufruf zu Google-Servern. Die Websitestatistik zählt ohne Cookies."),
    ]
    inhalt = "".join(
        '<div class="vertrauen__punkt">%s<span><b>%s</b><span>%s</span></span></div>'
        % (icon(s, 20), e(t), e(z)) for s, t, z in punkte
    )
    return '<div class="vertrauen">%s</div>' % inhalt


# ------------------------------------------------------------------ Ablauf --

def ablauf(schritte):
    """schritte: Liste aus (titel, text)."""
    teile = "".join(
        '<div class="ablauf__schritt"><h4>%s</h4><p>%s</p></div>' % (e(t), x)
        for t, x in schritte
    )
    return '<div class="ablauf">%s</div>' % teile


# ------------------------------------------------------- Vorher / Nachher --

def gegenueber(heute, mit_cms, kopf_heute="Ein typischer Dienstag",
               kopf_cms="Mit GolfProCMS"):
    def liste(punkte, sym):
        return "".join('<li>%s<span>%s</span></li>' % (icon(sym, 16), e(p)) for p in punkte)

    return (
        '<div class="gegen">'
        '<div class="gegen__spalte gegen__spalte--heute">'
        '<p class="gegen__kopf">%s</p><ul class="gegen__liste">%s</ul></div>'
        '<div class="gegen__pfeil">%s</div>'
        '<div class="gegen__spalte gegen__spalte--cms">'
        '<p class="gegen__kopf">%s</p><ul class="gegen__liste">%s</ul></div>'
        "</div>"
        % (e(kopf_heute), liste(heute, "x"), icon("arrow-right", 26),
           e(kopf_cms), liste(mit_cms, "check"))
    )


# ------------------------------------------------------------- Feature-Wechsel --

def wechsel(eintraege, gruppe="feature_wechsel"):
    """eintraege: Liste aus (schluessel, name, zeile, bild).

    Links die Liste, rechts der Screenshot. Beim Wechseln bleibt der Rahmen
    stehen und nur das Bild tauscht – das ist ruhiger als ein Sprung.
    """
    knoepfe, tafeln = [], []
    for i, (schluessel, name, zeile, bild) in enumerate(eintraege):
        knoepfe.append(
            '<button class="wechsel__knopf" type="button" role="tab" '
            'data-reiter="%s" aria-selected="%s">'
            '<span class="wechsel__nr">%02d</span>'
            '<span class="wechsel__name">%s</span>'
            '<span class="wechsel__zeile">%s</span></button>'
            % (e(schluessel), "true" if i == 0 else "false", i + 1, e(name), e(zeile))
        )
        tafeln.append(
            '<div class="wechsel__tafel" data-tafel="%s" data-aktiv="%s" role="tabpanel">%s</div>'
            % (e(schluessel), "ja" if i == 0 else "nein", screenshot_block(bild))
        )
    return (
        '<div class="wechsel" data-reitergruppe="%s">'
        '<div class="wechsel__liste" role="tablist" aria-label="Bereiche">%s</div>'
        '<div class="wechsel__buehne">%s</div></div>'
        % (e(gruppe), "".join(knoepfe), "".join(tafeln))
    )


# ----------------------------------------------------------- Interaktive Demo --

def demo_tafel(eintraege, gruppe="product_demo_start", start=None):
    """eintraege: Liste aus dict(key, name, sym, bild, titel, text, punkte, cta).

    Links/oben die CMS-Navigation als Reiter, in der Mitte die Aufnahme,
    rechts der erklaerende Kasten.
    """
    reiter, tafeln = [], []
    erste = start or eintraege[0]["key"]
    for eintrag in eintraege:
        aktiv = eintrag["key"] == erste
        reiter.append(
            '<button type="button" role="tab" data-reiter="%s" aria-selected="%s">%s %s</button>'
            % (e(eintrag["key"]), "true" if aktiv else "false",
               icon(eintrag["sym"], 15), e(eintrag["name"]))
        )
        punkte = "".join(
            "<li>%s<span>%s</span></li>" % (icon("check", 15), e(p))
            for p in eintrag.get("punkte", [])
        )
        _n, _b, zeile = bild_daten(eintrag["bild"])
        tafeln.append(
            '<div class="demo__tafel" data-tafel="%s" data-aktiv="%s" role="tabpanel" '
            'aria-label="%s">'
            '<div class="demo__koerper">'
            '<div class="demo__buehne"><img src="/assets/img/shots/%s.webp" alt="%s" '
            'loading="lazy" decoding="async" width="1600" height="1000">'
            '<div class="demo__laden" data-an="nein"><span class="kreisel"></span></div></div>'
            '<aside class="demo__info"><h3>%s</h3><p>%s</p>'
            '<ul class="demo__punkte">%s</ul>'
            '<div class="demo__fuss">%s</div></aside>'
            "</div></div>"
            % (e(eintrag["key"]), "ja" if aktiv else "nein", e(eintrag["name"]),
               e(eintrag["bild"]), e("%s – %s" % (eintrag["name"], zeile)),
               e(eintrag["titel"]), eintrag["text"], punkte,
               eintrag.get("cta", ""))
        )
    return (
        '<div class="demo" data-reitergruppe="%s" data-start="%s">'
        '<div class="demo__leiste">'
        '<div class="demo__reiter" role="tablist" aria-label="Bereiche im CMS">%s</div>'
        '<span class="marke-etikett">Echte Aufnahmen</span></div>'
        "%s</div>"
        % (e(gruppe), e(erste), "".join(reiter), "".join(tafeln))
    )


# ---------------------------------------------------------- Geraetewechsler --

def geraete(bilder, gruppe="beispiel", adresse="golf-academy-bergmann.de"):
    """bilder: dict mit desktop/tablet/mobile -> Bildschluessel."""
    knoepfe = []
    for kennung, name, sym in (("desktop", "Desktop", "monitor"),
                               ("tablet", "Tablet", "tablet"),
                               ("mobile", "Smartphone", "smartphone")):
        knoepfe.append(
            '<button type="button" data-geraet-knopf="%s" aria-selected="%s">%s %s</button>'
            % (kennung, "true" if kennung == "desktop" else "false", icon(sym, 15), e(name))
        )

    tafeln = []
    for kennung in ("desktop", "tablet", "mobile"):
        schluessel = bilder[kennung]
        _n, _b, zeile = bild_daten(schluessel.replace("-tablet", "").replace("-mobile", ""))
        tafeln.append(
            '<div data-geraet-bild="%s"%s>'
            '<figure class="rahmen" style="margin:0">'
            '<div class="rahmen__leiste">'
            '<span class="rahmen__ampel" aria-hidden="true"><i></i><i></i><i></i></span>'
            '<span class="rahmen__adresse">%s</span></div>'
            '<img class="rahmen__bild" src="/assets/img/shots/%s.webp" alt="%s" '
            'loading="lazy" decoding="async"></figure></div>'
            % (kennung, "" if kennung == "desktop" else " hidden",
               e(adresse), e(schluessel), e(zeile))
        )

    return (
        '<div data-geraetegruppe="%s">'
        '<div class="knopfreihe mb-5" style="justify-content:center">'
        '<div class="geraete" role="tablist" aria-label="Ansicht wählen">%s</div></div>'
        '<div class="buehne"><div class="buehne__halter" data-geraet="desktop">%s</div></div>'
        "</div>"
        % (e(gruppe), "".join(knoepfe), "".join(tafeln))
    )


# --------------------------------------------------------------------- FAQ --

def faq(paare, offen_erste=False):
    teile = []
    for i, (frage, antwort) in enumerate(paare):
        auf = " open" if (offen_erste and i == 0) else ""
        teile.append(
            "<details%s><summary>%s</summary>"
            '<div class="faq__antwort">%s</div></details>' % (auf, e(frage), antwort)
        )
    return '<div class="faq">%s</div>' % "".join(teile)


def faq_schema(paare):
    """FAQPage als JSON-LD – hilft der Darstellung in Suchergebnissen."""
    import json
    daten_ = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f,
             "acceptedAnswer": {"@type": "Answer",
                                "text": __import__("re").sub(r"<[^>]+>", "", a)}}
            for f, a in paare
        ],
    }
    return json.dumps(daten_, ensure_ascii=False)


# ------------------------------------------------------------------ Tabelle --

def tabelle(kopf, zeilen):
    kopf_html = "".join("<th>%s</th>" % e(k) for k in kopf)
    koerper = "".join(
        "<tr>%s</tr>" % "".join("<td>%s</td>" % z for z in zeile) for zeile in zeilen
    )
    return (
        '<div class="tabellenhuelle"><table class="tabelle">'
        "<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>"
        % (kopf_html, koerper)
    )


# ------------------------------------------------------------------- Preise --

def preiskarten():
    karten = []
    for t in D.TARIFE:
        punkte = "".join(
            "<li>%s<span>%s</span></li>" % (icon("check", 15), e(p))
            for p in t["enthalten"]
        )
        fahne = '<span class="preis__fahne">Meist gewählt</span>' if t.get("hervor") else ""
        karten.append(
            '<div class="preis%s">%s'
            '<p class="preis__name">%s</p>'
            '<p class="preis__zeile">%s</p>'
            '<p class="preis__betrag"><span class="preis__zahl">%d&nbsp;€</span>'
            '<span class="preis__takt">/ Monat</span></p>'
            '<ul class="preis__liste">%s</ul>'
            '<a class="knopf knopf--%s" href="/kontakt/?anliegen=demo" '
            'data-event="pricing_cta_click">Demo anfragen</a></div>'
            % (" preis--hervor" if t.get("hervor") else "", fahne,
               e(t["name"]), e(t["zeile"]), t["preis"], punkte,
               "primaer" if t.get("hervor") else "zweit")
        )
    return '<div class="preise">%s</div>' % "".join(karten)


# ------------------------------------------------------------- Abschluss-CTA --

def schluss_cta(titel=None, text=None, primaer=("Produktdemo ansehen", "/demo/"),
                zweit=("Persönliche Demo anfragen", "/kontakt/")):
    titel = titel or "Dein Golfbusiness.<br>Deine Website.<br>Dein GolfProCMS."
    text = text or ("Schau dir das System selbst an und entscheide, ob es zu deinem "
                    "Alltag als Golfpro passt. Ohne Anmeldung, ohne Termin.")
    return abschnitt(
        '<div class="kopfblock kopfblock--mitte" style="max-width:820px">'
        '<h2 style="font-size:clamp(34px,5.4vw,64px)">%s</h2>'
        '<p class="fuehrung mt-5">%s</p>'
        '<div class="knopfreihe knopfreihe--mitte mt-7">'
        '<a class="knopf knopf--hell" href="%s" data-event="footer_demo_click">%s %s</a>'
        '<a class="knopf knopf--rand-hell" href="%s" data-event="footer_contact_click">%s</a>'
        "</div></div>"
        % (titel, e(text), e(primaer[1]), icon("play", 17), e(primaer[0]),
           e(zweit[1]), e(zweit[0])),
        art="dunkel",
    )


# ------------------------------------------------------------------- Lupe --

def lupe():
    return (
        '<dialog class="lupe" aria-label="Aufnahme vergrößert">'
        '<div class="lupe__kasten">'
        '<button class="lupe__zu" type="button" aria-label="Schließen">%s</button>'
        '<img src="" alt="" role="presentation"><p class="lupe__text"></p></div></dialog>' % icon("x", 19)
    )
