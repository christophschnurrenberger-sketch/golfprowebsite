/**
 * Was diese Seite von der echten unterscheidet.
 *
 * Die Seiten daneben sind unveraenderte Ausgabe von TeePilot: derselbe
 * Renderer, dasselbe Stylesheet, dieselben Bausteine. Nur der Server fehlt -
 * es ist eine eingefrorene Kopie. Buchen, Anmelden und Absenden koennen
 * deshalb nicht funktionieren. Statt ins Leere zu klicken, sagt diese Datei,
 * was an der Stelle passieren wuerde.
 *
 * Eine Datei, kein Geruest: Sie darf geloescht werden, dann bleibt die
 * Seite genau so stehen, wie das CMS sie ausgegeben hat.
 */
(function () {
  'use strict';

  var HINWEIS = {
    buchen: ['Hier würde jetzt gebucht.',
             'Im laufenden System stehen hier nur die Zeiten, die wirklich frei sind. '
           + 'Nach dem Klick kommen Name und E-Mail, danach die Bestätigung per Mail '
           + 'und am Tag davor eine Erinnerung.'],
    konto:  ['Hier ginge es in den Kundenbereich.',
             'Dort sieht der Schüler seine Termine, offene Paketeinheiten, den '
           + 'Trainingsplan und seine Rechnungen — auf dem Telefon genauso wie am Rechner.'],
    formular: ['Die Nachricht ginge jetzt raus.',
             'Im laufenden System landet sie als Anfrage im CMS, mit Quelle und Zeitpunkt, '
           + 'und lässt sich von dort direkt in einen Kunden verwandeln.']
  };

  var stil = document.createElement('style');
  stil.textContent = [
    '.bsp-marke{position:fixed;right:16px;bottom:16px;z-index:60;',
      'font:500 13px/1 var(--schrift,system-ui);letter-spacing:.01em;',
      'display:inline-flex;align-items:center;gap:8px;padding:9px 13px;',
      'border-radius:999px;border:1px solid rgba(0,0,0,.12);cursor:pointer;',
      'background:#fffdf8;color:#2b2f2c;box-shadow:0 6px 22px rgba(0,0,0,.13)}',
    '.bsp-marke::before{content:"";width:7px;height:7px;border-radius:50%;',
      'background:var(--akzent,#c9922e)}',
    '.bsp-marke:hover{border-color:rgba(0,0,0,.26)}',
    '.bsp-blatt{position:fixed;inset:0;z-index:61;display:none;',
      'align-items:center;justify-content:center;padding:20px;',
      'background:rgba(20,26,22,.5)}',
    '.bsp-blatt[data-offen="ja"]{display:flex}',
    '.bsp-kasten{max-width:430px;background:#fffdf8;color:#2b2f2c;',
      'border-radius:var(--radius,8px);padding:26px 26px 22px;',
      'font:400 15px/1.55 var(--schrift,system-ui);box-shadow:0 24px 60px rgba(0,0,0,.3)}',
    '.bsp-kasten h2{margin:0 0 10px;font-size:20px;line-height:1.25;letter-spacing:-.01em}',
    '.bsp-kasten p{margin:0 0 14px}',
    '.bsp-kasten p:last-of-type{margin-bottom:18px}',
    '.bsp-kasten small{display:block;color:#6f766f;font-size:13px;line-height:1.5}',
    '.bsp-zu{appearance:none;border:0;cursor:pointer;font:inherit;font-weight:600;',
      'padding:10px 16px;border-radius:var(--radius,8px);',
      'background:var(--marke,#1e4b54);color:#fff}'
  ].join('');
  document.head.appendChild(stil);

  var blatt = document.createElement('div');
  blatt.className = 'bsp-blatt';
  blatt.innerHTML = '<div class="bsp-kasten" role="dialog" aria-modal="true">'
    + '<h2></h2><p></p><small></small>'
    + '<p style="margin:18px 0 0"><button class="bsp-zu" type="button">Verstanden</button></p>'
    + '</div>';
  document.body.appendChild(blatt);

  var kUeber = 'Max Mustermann gibt es nicht. Name, Preise, Texte und Termine sind erfunden. '
             + 'Die Seite selbst ist es nicht: Sie kommt unverändert aus dem Baukasten von '
             + 'TeePilot — derselbe Renderer, dasselbe Stylesheet, dieselben Bausteine.';

  function zeigen(titel, text, fuss) {
    blatt.querySelector('h2').textContent = titel;
    blatt.querySelector('p').textContent = text;
    blatt.querySelector('small').textContent = fuss || '';
    blatt.setAttribute('data-offen', 'ja');
    blatt.querySelector('.bsp-zu').focus();
  }
  function schliessen() { blatt.setAttribute('data-offen', 'nein'); }

  blatt.addEventListener('click', function (e) {
    if (e.target === blatt || e.target.classList.contains('bsp-zu')) schliessen();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') schliessen();
  });

  var marke = document.createElement('button');
  marke.className = 'bsp-marke';
  marke.type = 'button';
  marke.textContent = 'Beispielseite';
  marke.addEventListener('click', function () {
    zeigen('Eine Beispielseite', kUeber,
           'Was hier nicht geht: buchen, anmelden, absenden. Dafür fehlt der Server — '
         + 'es ist eine eingefrorene Kopie.');
  });
  document.body.appendChild(marke);

  /* Alles, was auf einen Server zeigen würde, wurde beim Einfrieren auf
     #beispiel umgebogen. Welcher Hinweis dazu passt, verrät die Umgebung. */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href="#beispiel"]');
    if (!a) return;
    e.preventDefault();
    var art = a.closest('.kontokasten, .abschnitt--konto') ? 'konto' : 'buchen';
    zeigen(HINWEIS[art][0], HINWEIS[art][1]);
  });

  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f.getAttribute || (f.getAttribute('action') || '').indexOf('#beispiel') === -1) return;
    e.preventDefault();
    var art = f.closest('.kontokasten, .abschnitt--konto') ? 'konto' : 'formular';
    zeigen(HINWEIS[art][0], HINWEIS[art][1]);
  });
})();
