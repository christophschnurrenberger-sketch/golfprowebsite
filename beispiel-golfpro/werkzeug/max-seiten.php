<?php
require __DIR__ . '/cms/lib/bootstrap.php';
$ids = json_decode((string) file_get_contents(__DIR__ . '/max-ids.json'), true);
Tenant::setzen((int) $ids['ws']);
DB::query("DELETE FROM pages WHERE workspace_id = " . (int) $ids['ws']);
DB::query("DELETE FROM posts WHERE workspace_id = " . (int) $ids['ws']);
DB::query("DELETE FROM categories WHERE workspace_id = " . (int) $ids['ws']);

function bl(string $typ, array $daten = []): array {
    $b = Bloecke::neu($typ);
    $b['daten'] = array_merge($b['daten'], $daten);
    return $b;
}
function seite(array $d): int { return Tenant::insert('pages', $d + [
    'status' => 'veroeffentlicht', 'aufrufe' => 0, 'conversions' => 0,
    'geaendert' => date('Y-m-d H:i:s', strtotime('-9 days')),
    'erstellt' => date('Y-m-d H:i:s', strtotime('-2 years')),
]); }

$FAQ = [
    ['frage' => 'Brauche ich Vorkenntnisse?',
     'antwort' => 'Nein. Ein guter Teil meiner Schüler hat vor der ersten Stunde noch nie einen Schläger in der Hand gehabt.'],
    ['frage' => 'Wie läuft eine Einzelstunde ab?',
     'antwort' => "Wir fangen mit ein paar Schlägen an, damit ich sehe, wo du stehst. Danach suchen wir eine Sache aus, an der wir arbeiten. Am Ende bekommst du kurz schriftlich, was du bis zum nächsten Mal üben solltest."],
    ['frage' => 'Was soll ich mitbringen?',
     'antwort' => 'Bequeme Kleidung und feste Schuhe. Schläger und Bälle stelle ich, solange du noch keine eigenen hast.'],
    ['frage' => 'Wo findet das Training statt?',
     'antwort' => 'Im Sommer auf der Anlage, im Winter im Indoor-Studio. Welcher Ort gerade gilt, steht beim jeweiligen Termin.'],
    ['frage' => 'Wie lange dauert es bis zur Platzreife?',
     'antwort' => 'Der Kurs hat acht Einheiten. Viele brauchen dazwischen noch ein paar Runden Übung. Rechne mit sechs bis zehn Wochen, wenn du regelmäßig kommst.'],
    ['frage' => 'Kann ich einen Termin verschieben?',
     'antwort' => 'Ja, bis 24 Stunden vorher. Danach wird die Einheit berechnet.'],
];

