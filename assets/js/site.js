/* =============================================================================
   GolfProCMS – Marketingwebsite
   -----------------------------------------------------------------------------
   Ein Skript, keine Abhaengigkeit. Alles was hier steht, ist Verhalten, das
   ohne JavaScript nicht ginge – die Seite selbst ist auch ohne lesbar und
   navigierbar. Jeder Block prueft erst, ob es sein Element ueberhaupt gibt.
   ============================================================================= */
(function () {
  'use strict';

  var $  = function (s, w) { return (w || document).querySelector(s); };
  var $$ = function (s, w) { return Array.prototype.slice.call((w || document).querySelectorAll(s)); };
  var sanft = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------------------- Analytics
     Events werden nur eingesammelt und weitergereicht. Ob ueberhaupt etwas
     gemessen wird, entscheidet spaeter ein Consent-Banner; bis dahin landen
     sie in einer Warteschlange, die niemand abholt. Kein Tracker, kein Cookie. */
  var spur = (window.gpAnalytics = window.gpAnalytics || { queue: [] });
  function melden(name, daten) {
    var e = { event: name, daten: daten || {}, t: Date.now() };
    spur.queue.push(e);
    if (typeof spur.sink === 'function') { try { spur.sink(e); } catch (x) {} }
    if (window.dataLayer && typeof window.dataLayer.push === 'function') {
      window.dataLayer.push(Object.assign({ event: name }, e.daten));
    }
  }
  window.gpMelden = melden;

  /* Alles mit data-event meldet sich beim Klick selbst. */
  document.addEventListener('click', function (ev) {
    var t = ev.target.closest('[data-event]');
    if (t) melden(t.getAttribute('data-event'), { ziel: t.getAttribute('href') || '' });
  });

  /* ------------------------------------------------------------- Kopfzeile */
  var kopf = $('.kopf');
  if (kopf) {
    var setzenKopf = function () {
      kopf.setAttribute('data-gescrollt', window.scrollY > 8 ? 'ja' : 'nein');
    };
    setzenKopf();
    window.addEventListener('scroll', setzenKopf, { passive: true });
  }

  /* --------------------------------------------------------- Mega-Menues
     Auf dem Zeigegeraet oeffnet Hover, auf Tastatur und Touch der Klick.
     Das Schliessen nach dem Verlassen bekommt eine kurze Gnadenfrist, damit
     der Weg vom Knopf ins Menue nicht abreisst. */
  var punkte = $$('.nav__punkt');
  var zeiger = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  function zu(p) {
    p.setAttribute('data-offen', 'nein');
    var k = $('.nav__knopf', p);
    if (k) k.setAttribute('aria-expanded', 'false');
  }
  function auf(p) {
    punkte.forEach(function (a) { if (a !== p) zu(a); });
    p.setAttribute('data-offen', 'ja');
    var k = $('.nav__knopf', p);
    if (k) k.setAttribute('aria-expanded', 'true');
  }

  punkte.forEach(function (p) {
    var knopf = $('.nav__knopf', p);
    var menue = $('.mega', p);
    if (!knopf || !menue) return;
    var frist;

    /* Wer mit der Maus darueberfaehrt und dann klickt, will das Menue nicht
       schliessen – er hat es ja gerade erst gesehen. Deshalb merkt sich der
       Punkt, dass Hover es geoeffnet hat, und der erste Klick danach laesst
       es stehen. Jeder weitere Klick schliesst wie erwartet. */
    var durchHover = false;

    knopf.addEventListener('click', function (e) {
      e.preventDefault();
      if (p.getAttribute('data-offen') === 'ja') {
        if (durchHover) { durchHover = false; return; }
        zu(p);
      } else {
        auf(p);
      }
    });

    if (zeiger) {
      p.addEventListener('mouseenter', function () {
        clearTimeout(frist);
        if (p.getAttribute('data-offen') !== 'ja') durchHover = true;
        auf(p);
      });
      p.addEventListener('mouseleave', function () {
        clearTimeout(frist);
        frist = setTimeout(function () { durchHover = false; zu(p); }, 180);
      });
    }

    /* Tab aus dem Menue heraus schliesst es. */
    p.addEventListener('focusout', function (e) {
      if (!p.contains(e.relatedTarget)) zu(p);
    });
  });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    punkte.forEach(function (p) {
      if (p.getAttribute('data-offen') === 'ja') { zu(p); var k = $('.nav__knopf', p); if (k) k.focus(); }
    });
    if (mobilOffen()) mobilSchliessen(true);
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav__punkt')) punkte.forEach(zu);
  });

  /* ------------------------------------------------- Vorschau im Mega-Menü
     Wer einen Eintrag ueberfaehrt, sieht rechts die Aufnahme des Bereichs.
     Reine Zugabe: Ohne JavaScript steht dort das erste Bild, und die Links
     funktionieren ohnehin. */
  $$('.mega').forEach(function (menue) {
    var rahmen = $('.mega__rahmen', menue);
    if (!rahmen) return;
    var bilder = $$('img', rahmen);
    var texte = $$('[data-bildtext]', menue);
    var anfang = bilder.length ? bilder[0].getAttribute('data-bild') : null;

    function zeigen(schluessel) {
      bilder.forEach(function (b) { b.hidden = b.getAttribute('data-bild') !== schluessel; });
      texte.forEach(function (t) { t.hidden = t.getAttribute('data-bildtext') !== schluessel; });
    }

    $$('[data-vorschau]', menue).forEach(function (a) {
      var schluessel = a.getAttribute('data-vorschau');
      a.addEventListener('mouseenter', function () { zeigen(schluessel); });
      a.addEventListener('focus', function () { zeigen(schluessel); });
    });

    /* Verlaesst der Zeiger die Liste, kehrt die Vorschau zum Ausgangsbild
       zurueck – sonst bleibt ein zufaelliger Zwischenstand stehen. */
    var liste = $('.mega__spalten', menue);
    if (liste && anfang) {
      liste.addEventListener('mouseleave', function () { zeigen(anfang); });
    }
  });

  /* ---------------------------------------------------- Mobile Navigation */
  var menueKnopf = $('.menue-knopf');
  var mobil = $('.mobil');

  function mobilOffen() { return mobil && mobil.getAttribute('data-offen') === 'ja'; }
  function mobilSchliessen(fokus) {
    if (!mobil) return;
    mobil.setAttribute('data-offen', 'nein');
    if (menueKnopf) menueKnopf.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    if (fokus && menueKnopf) menueKnopf.focus();
  }

  if (menueKnopf && mobil) {
    menueKnopf.addEventListener('click', function () {
      var offen = mobilOffen();
      mobil.setAttribute('data-offen', offen ? 'nein' : 'ja');
      menueKnopf.setAttribute('aria-expanded', offen ? 'false' : 'true');
      /* Hintergrund festhalten, solange das Menue liegt. */
      document.body.style.overflow = offen ? '' : 'hidden';
    });

    $$('.mobil__schalter', mobil).forEach(function (s) {
      s.addEventListener('click', function () {
        var ziel = document.getElementById(s.getAttribute('aria-controls'));
        if (!ziel) return;
        var offen = s.getAttribute('aria-expanded') === 'true';
        s.setAttribute('aria-expanded', offen ? 'false' : 'true');
        ziel.setAttribute('data-offen', offen ? 'nein' : 'ja');
      });
    });

    /* Ein Klick auf einen Link im Menue schliesst es. */
    $$('a', mobil).forEach(function (a) {
      a.addEventListener('click', function () { mobilSchliessen(false); });
    });

    var mobilZu = $('.mobil__zu', mobil);
    if (mobilZu) mobilZu.addEventListener('click', function () { mobilSchliessen(true); });
  }

  /* Wird das Fenster breit, darf kein gesperrter Body zurueckbleiben. */
  window.addEventListener('resize', function () {
    if (window.innerWidth > 980 && mobilOffen()) mobilSchliessen(false);
  });

  /* ------------------------------------------------------- Klebender CTA
     Erscheint erst, wenn jemand wirklich liest – nicht sofort. Ein Schliessen
     haelt fuer die Sitzung. */
  var kleber = $('.sticky-cta');
  if (kleber) {
    var weg = false;
    try { weg = sessionStorage.getItem('gp-cta-zu') === '1'; } catch (x) {}
    if (!weg) {
      var pruefen = function () {
        var tief = window.scrollY > window.innerHeight * 1.2;
        var ende = window.scrollY + window.innerHeight > document.body.scrollHeight - 700;
        kleber.setAttribute('data-sichtbar', tief && !ende ? 'ja' : 'nein');
      };
      window.addEventListener('scroll', pruefen, { passive: true });
      pruefen();
    }
    var kleberZu = $('.sticky-cta__zu', kleber);
    if (kleberZu) kleberZu.addEventListener('click', function () {
      kleber.setAttribute('data-sichtbar', 'nein');
      kleber.style.display = 'none';
      try { sessionStorage.setItem('gp-cta-zu', '1'); } catch (x) {}
    });
  }

  /* ------------------------------------------------- Erscheinen beim Scrollen */
  var zuZeigen = $$('.zeigen');
  if (zuZeigen.length && 'IntersectionObserver' in window && sanft) {
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.setAttribute('data-sichtbar', 'ja');
        beobachter.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -60px 0px', threshold: 0.08 });
    zuZeigen.forEach(function (el) { beobachter.observe(el); });
  } else {
    zuZeigen.forEach(function (el) { el.setAttribute('data-sichtbar', 'ja'); });
  }

  /* -------------------------------------------------------- Reiter-Gruppen
     Bedient die interaktive Demo, den Feature-Wechsel und den Geraetewechsler
     ueber dieselbe Mechanik: [data-reiter] am Knopf, [data-tafel] am Inhalt. */
  $$('[data-reitergruppe]').forEach(function (gruppe) {
    var knoepfe = $$('[data-reiter]', gruppe);
    var tafeln  = $$('[data-tafel]', gruppe);
    var laden   = $('.demo__laden', gruppe);
    if (!knoepfe.length) return;

    function waehlen(schluessel, melde) {
      knoepfe.forEach(function (k) {
        k.setAttribute('aria-selected', k.getAttribute('data-reiter') === schluessel ? 'true' : 'false');
      });
      var zeigenTafel = function () {
        tafeln.forEach(function (t) {
          t.setAttribute('data-aktiv', t.getAttribute('data-tafel') === schluessel ? 'ja' : 'nein');
        });
      };
      /* Winzige Ladeanzeige: das Bild wechselt, das soll man merken. */
      if (laden && sanft) {
        laden.setAttribute('data-an', 'ja');
        setTimeout(function () { zeigenTafel(); laden.setAttribute('data-an', 'nein'); }, 170);
      } else {
        zeigenTafel();
      }
      if (melde) melden(gruppe.getAttribute('data-reitergruppe'), { bereich: schluessel });
    }

    knoepfe.forEach(function (k, i) {
      k.addEventListener('click', function () { waehlen(k.getAttribute('data-reiter'), true); });
      /* Pfeiltasten wandern durch die Reiter – so erwartet es jeder Screenreader. */
      k.addEventListener('keydown', function (e) {
        var schritt = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1
                    : e.key === 'ArrowLeft'  || e.key === 'ArrowUp'   ? -1 : 0;
        if (!schritt) return;
        e.preventDefault();
        var n = knoepfe[(i + schritt + knoepfe.length) % knoepfe.length];
        n.focus(); waehlen(n.getAttribute('data-reiter'), true);
      });
    });

    var start = gruppe.getAttribute('data-start') || knoepfe[0].getAttribute('data-reiter');
    waehlen(start, false);
  });

  /* ------------------------------------------------------- Geraetewechsler */
  $$('[data-geraetegruppe]').forEach(function (gruppe) {
    var knoepfe = $$('[data-geraet-knopf]', gruppe);
    var halter  = $('.buehne__halter', gruppe);
    if (!halter) return;
    knoepfe.forEach(function (k) {
      k.addEventListener('click', function () {
        var g = k.getAttribute('data-geraet-knopf');
        knoepfe.forEach(function (a) { a.setAttribute('aria-selected', a === k ? 'true' : 'false'); });
        halter.setAttribute('data-geraet', g);
        $$('[data-geraet-bild]', gruppe).forEach(function (b) {
          b.hidden = b.getAttribute('data-geraet-bild') !== g;
        });
        melden('demo_geraet_wechsel', { geraet: g });
      });
    });
  });

  /* ---------------------------------------------------- Gefuehrte Produkttour */
  var tour = $('[data-tour]');
  if (tour) {
    var schritte = $$('[data-schritt]', tour);
    var zurueck  = $('[data-tour-zurueck]', tour);
    var weiter   = $('[data-tour-weiter]', tour);
    var zaehler  = $('[data-tour-zaehler]', tour);
    var balken   = $('[data-tour-balken]', tour);
    var punkteT  = $$('[data-tour-punkt]', tour);
    var jetzt = 0;

    function zeichnen(melde) {
      schritte.forEach(function (s, i) { s.setAttribute('data-aktiv', i === jetzt ? 'ja' : 'nein'); });
      punkteT.forEach(function (p, i) { p.setAttribute('aria-selected', i === jetzt ? 'true' : 'false'); });
      if (zaehler) zaehler.textContent = String(jetzt + 1).padStart(2, '0') + ' / ' + String(schritte.length).padStart(2, '0');
      if (balken) balken.style.width = ((jetzt + 1) / schritte.length * 100) + '%';
      if (zurueck) zurueck.disabled = jetzt === 0;
      if (weiter) {
        var fertig = jetzt === schritte.length - 1;
        weiter.textContent = fertig ? 'Tour beenden' : 'Weiter';
        weiter.setAttribute('data-fertig', fertig ? 'ja' : 'nein');
      }
      if (melde) melden('product_tour_step', { schritt: jetzt + 1 });
    }

    if (weiter) weiter.addEventListener('click', function () {
      if (weiter.getAttribute('data-fertig') === 'ja') {
        melden('product_tour_complete', {});
        var ziel = tour.getAttribute('data-tour-ende');
        if (ziel) { window.location.href = ziel; return; }
      }
      jetzt = Math.min(jetzt + 1, schritte.length - 1); zeichnen(true);
    });
    if (zurueck) zurueck.addEventListener('click', function () {
      jetzt = Math.max(jetzt - 1, 0); zeichnen(true);
    });
    punkteT.forEach(function (p, i) {
      p.addEventListener('click', function () { jetzt = i; zeichnen(true); });
    });

    zeichnen(false);
    melden('product_tour_start', {});
  }

  /* --------------------------------------------------------- Galerie-Filter */
  var galerie = $('[data-galerie]');
  if (galerie) {
    var stuecke = $$('[data-bereich]', galerie);
    $$('[data-filter]', document).forEach(function (f) {
      f.addEventListener('click', function () {
        var wahl = f.getAttribute('data-filter');
        $$('[data-filter]').forEach(function (a) { a.setAttribute('aria-pressed', a === f ? 'true' : 'false'); });
        stuecke.forEach(function (s) {
          s.hidden = wahl !== 'alle' && s.getAttribute('data-bereich') !== wahl;
        });
        melden('screenshot_filter', { bereich: wahl });
      });
    });
  }

  /* ------------------------------------------------------------------ Lupe */
  var lupe = $('dialog.lupe');
  if (lupe) {
    var lupeBild = $('.lupe__kasten img', lupe);
    var lupeText = $('.lupe__text', lupe);

    $$('[data-lupe]').forEach(function (k) {
      k.addEventListener('click', function () {
        var bild = $('img', k);
        if (!bild) return;
        lupeBild.src = bild.getAttribute('data-gross') || bild.src;
        lupeBild.alt = bild.alt;
        if (lupeText) lupeText.textContent = k.getAttribute('data-lupe') || bild.alt;
        if (typeof lupe.showModal === 'function') lupe.showModal();
        melden('screenshot_open', { bild: lupeBild.src });
      });
    });

    var lupeZu = $('.lupe__zu', lupe);
    if (lupeZu) lupeZu.addEventListener('click', function () { lupe.close(); });
    /* Klick auf den Hintergrund schliesst ebenfalls. */
    lupe.addEventListener('click', function (e) { if (e.target === lupe) lupe.close(); });
  }

  /* -------------------------------------------------------------- Formular
     Ohne Backend wird nichts verschickt. Statt eine Absendung vorzutaeuschen,
     sagt die Seite genau das – und bietet den E-Mail-Weg an. Sobald
     data-endpunkt gesetzt ist, geht es wirklich raus. */
  var form = $('form[data-formular]');
  if (form) {
    var erfolg   = $('.erfolg', form.parentNode);
    var abschick = $('[type="submit"]', form);
    var begonnen = false;

    form.addEventListener('input', function () {
      if (!begonnen) { begonnen = true; melden('contact_form_start', {}); }
    });

    var pruefeFeld = function (el) {
      var huelle = el.closest('.feld');
      if (!huelle) return true;
      var ok = el.checkValidity();
      huelle.setAttribute('data-fehler', ok ? 'nein' : 'ja');
      var meldung = $('.feld__fehler', huelle);
      if (meldung && !ok) {
        meldung.textContent = el.validity.valueMissing
          ? (el.getAttribute('data-leer') || 'Bitte fülle dieses Feld aus.')
          : (el.getAttribute('data-ungueltig') || 'Diese Eingabe sieht noch nicht richtig aus.');
      }
      return ok;
    };

    $$('input, select, textarea', form).forEach(function (el) {
      el.addEventListener('blur', function () { pruefeFeld(el); });
      el.addEventListener('input', function () {
        var h = el.closest('.feld');
        if (h && h.getAttribute('data-fehler') === 'ja') pruefeFeld(el);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var alleOk = true, erstesFehlfeld = null;
      $$('input, select, textarea', form).forEach(function (el) {
        if (!pruefeFeld(el)) { alleOk = false; if (!erstesFehlfeld) erstesFehlfeld = el; }
      });
      if (!alleOk) { if (erstesFehlfeld) erstesFehlfeld.focus(); return; }

      melden('contact_form_submit', {});
      var endpunkt = form.getAttribute('data-endpunkt');

      if (!endpunkt) {
        /* Kein Backend hinterlegt: ehrlich sagen und den Mailweg oeffnen. */
        if (erfolg) {
          erfolg.setAttribute('data-an', 'ja');
          erfolg.scrollIntoView({ behavior: sanft ? 'smooth' : 'auto', block: 'center' });
        }
        form.hidden = true;
        return;
      }

      if (abschick) { abschick.disabled = true; abschick.textContent = 'Wird gesendet…'; }
      fetch(endpunkt, { method: 'POST', body: new FormData(form) })
        .then(function (r) {
          if (!r.ok) throw new Error('Status ' + r.status);
          form.hidden = true;
          if (erfolg) { erfolg.setAttribute('data-an', 'ja'); erfolg.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
        })
        .catch(function () {
          if (abschick) { abschick.disabled = false; abschick.textContent = 'Anfrage senden'; }
          var box = $('[data-sendefehler]', form);
          if (box) box.hidden = false;
        });
    });
  }
})();
