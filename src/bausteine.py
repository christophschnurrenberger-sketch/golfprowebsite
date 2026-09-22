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
        schluessel, (schluessel, "", "Aufnahme aus TeePilot")
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
        adresse = ("teepilot · " + name) if schluessel.startswith("app-") \
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

def kopfblock(vorzeile, titel, fuehrung="", mitte=False, stufe=2, extra="",
              marke=False):
    """Kopf eines Abschnitts.

    `vorzeile` wird standardmaessig **nicht** ausgegeben. Ein kleines
    gesperrtes Versal-Etikett ueber jeder Ueberschrift ist das
    Erkennungsmerkmal zusammengesetzter Seiten, und eine Ueberschrift, die
    ein Schild darueber braucht, ist noch nicht fertig. Wo die Angabe
    wirklich traegt, etwa „Schritt 3 von 5", setzt der Aufrufer
    `marke=True`.
    """
    teile = ['<div class="kopfblock%s">' % (" kopfblock--mitte" if mitte else "")]
    if vorzeile and marke:
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
            "<div><h1>%s</h1>"
            '<p class="fuehrung mt-5">%s</p></div>'
            "%s</div></div></section>"
            % (titel, fuehrung,
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
               kopf_cms="Mit TeePilot"):
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

def schluss_cta(titel=None, text=None, primaer=("Demo ansehen", "/demo/"),
                zweit=("Persönlich sprechen", "/kontakt/")):
    """Der Abschluss jeder Seite.

    Linksbündig und zweispaltig statt zentriert: Auf zwanzig Seiten
    derselbe mittig gesetzte Block waere genau das Vorlagengefuehl, das
    hier nicht entstehen soll.
    """
    titel = titel or "Sieh es dir an."
    text = text or ("Die Demo braucht keine Anmeldung und keine Angaben. Wenn "
                    "es nicht passt, hast du zwei Minuten verloren.")
    return (
        '<section class="abschnitt abschnitt--dunkel"><div class="huelle">'
        '<div class="paar paar--unten" style="--paar:minmax(0,6fr) minmax(0,5fr)">'
        '<div class="aussage aussage--weit"><h2>%s</h2>'
        '<p class="aussage__nach" style="color:#b9c8bf">%s</p></div>'
        '<div class="knopfreihe" style="padding-bottom:6px">'
        '<a class="knopf knopf--hell" href="%s" data-event="footer_demo_click">%s</a>'
        '<a class="knopf knopf--rand-hell" href="%s" data-event="footer_contact_click">%s</a>'
        "</div></div></div></section>"
        % (titel, e(text), e(primaer[1]), e(primaer[0]),
           e(zweit[1]), e(zweit[0]))
    )


# ------------------------------------------------------------------- Lupe --

def lupe():
    return (
        '<dialog class="lupe" aria-label="Aufnahme vergrößert">'
        '<div class="lupe__kasten">'
        '<button class="lupe__zu" type="button" aria-label="Schließen">%s</button>'
        '<img src="" alt="" role="presentation"><p class="lupe__text"></p></div></dialog>' % icon("x", 19)
    )


# ============================================================================
# REDAKTIONELLE BAUSTEINE
# ----------------------------------------------------------------------------
# Gegen das Kachelraster. Jeder dieser Bausteine gibt einer Section einen
# eigenen Rhythmus, damit keine zwei hintereinander gleich aussehen.
# ============================================================================


def aussage(titel, nach="", art="", weit=False):
    """Eine einzelne grosse Aussage traegt die ganze Section.

    Staerker als fuenf weitere Kacheln – und sie kostet keine einzige.
    """
    return abschnitt(
        '<div class="aussage%s"><h2>%s</h2>%s</div>'
        % (" aussage--weit" if weit else "", titel,
           ('<p class="aussage__nach">%s</p>' % nach) if nach else ""),
        art=art,
    )


def legende(nummer, titel, satz):
    """01 — Dashboard / „Alles Wichtige auf einen Blick.“"""
    return (
        '<figcaption class="legende">'
        '<span class="legende__nr">%s %s</span>'
        '<span class="legende__text">%s</span></figcaption>'
        % (e(nummer), e(titel), e(satz))
    )