/* ------------------------------------------------------------- Startseite */
seite([
    'titel' => 'Startseite', 'slug' => 'start', 'startseite' => 1, 'im_menue' => 0, 'position' => 0,
    'seo' => Util::json([
        'titel' => 'Golfunterricht in Musterstadt · Max Mustermann Golf',
        'beschreibung' => 'Golftraining für Einsteiger, Fortgeschrittene und Junioren in Musterstadt. '
                        . 'Platzreifekurs, Videoanalyse und Einzelstunden. Termine online buchen.',
    ]),
    'bloecke' => Util::json([
        bl('hero', [
            'obertitel' => 'PGA Golf Professional',
            'titel' => 'Besser Golf spielen beginnt mit dem *richtigen Training.*',
            'text' => 'Ich unterrichte Einsteiger auf dem Weg zur Platzreife und Spieler, die vom '
                    . 'mittleren ins einstellige Handicap wollen. In kleinen Gruppen oder einzeln, '
                    . 'mit festem Ablauf und ohne den Druck, schon etwas können zu müssen.',
            'knopf_text' => 'Freie Termine ansehen', 'knopf_url' => '#buchung',
            'knopf2_text' => 'Preise ansehen', 'knopf2_url' => '?w=max&seite=preise',
            'notiz' => 'Erste Stunde? Schläger und Bälle stelle ich — Sportschuhe genügen.',
            'fakten' => 'PGA Professional · Kleine Gruppen · Prüfung inklusive',
            'ausrichtung' => 'geteilt', 'hoehe' => 'normal',
        ]),
        bl('spalten', [
            'titel' => 'Was dich erwartet',
            'text' => 'Drei Dinge, die bei mir immer gleich sind.',
            'eintraege' => [
                ['icon' => 'customers', 'titel' => 'Kleine Gruppen',
                 'text' => 'Höchstens sechs Teilnehmer. So bleibt genug Zeit für jeden Einzelnen.'],
                ['icon' => 'gift', 'titel' => 'Alles inklusive',
                 'text' => 'Leihschläger, Bälle und Unterlagen sind dabei. Du brauchst nur bequeme Schuhe.'],
                ['icon' => 'list', 'titel' => 'Fester Ablauf',
                 'text' => 'Du weißt von Anfang an, was in welcher Woche drankommt und wann die Prüfung ist.'],
            ],
        ]),
        bl('leistungen', [
            'titel' => 'Golftraining, das zu dir passt.',
            'text' => 'Was für dich passt, klären wir am besten kurz vorher.',
            'automatisch' => true,
        ]),
        bl('zahlen', ['eintraege' => [
            ['wert' => '20', 'label' => 'Jahre auf dem Platz'],
            ['wert' => '12', 'label' => 'Jahre als Trainer'],
            ['wert' => '6', 'label' => 'Teilnehmer höchstens'],
            ['wert' => '8', 'label' => 'Einheiten bis zur Platzreife'],
        ]]),
        bl('buchung', [
            'obertitel' => 'Termine',
            'titel' => 'Such dir eine Zeit aus, die passt.',
            'text' => 'Du brauchst dafür kein Konto. Wenn du eins anlegst, siehst du später deine '
                    . 'Termine, Pakete und Rechnungen an einer Stelle.',
            'wochen' => 3,
        ]),
        bl('faq', ['titel' => 'Häufige Fragen', 'eintraege' => $FAQ]),
        bl('konto', []),
        bl('kontakt', ['titel' => 'Wo wir trainieren', 'karte' => true,
                       'location_id' => (int) $ids['platz']]),
    ]),
]);

/* ------------------------------------------------------------- Über mich */
seite([
    'titel' => 'Über mich', 'slug' => 'ueber-mich', 'im_menue' => 1, 'position' => 1,
    'seo' => Util::json(['titel' => 'Über mich · Max Mustermann Golf',
        'beschreibung' => 'PGA Golf Professional in Musterstadt. Zwanzig Jahre auf dem Platz, zwölf davon als Trainer.']),
    'bloecke' => Util::json([
        bl('hero', ['obertitel' => 'Der Trainer', 'titel' => 'Max Mustermann',
            'text' => 'PGA Golf Professional. Zwanzig Jahre auf dem Platz, zwölf davon als Trainer.',
            'ausrichtung' => 'links', 'hoehe' => 'klein',
            'knopf_text' => '', 'knopf2_text' => '', 'notiz' => '', 'fakten' => '']),
        bl('text', ['titel' => 'Wie ich dazu gekommen bin', 'text' =>
            "Angefangen habe ich wie die meisten: mit einem geliehenen Schläger und der festen "
          . "Überzeugung, dass Golf schnell gehen müsste. Es ging nicht schnell. Genau deshalb "
          . "unterrichte ich heute gern Einsteiger — ich weiß noch, wie sich die ersten Wochen anfühlen.\n\n"
          . "Nach der Ausbildung zum PGA Professional habe ich einige Jahre im Clubbetrieb gearbeitet, "
          . "bevor ich mich selbstständig gemacht habe. Seitdem gebe ich Einzelstunden, Gruppentrainings "
          . "und Platzreifekurse, im Sommer auf der Anlage und im Winter im Indoor-Studio.\n\n"
          . "Mein Unterricht ist eher ruhig als laut. Ich ändere nicht alles auf einmal, sondern eine "
          . "Sache nach der anderen. Was wir in der Stunde erarbeiten, bekommst du schriftlich mit, damit "
          . "du auch zwischen zwei Terminen weißt, woran du arbeitest."]),
        bl('zitat', ['text' => 'Wenn du unsicher bist, ob Golf etwas für dich ist: Komm einfach mal für '
            . 'eine halbe Stunde vorbei. Danach weißt du mehr als nach jedem Prospekt.',
            'autor' => 'Max Mustermann']),
        bl('cta', ['titel' => 'Lust, es auszuprobieren?',
            'text' => 'Eine halbe Stunde reicht für den ersten Eindruck. Schläger und Bälle stelle ich.',
            'knopf_text' => 'Freie Termine ansehen', 'knopf_url' => '?w=max&seite=termine',
            'notiz' => 'Anrufen geht meistens schneller: 0123 4567890']),
    ]),
]);

