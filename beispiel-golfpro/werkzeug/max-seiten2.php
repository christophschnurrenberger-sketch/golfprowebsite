<?php
require __DIR__ . '/cms/lib/bootstrap.php';
$ids = json_decode((string) file_get_contents(__DIR__ . '/max-ids.json'), true);
Tenant::setzen((int) $ids['ws']);

function bl(string $typ, array $daten = []): array {
    $b = Bloecke::neu($typ); $b['daten'] = array_merge($b['daten'], $daten); return $b;
}
function seite(array $d): int { return Tenant::insert('pages', $d + [
    'status' => 'veroeffentlicht', 'aufrufe' => 0, 'conversions' => 0,
    'geaendert' => date('Y-m-d H:i:s', strtotime('-9 days')),
    'erstellt' => date('Y-m-d H:i:s', strtotime('-2 years')),
]); }

/* ------------------------------------------------------------------ Kurse */
seite([
    'titel' => 'Kurse', 'slug' => 'kurse', 'im_menue' => 1, 'position' => 3,
    'seo' => Util::json(['titel' => 'Kurse und Platzreife · Max Mustermann Golf',
        'beschreibung' => 'Platzreifekurs in acht Einheiten, Juniorentraining und Online-Coaching in Musterstadt.']),
    'bloecke' => Util::json([
        bl('hero', ['obertitel' => 'Kurse', 'titel' => 'Kurse mit festem Ablauf.',
            'text' => 'Du weißt von Anfang an, was in welcher Woche drankommt und wann die Prüfung ist.',
            'ausrichtung' => 'links', 'hoehe' => 'klein',
            'knopf_text' => 'Termin buchen', 'knopf_url' => '?w=max&seite=termine',
            'knopf2_text' => '', 'notiz' => '', 'fakten' => '']),
        bl('leistungen', ['titel' => '', 'text' => '', 'automatisch' => false, 'eintraege' => [
            ['titel' => 'Platzreifekurs', 'preis' => '349 €', 'dauer' => '8 Einheiten à 90 Minuten',
             'wer' => 'Einsteiger ohne Vorkenntnisse',
             'text' => 'Acht Einheiten von der ersten Berührung mit dem Schläger bis zur Prüfung. '
                     . 'Theorie, Technik, Etikette und eine Runde auf dem Platz.',
             'note' => 'Leihschläger, Bälle und Prüfungsgebühr sind enthalten.'],
            ['titel' => 'Juniorentraining', 'preis' => '22 €', 'dauer' => '60 Minuten',
             'wer' => 'Kinder und Jugendliche von 6 bis 16',
             'text' => 'Spielerisch, in kleinen Gruppen, mit Material in passender Größe.'],
            ['titel' => 'Online-Coaching (Videocheck)', 'preis' => '45 €', 'dauer' => '30 Minuten',
             'wer' => 'Wer zu weit weg wohnt oder zwischendurch eine Einschätzung braucht',
             'text' => 'Du schickst mir ein Video von deinem Schwung, ich schaue es durch und schicke '
                     . 'dir eine Analyse mit Übungen zurück.'],
        ]]),
        bl('text', ['titel' => 'Wie der Platzreifekurs abläuft', 'spalten' => '2', 'text' =>
            "Die ersten vier Einheiten verbringen wir auf der Übungsanlage: Griff, Stand, Schwung, "
          . "und dazwischen so viel Theorie, wie es für die Prüfung braucht.\n\n"
          . "Ab Einheit fünf geht es auf den Kurzplatz, in der letzten Einheit auf neun Löcher. "
          . "Die Prüfung nehme ich selbst ab — du musst dafür nirgendwo anders hin.\n\n"
          . "Rechne mit sechs bis zehn Wochen, wenn du regelmäßig kommst. Wer zwischendurch "
          . "zwanzig Minuten übt, ist deutlich schneller fertig als jemand, der nur zur Stunde erscheint."]),
        bl('cta', ['titel' => 'Der nächste Kurs startet laufend.',
            'text' => 'Ich setze die Gruppen zusammen, sobald vier Leute zusammenkommen. Schreib mir, '
                    . 'wann es dir passt — dann sage ich dir, wann der nächste beginnt.',
            'knopf_text' => 'Auf die Liste setzen', 'knopf_url' => '?w=max&seite=kontakt',
            'notiz' => 'Unverbindlich, du hörst von mir, bevor es losgeht.']),
    ]),
]);