def bild_mit_legende(schluessel, nummer, titel=None, satz=None, lazy=True, klein=False):
    name, _bereich, zeile = bild_daten(schluessel)
    return (
        '<figure style="margin:0">%s%s</figure>'
        % (rahmen(schluessel, lazy=lazy, klein=klein),
           legende(nummer, titel or name, satz or zeile))
    )


def kapitel(nummer, titel, text, bild, punkte=None, fuss="", gedreht=False,
            lazy=True):
    """Ein Modul als eigene Doppelseite: Nummer, Ueberschrift, Text, Bild.

    Ungerade Nummern haben das Bild rechts, gerade links. Der Wechsel
    nimmt der Reihe den Gleichschritt.
    """
    liste = ""
    if punkte:
        liste = ('<ul class="kapitel__liste">%s</ul>'
                 % "".join("<li><span>%s</span></li>" % e(x) for x in punkte))
    return (
        '<div class="kapitel%s">'
        '<div class="kapitel__text">'
        '<span class="kapitel__nr" aria-hidden="true">%s</span>'
        "<h3>%s</h3><p>%s</p>%s%s</div>"
        '<div class="kapitel__bild">%s</div>'
        "</div>"
        % (" kapitel--gedreht" if gedreht else "", e(nummer), e(titel), text,
           liste, ('<div class="kapitel__fuss">%s</div>' % fuss) if fuss else "",
           bild_mit_legende(bild, nummer, lazy=lazy))
    )


def split(links_marke, links_bild, rechts_marke, rechts_bild,
          links_nr="", rechts_nr=""):
    """Links das CMS, rechts die Website, dazwischen eine Linie."""
    def seite(marke, bild, nr, gruen):
        name, _b, zeile = bild_daten(bild)
        return (
            '<div><span class="split__marke%s">%s</span>%s</div>'
            % (" split__marke--gruen" if gruen else "", e(marke),
               bild_mit_legende(bild, nr or name, satz=zeile))
        )
    return (
        '<div class="split">%s<div class="split__linie" aria-hidden="true"></div>%s</div>'
        % (seite(links_marke, links_bild, links_nr, True),
           seite(rechts_marke, rechts_bild, rechts_nr, False))
    )


def kette(glieder):
    """glieder: Liste aus (titel, text). Ein Ablauf, keine vier Kaesten."""
    return (
        '<div class="kette">%s</div>'
        # Ohne Nummernplaketten: Vier Schritte untereinander, jeder durch
        # eine Haarlinie getrennt, liest ohnehin jeder von oben nach unten.
        % "".join(
            '<div class="kette__glied"><div><h4>%s</h4><p>%s</p></div></div>'
            % (e(t), x) for t, x in glieder
        )
    )


def typoliste(paare):
    """paare: Liste aus (begriff, erklaerung). Ersetzt ein Kachelraster.

    Beide Spalten nehmen HTML: Der Begriff ist oft ein Link. Wer Klartext
    uebergibt, der Sonderzeichen enthalten kann, entschaerft ihn selbst
    mit e().
    """
    return (
        '<ul class="typoliste">%s</ul>'
        % "".join("<li><b>%s</b><span>%s</span></li>" % (b, x) for b, x in paare)
    )


def vollbild(schluessel, legende_nr="", legende_satz="", rand=True):
    """Ein Screenshot ueber die volle Seitenbreite."""
    name, _b, zeile = bild_daten(schluessel)
    return (
        '<div class="voll%s">%s%s</div>'
        % (" voll--rand" if rand else "",
           rahmen(schluessel),
           ('<div class="huelle">%s</div>'
            % legende(legende_nr or name, name, legende_satz or zeile))
           if legende_nr or legende_satz else "")
    )


def foto_flaeche(schluessel, form="quer", alt_text="", rund=True):
    """Ein Foto – oder nichts.

    Gibt einen leeren String zurueck, wenn kein Foto hinterlegt ist. Der
    aufrufende Abschnitt prueft das und baut dann seine typografische
    Alternative. Graue Platzhalterflaechen gibt es nicht.
    """
    pfad = D.foto(schluessel)
    if not pfad:
        return ""
    return (
        '<div class="foto foto--%s%s">'
        '<img src="%s" alt="%s" loading="lazy" decoding="async"></div>'
        % (form, " foto--rund" if rund else "", e(pfad), e(alt_text))
    )


def hat_foto(schluessel):
    return D.foto(schluessel) is not None
