/* =============================================================================
   TeePilot – Marketingwebsite
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

  /* -------------------------------------------------------------- Vorhang
     Die Navigation ist kein Klappmenue, sondern eine ganze Seite. Ein Klick
     auf einen Punkt im Kopf zieht sie herunter; der Kopf bleibt darueber
     stehen und wird hell. Auf dem Telefon oeffnet der Menue-Knopf denselben
     Vorhang, nur mit allen Abschnitten untereinander.

     Kein Hover-Oeffnen: Ein Vollbild, das aufgeht, weil die Maus im
     Vorbeifahren einen Knopf streift, ist eine Zumutung. Klick oder nichts. */
  var vorhang = $('#vorhang');
  var kopf = $('.kopf');
  var menueKnopf = $('.menue-knopf');
  var schalter = $$('.nav__knopf--vorhang');
  var teile = vorhang ? $$('.vorhang__teil', vorhang) : [];
  var letzterKnopf = null;

  function vorhangOffen() {
    return vorhang && vorhang.getAttribute('data-offen') === 'ja';
  }

  /* Der Kopf wechselt die Farbe nicht mit dem Vorhang, sondern wenn der
     Vorhang ihn erreicht hat. Sofort gewechselt stand helle Schrift einen
     Moment lang auf hellem Grund; sofort zurueckgewechselt stuende dunkle
     Schrift auf Gruen. Beim Aufziehen faellt der Vorhang ueber den Kopf,
     beim Zumachen gibt er ihn als Letztes wieder frei. */
  var kopfFrist;
  function kopfHell(ja) {
    if (!kopf) return;
    clearTimeout(kopfFrist);
    kopfFrist = setTimeout(function () {
      kopf.setAttribute('data-vorhang', ja ? 'ja' : 'nein');
    }, ja ? 150 : 430);
  }

  function vorhangZu(fokus) {
    if (!vorhang) return;
    vorhang.setAttribute('data-offen', 'nein');
    kopfHell(false);
    schalter.forEach(function (k) { k.setAttribute('aria-expanded', 'false'); });
    if (menueKnopf) menueKnopf.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    if (fokus && letzterKnopf) letzterKnopf.focus();
    letzterKnopf = null;
    durchHover = 0;
    feldFristAus();
    feld = null;
  }

  function vorhangAuf(teil, knopf) {
    if (!vorhang) return;
    /* Die Abschnitte werden neu gesetzt, bevor der Vorhang faellt – sonst
       sieht man beim Wechsel kurz den alten. */
    teile.forEach(function (t) {
      t.classList.toggle('ist-an', teil !== null && t.getAttribute('data-teil') === teil);
    });
    /* Wo der Kopf gerade endet, haengt davon ab, ob das Ankuendigungsband
       noch steht – also vom Scrollstand. Gemessen statt geraten: Sonst
       lag die erste Zeile auf dem Telefon im Logo. */
    if (kopf) {
      vorhang.style.setProperty(
        '--kopf-unten', Math.round(kopf.getBoundingClientRect().bottom) + 'px');
    }
    vorhang.setAttribute('data-offen', 'ja');
    vorhang.setAttribute('data-alle', teil === null ? 'ja' : 'nein');
    /* Beim Wechsel zwischen zwei Abschnitten steht der Kopf schon hell –
       dann darf die Frist ihn nicht erneut verzoegern. */
    if (kopf.getAttribute('data-vorhang') === 'ja') { clearTimeout(kopfFrist); }
    else { kopfHell(true); }
    schalter.forEach(function (k) {
      k.setAttribute('aria-expanded', k === knopf ? 'true' : 'false');
    });
    if (menueKnopf) {
      menueKnopf.setAttribute('aria-expanded', teil === null ? 'true' : 'false');
    }
    document.body.style.overflow = 'hidden';
    letzterKnopf = knopf || null;
    feldFristAus();
    feldMessen();
  }

  /* Hover oeffnet - aber erst, wenn jemand wirklich stehen bleibt. Ohne
     Absichtsfrist zieht jede Maus, die im Vorbeifahren die Leiste streift,
     eine ganze Seite auf. 170 ms sind lang genug, dass ein Durchfahren
     nichts ausloest, und kurz genug, dass es nicht traege wirkt. */
  var zeiger = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var absicht;
  var durchHover = 0;

  schalter.forEach(function (knopf) {
    knopf.addEventListener('click', function () {
      clearTimeout(absicht);
      /* Ein Klick kurz nach dem Hover-Oeffnen schliesst nicht: Er gilt dem,
         was man gerade erst gesehen hat, nicht dem Zumachen. */
      if (Date.now() - durchHover < 400) { durchHover = 0; return; }
      if (vorhangOffen() && knopf.getAttribute('aria-expanded') === 'true') {
        vorhangZu(true); return;
      }
      vorhangAuf(knopf.getAttribute('data-teil'), knopf);
    });

    if (!zeiger) return;

    knopf.addEventListener('mouseenter', function () {
      clearTimeout(absicht);
      if (vorhangOffen()) {
        /* Steht der Vorhang schon, wird ohne Frist gewechselt - sonst
           haengt der Wechsel zwischen zwei Bereichen spuerbar nach. */
        if (knopf.getAttribute('aria-expanded') !== 'true') {
          vorhangAuf(knopf.getAttribute('data-teil'), knopf);
        }
        return;
      }
      absicht = setTimeout(function () {
        durchHover = Date.now();
        vorhangAuf(knopf.getAttribute('data-teil'), knopf);
      }, 170);
    });

    knopf.addEventListener('mouseleave', function () { clearTimeout(absicht); });
  });

  if (menueKnopf) {
    menueKnopf.addEventListener('click', function () {
      if (vorhangOffen()) { vorhangZu(true); return; }
      vorhangAuf(null, menueKnopf);
    });
  }

  /* ---- Wann der Vorhang von selbst wieder zugeht
     Der Vorhang fuellt das ganze Fenster, also kann man ihn nicht
     "verlassen" - mouseleave feuert nie. Stattdessen ein Feld: die Kopfzeile
     ueber die ganze Breite, darunter der Inhalt mit etwas Luft. Wer da
     herausfaehrt - weit nach rechts, weit nach links, unter den Text -
     meint den Vorhang nicht mehr.

     Zwei Dinge halten das ruhig: Das Feld ist grosszuegiger als der Inhalt,
     und das Zugehen wartet eine Karenzzeit ab. Wer nur kurz ueber den Rand
     wischt und zurueckkommt, loest nichts aus. */
  var LUFT = 56;      /* Zugabe um den Inhalt, in Pixeln */
  var RAND = 48;      /* Streifen an jeder Kante, der immer schliesst */
  var KARENZ = 340;   /* wie lange draussen, bevor es zugeht */
  var feld = null;
  var feldFrist = null;

  function feldMessen() {
    if (!vorhang || !vorhangOffen()) { feld = null; return; }
    var inhalt = vorhang.querySelector('.vorhang__teil.ist-an')
              || $('.vorhang__koerper', vorhang);
    if (!inhalt) { feld = null; return; }
    var r = inhalt.getBoundingClientRect();
    var w = window.innerWidth;
    /* Der Streifen an der Kante muss bleiben, auch wenn der Inhalt fast so
       breit ist wie das Fenster. Bei 1440 waeren aus der Zugabe sonst acht
       Pixel geworden - dahin trifft niemand absichtlich. Die Klammer greift
       nie in den Inhalt: Bis hinunter zu 1024 liegt sie ausserhalb. */
    feld = {
      kopfUnten: kopf ? kopf.getBoundingClientRect().bottom : 0,
      links: Math.max(r.left - LUFT, RAND),
      rechts: Math.min(r.right + LUFT, w - RAND),
      unten: r.bottom + LUFT
    };
  }

  function imFeld(x, y) {
    if (!feld) return true;
    /* Die Kopfzeile geht ueber die ganze Breite und gehoert immer dazu -
       sonst schloesse der Vorhang beim Weg zum Menuepunkt ganz rechts. */
    if (y <= feld.kopfUnten) return true;
    return x >= feld.links && x <= feld.rechts && y <= feld.unten;
  }

  function feldFristAus() {
    if (feldFrist) { clearTimeout(feldFrist); feldFrist = null; }
  }

  function zeigerBewegt(e) {
    if (!zeiger || !vorhangOffen()) return;
    if (vorhang.getAttribute('data-alle') === 'ja') return;  /* Telefon */
    if (imFeld(e.clientX, e.clientY)) { feldFristAus(); return; }
    if (feldFrist) return;
    feldFrist = setTimeout(function () {
      feldFrist = null;
      vorhangZu(false);
    }, KARENZ);
  }

  if (vorhang) {
    document.addEventListener('mousemove', zeigerBewegt);
    /* Faehrt die Maus ganz aus dem Fenster, ist sie auch draussen. */
    document.addEventListener('mouseleave', function () {
      if (zeiger && vorhangOffen() && vorhang.getAttribute('data-alle') !== 'ja'
          && !feldFrist) {
        feldFrist = setTimeout(function () { feldFrist = null; vorhangZu(false); },
                               KARENZ);
      }
    });
    window.addEventListener('resize', feldMessen);

    /* Ein Klick irgendwohin, wo kein Ziel ist, schliesst. Bei einem Vorhang,
       der per Hover aufgeht, muss das Zumachen leicht sein. */
    vorhang.addEventListener('click', function (e) {
      if (!e.target.closest('a, button')) vorhangZu(true);
    });

    /* Der Fokus darf nicht hinter den Vorhang wandern. Gefangen wird er
       zwischen Kopf und Vorhang – beide liegen oben. */
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && vorhangOffen()) { vorhangZu(true); return; }
      if (e.key !== 'Tab' || !vorhangOffen()) return;
      var felder = [].concat($$('a, button', kopf || document),
                             $$('a, button', vorhang))
        .filter(function (el) { return el.offsetParent !== null; });
      if (!felder.length) return;
      var erster = felder[0], letzter = felder[felder.length - 1];
      if (e.shiftKey && document.activeElement === erster) {
        e.preventDefault(); letzter.focus();
      } else if (!e.shiftKey && document.activeElement === letzter) {
        e.preventDefault(); erster.focus();
      }
    });

    /* Wird das Fenster breit, darf kein gesperrter Body zurueckbleiben. */
    window.addEventListener('resize', function () {
      if (vorhangOffen() && vorhang.getAttribute('data-alle') === 'ja'
          && window.innerWidth > 980) {
        vorhangZu(false);
      }
    });
  }

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