/* ----------------------------------------------------------------- Preise */
seite([
    'titel' => 'Preise', 'slug' => 'preise', 'im_menue' => 1, 'position' => 4,
    'seo' => Util::json(['titel' => 'Preise · Max Mustermann Golf',
        'beschreibung' => 'Einzelstunden, Gruppentraining, Pakete und Kurse — alle Preise auf einen Blick.']),
    'bloecke' => Util::json([
        bl('hero', ['obertitel' => 'Preise', 'titel' => 'Alles, was es kostet.',
            'text' => 'Alle Preise pro Person. Pakete sind günstiger als Einzelstunden und ein Jahr gültig.',
            'ausrichtung' => 'links', 'hoehe' => 'klein',
            'knopf_text' => '', 'knopf2_text' => '', 'notiz' => '', 'fakten' => '']),
        bl('leistungen', ['titel' => 'Einzeln', 'text' => '', 'automatisch' => true]),
        bl('preise', ['titel' => 'Pakete', 'eintraege' => [
            ['titel' => 'Golf Starter 5', 'preis' => '399 €', 'zusatz' => '5 Einzelstunden à 60 Minuten',
             'merkmale' => "5 × 60 Minuten Einzeltraining\nEin Jahr gültig\nSchriftliche Zusammenfassung je Stunde",
             'knopf_text' => 'Anfragen', 'knopf_url' => '?w=max&seite=kontakt', 'hervorheben' => false],
            ['titel' => 'Golf Fortschritt 10', 'preis' => '749 €', 'zusatz' => '10 Einzelstunden',
             'merkmale' => "10 × 60 Minuten Einzeltraining\nVideoanalyse in Stunde 1, 5 und 10\nTrainingsplan für zwischendurch\nEin Jahr gültig",
             'knopf_text' => 'Anfragen', 'knopf_url' => '?w=max&seite=kontakt', 'hervorheben' => true],
            ['titel' => 'Winterpaket Indoor 8', 'preis' => '519 €', 'zusatz' => '8 Einheiten im Studio',
             'merkmale' => "8 Einheiten im Indoor-Studio\nMit Launch Monitor\nVon November bis März",
             'knopf_text' => 'Anfragen', 'knopf_url' => '?w=max&seite=kontakt', 'hervorheben' => false],
        ]]),
        bl('text', ['titel' => 'Was noch zu den Preisen gehört', 'spalten' => '2', 'text' =>
            "Alle Preise sind Endpreise und enthalten die gesetzliche Umsatzsteuer. Leihschläger und "
          . "Bälle stelle ich, solange du noch keine eigenen hast.\n\n"
          . "Absagen bitte bis 24 Stunden vorher — danach wird die Einheit berechnet. Bei Regen "
          . "verlegen wir ins Indoor-Studio oder verschieben, je nachdem was dir lieber ist.\n\n"
          . "Pakete sind ein Jahr ab Kauf gültig. Du siehst jederzeit in deinem Bereich, wie viele "
          . "Einheiten noch offen sind."]),
        bl('faq', ['titel' => 'Zu Preisen und Bezahlung', 'eintraege' => [
            ['frage' => 'Wie bezahle ich?',
             'antwort' => 'Einzelstunden direkt vor Ort oder per Überweisung. Pakete und Kurse bekommst du als Rechnung.'],
            ['frage' => 'Kann ich ein Paket verschenken?',
             'antwort' => 'Ja. Sag mir den Namen, dann bekommst du einen Gutschein zum Ausdrucken.'],
            ['frage' => 'Was passiert, wenn ein Paket abläuft?',
             'antwort' => 'Ich melde mich vorher, wenn noch Einheiten offen sind. In der Regel finden wir einen Weg.'],
        ]]),
    ]),
]);