/* --------------------------------------------------------- Golfunterricht */
seite([
    'titel' => 'Golfunterricht', 'slug' => 'golfunterricht', 'im_menue' => 1, 'position' => 2,
    'seo' => Util::json(['titel' => 'Golfunterricht in Musterstadt · Max Mustermann Golf',
        'beschreibung' => 'Einzeltraining, Gruppentraining, Platztraining und Videoanalyse. Preise und Ablauf im Überblick.']),
    'bloecke' => Util::json([
        bl('hero', ['obertitel' => 'Unterricht', 'titel' => 'Golftraining, das zu dir passt.',
            'text' => 'Vier Wege, mit dem Training anzufangen oder weiterzukommen. Was für dich passt, '
                    . 'klären wir am besten kurz vorher.',
            'ausrichtung' => 'links', 'hoehe' => 'klein',
            'knopf_text' => 'Termin buchen', 'knopf_url' => '?w=max&seite=termine',
            'knopf2_text' => '', 'notiz' => '', 'fakten' => '']),
        bl('leistungen', ['titel' => '', 'text' => '', 'automatisch' => false, 'eintraege' => [
            ['titel' => 'Einzeltraining', 'preis' => 'ab 49 €', 'dauer' => '30 oder 60 Minuten',
             'wer' => 'Alle, die gezielt an etwas arbeiten wollen',
             'text' => 'Eine Stunde nur für dich. Wir schauen uns an, wo es hakt, und arbeiten an genau '
                     . 'der einen Sache, die gerade den größten Unterschied macht.',
             'note' => '60 Minuten 89 € · 30 Minuten 49 €'],
            ['titel' => 'Gruppentraining', 'preis' => '39 €', 'dauer' => '90 Minuten',
             'wer' => 'Einsteiger und Wiedereinsteiger',
             'text' => 'Höchstens sechs Teilnehmer. Günstiger als Einzelunterricht und für viele '
                     . 'angenehmer, weil man sieht, dass alle mit denselben Dingen kämpfen.'],
            ['titel' => 'Platztraining', 'preis' => '149 €', 'dauer' => '120 Minuten',
             'wer' => 'Alle mit Platzreife',
             'text' => 'Neun Löcher gemeinsam auf der Runde. Hier geht es weniger um Technik als um '
                     . 'Entscheidungen: Welcher Schläger, welches Ziel, wann Risiko.'],
            ['titel' => 'Videoanalyse', 'preis' => '119 €', 'dauer' => '60 Minuten',
             'wer' => 'Spieler, die verstehen wollen, warum etwas passiert',
             'text' => 'Wir nehmen deinen Schwung auf und gehen ihn Bild für Bild durch. Du bekommst die '
                     . 'Aufnahme mit den Markierungen mit nach Hause.'],
        ]]),
        bl('faq', ['titel' => 'Bevor du buchst', 'eintraege' => array_slice($FAQ, 0, 4)]),
        bl('cta', ['titel' => 'Welche Form passt?',
            'text' => 'Wenn du unsicher bist, schreib kurz, was du vorhast. Ich sage dir, womit ich anfangen würde.',
            'knopf_text' => 'Kurz schreiben', 'knopf_url' => '?w=max&seite=kontakt',
            'notiz' => 'Antwort meistens am selben Tag.']),
    ]),
]);

echo "3 Seiten\n";