/* ---------------------------------------------------------------- Termine */
seite([
    'titel' => 'Termine', 'slug' => 'termine', 'im_menue' => 0, 'position' => 5,
    'seo' => Util::json(['titel' => 'Freie Termine · Max Mustermann Golf',
        'beschreibung' => 'Freie Trainingstermine in Musterstadt online buchen — ohne Konto.']),
    'bloecke' => Util::json([
        bl('hero', ['obertitel' => 'Termine', 'titel' => 'Freie Termine.',
            'text' => 'Such dir eine Zeit aus, die passt. Du brauchst dafür kein Konto.',
            'ausrichtung' => 'links', 'hoehe' => 'klein',
            'knopf_text' => '', 'knopf2_text' => '', 'notiz' => '', 'fakten' => '']),
        bl('buchung', ['obertitel' => '', 'titel' => '', 'text' => '', 'wochen' => 4]),
        bl('spalten', ['titel' => 'So läuft die Buchung', 'text' => '', 'eintraege' => [
            ['icon' => 'calendar', 'titel' => 'Zeit wählen',
             'text' => 'Leistung aussuchen, freien Termin anklicken. Was belegt ist, siehst du gar nicht erst.'],
            ['icon' => 'user', 'titel' => 'Deine Angaben',
             'text' => 'Name, E-Mail, Telefon. Mehr brauche ich nicht, um den Termin zu bestätigen.'],
            ['icon' => 'check', 'titel' => 'Bestätigung',
             'text' => 'Du bekommst die Bestätigung per E-Mail und eine Erinnerung am Tag davor.'],
        ]]),
        bl('konto', []),
    ]),
]);

/* ---------------------------------------------------------------- Kontakt */
seite([
    'titel' => 'Kontakt', 'slug' => 'kontakt', 'im_menue' => 1, 'position' => 6,
    'seo' => Util::json(['titel' => 'Kontakt · Max Mustermann Golf',
        'beschreibung' => 'Fragen zum Training? Schreib kurz, was du vorhast — Antwort meistens am selben Tag.']),
    'bloecke' => Util::json([
        bl('hero', ['obertitel' => 'Kontakt', 'titel' => 'Schreib mir.',
            'text' => 'Du willst anfangen, hast eine Frage oder bist unsicher, was passt? '
                    . 'Eine kurze Nachricht reicht.',
            'ausrichtung' => 'links', 'hoehe' => 'klein',
            'knopf_text' => '', 'knopf2_text' => '', 'notiz' => '', 'fakten' => '']),
        bl('formular', ['titel' => '', 'text' => '', 'knopf_text' => 'Nachricht senden',
            'bestaetigung' => 'Danke — ich melde mich, meistens noch am selben Tag.']),
        bl('kontakt', ['obertitel' => 'Anfahrt', 'titel' => 'Wo wir trainieren',
            'text' => 'Im Sommer auf der Anlage, im Winter im Indoor-Studio. Welcher Ort gerade gilt, '
                    . 'steht beim jeweiligen Termin.',
            'karte' => true, 'location_id' => (int) $ids['platz']]),
    ]),
]);

/* ------------------------------------------------------------------- Blog */
$kat = Tenant::insert('categories', ['name' => 'Training', 'slug' => 'training', 'art' => 'blog']);
$beitraege = [
    ['Die drei häufigsten Fehler beim Putten',
     'Zu schneller Rückschwung, wandernder Kopf, fehlende Routine — und was dagegen hilft.',
     "Putten sieht einfach aus, und genau darin liegt das Problem: Weil die Bewegung klein ist, übt sie "
   . "kaum jemand ernsthaft. Dabei entscheidet sie über fast vierzig Prozent aller Schläge.\n\n"
   . "**Der Rückschwung ist zu schnell.** Wer den Putter zurückreißt, muss im Durchschwung abbremsen. "
   . "Zähl beim Üben laut mit: eins zurück, zwei durch. Das klingt albern und wirkt sofort.\n\n"
   . "**Der Kopf geht mit.** Der Blick folgt dem Ball, bevor er getroffen ist. Übung: nach dem Treffen "
   . "bis drei zählen, bevor du aufschaust.\n\n"
   . "**Keine Routine.** Auf dem Übungsgrün funktioniert alles, auf der Runde nicht. Leg dir eine feste "
   . "Abfolge zu: Linie lesen, zwei Probeschwünge, ansprechen, putten. Immer dieselbe."],
    ['Platzreife: Was dich tatsächlich erwartet',
     'Ablauf, Kosten, Dauer — und was vorher selten jemand sagt.',
     "Die Platzreife ist keine Prüfung im schulischen Sinn, auch wenn der Name danach klingt. Sie ist "
   . "der Nachweis, dass du dich auf einem Golfplatz sicher bewegen kannst.\n\n"
   . "**Der Ablauf.** Bei mir sind es acht Einheiten à 90 Minuten. Die ersten vier auf der Übungsanlage, "
   . "danach der Kurzplatz und zum Schluss neun Löcher.\n\n"
   . "**Was es kostet.** 349 Euro inklusive Leihschläger, Bällen und Prüfungsgebühr.\n\n"
   . "**Was selten jemand sagt.** Die Platzreife ist der Anfang, nicht das Ziel. Danach beginnt das "
   . "eigentliche Lernen. Wer das weiß, geht entspannter in den Kurs und hat mehr davon."],
    ['Drei Schläge weniger in einer Saison',
     'Der realistische Weg — und warum die meisten zu viel auf einmal wollen.',
     "Drei Schläge in einer Saison sind ein gutes Ziel. Nicht zehn. Wer zehn will, arbeitet an allem "
   . "gleichzeitig und verbessert nichts.\n\n"
   . "**So funktioniert es.** Wir suchen den einen Bereich, in dem du am meisten verlierst. Bei den "
   . "meisten ist es das Kurzspiel innerhalb von 50 Metern. Dort arbeiten wir acht bis zwölf Wochen "
   . "konzentriert. Danach der nächste Bereich — nacheinander, nicht parallel.\n\n"
   . "**Der Aufwand.** Eine Stunde Unterricht alle zwei Wochen, zwei eigene Einheiten pro Woche à "
   . "45 Minuten. Das ist realistisch neben Beruf und Familie und reicht für drei Schläge."],
];
foreach ($beitraege as $i => [$titel, $auszug, $text]) {
    Tenant::insert('posts', [
        'titel' => $titel, 'slug' => Util::slug($titel), 'auszug' => $auszug, 'text' => $text,
        'category_id' => $kat, 'tags' => 'Training, Tipps', 'user_id' => (int) $ids['max'],
        'status' => 'veroeffentlicht',
        'seo' => Util::json(['titel' => Util::kuerzen($titel . ' · Max Mustermann Golf', 60),
                             'beschreibung' => Util::kuerzen($auszug, 155)]),
        'veroeffentlicht' => date('Y-m-d H:i:s', strtotime('-' . ($i * 26 + 9) . ' days')),
        'aufrufe' => 0,
        'erstellt' => date('Y-m-d H:i:s', strtotime('-' . ($i * 26 + 11) . ' days')),
    ]);
}

/* Blogblock in die Startseite, vor den Kontaktabschnitt */
$start = Tenant::one('pages', "slug = 'start'");
$bloecke = json_decode((string) $start['bloecke'], true);
$pos = null;
foreach ($bloecke as $i => $b) { if ($b['typ'] === 'kontakt') { $pos = $i; break; } }
array_splice($bloecke, $pos === null ? count($bloecke) : $pos, 0,
    [bl('blog', ['titel' => 'Aus der Praxis', 'anzahl' => 3])]);
Tenant::update('pages', (int) $start['id'], ['bloecke' => Util::json($bloecke)]);

echo "4 weitere Seiten, 3 Beiträge, Blogblock eingefügt\n";
