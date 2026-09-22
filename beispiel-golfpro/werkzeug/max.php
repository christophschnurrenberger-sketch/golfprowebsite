<?php
/**
 * Legt den Beispiel-Workspace "Max Mustermann Golf" an.
 *
 * Kein Eingriff ins CMS: Das Skript liegt ausserhalb und benutzt nur die
 * oeffentlichen Klassen, so wie es der Baukasten selbst tut. Die Texte
 * stammen aus TEXTE.md, die Preise aus derselben Tabelle wie dort.
 */
require __DIR__ . '/cms/lib/bootstrap.php';

$alt = DB::one("SELECT * FROM workspaces WHERE slug = 'max'");
if ($alt) {
    $id = (int) $alt['id'];
    foreach (DB::all("SELECT name FROM sqlite_master WHERE type='table'") as $r) {
        $t = (string) $r['name'];
        foreach (DB::all("PRAGMA table_info(\"$t\")") as $sp) {
            if ($sp['name'] === 'workspace_id') {
                DB::query("DELETE FROM \"$t\" WHERE workspace_id = $id");
                break;
            }
        }
    }
    DB::query("DELETE FROM workspaces WHERE id = $id");
    echo "alter Bestand entfernt\n";
}

function bl(string $typ, array $daten): array {
    $b = Bloecke::neu($typ);
    $b['daten'] = array_merge($b['daten'], $daten);
    return $b;
}

$ws = DB::insert('workspaces', [
    'slug' => 'max', 'name' => 'Max Mustermann Golf', 'typ' => 'pro', 'plan' => 'pro',
    'domain' => '',
    'branding' => Util::json([
        'primaer' => '#1E4B54', 'akzent' => '#C9922E',
        'schrift' => 'Archivo', 'radius' => 6, 'stil' => 'modern',
    ]),
    'waehrung' => 'EUR', 'sprache' => 'de', 'onboarding_schritt' => 9,
    'aktiv' => 1, 'demo' => 1,
    'erstellt' => date('Y-m-d H:i:s', strtotime('-3 years')),
]);
Tenant::setzen($ws);

foreach ([
    'module' => Module::standardFuerPlan('pro'),
    'steuersatz' => 19, 'zahlungsziel_tage' => 14, 'rechnung_praefix' => 'R',
    'kopf_zusatz' => 'Golfschule · Musterstadt',
    'telefon' => '0123 4567890',
    'unterrichtszeiten' => 'Di – Sa, nach Vereinbarung',
    'stornofrist_stunden' => 24,
    'website_beschreibung' => 'Golfunterricht in Musterstadt: Einzeltraining, Gruppen, '
                            . 'Platzreifekurs und Videoanalyse. Termine online buchen.',
    'mail_absender_name' => 'Max Mustermann Golf',
    'rechnung_absender' => 'Max Mustermann Golf · Musterweg 12 · 12345 Musterstadt',
] as $k => $v) { Tenant::einstellungSetzen($k, $v); }

$max = Tenant::insert('users', [
    'email' => 'max@maxmustermann-demo.de', 'passwort' => Auth::hash(Util::token(16)),
    'name' => 'Max Mustermann', 'rolle' => 'owner',
    'titel' => 'PGA Golf Professional',
    'telefon' => '0123 4567890',
    'bio' => 'Zwanzig Jahre auf dem Platz, zwölf davon als Trainer. Schwerpunkt: '
           . 'Einsteiger auf dem Weg zur Platzreife und Spieler, die vom mittleren '
           . 'ins einstellige Handicap wollen.',
    'aktiv' => 1, 'erstellt' => date('Y-m-d H:i:s', strtotime('-3 years')),
]);

$platz = Tenant::insert('locations', [
    'name' => 'Golfanlage Musterstadt', 'typ' => 'club',
    'strasse' => 'Musterweg 12', 'plz' => '12345', 'ort' => 'Musterstadt',
    'notiz' => 'Driving Range, zwei Übungsgrüns und Kurzplatz.',
    'farbe' => '#1E4B54', 'aktiv' => 1,
]);
$indoor = Tenant::insert('locations', [
    'name' => 'Indoor-Studio Musterstadt', 'typ' => 'indoor',
    'strasse' => 'Bahnhofstraße 7', 'plz' => '12345', 'ort' => 'Musterstadt',
    'notiz' => 'Zwei Abschlagplätze mit Launch Monitor. Ganzjährig.',
    'farbe' => '#C9922E', 'aktiv' => 1,
]);

/* Leistungen – dieselben Preise wie in der Preistabelle in TEXTE.md */
$dienste = [
    ['Einzeltraining 60 Minuten', 'einzel', 60, 8900, 1,
     'Eine Stunde nur für dich. Wir schauen uns an, wo es hakt, und arbeiten an genau der einen Sache, die gerade den größten Unterschied macht.'],
    ['Einzeltraining 30 Minuten', 'einzel', 30, 4900, 1,
     'Kurze Einheit für einen konkreten Punkt. Gut zwischendurch oder zur Vorbereitung auf eine Runde.'],
    ['Gruppentraining 90 Minuten', 'gruppe', 90, 3900, 6,
     'Höchstens sechs Teilnehmer. Günstiger als Einzelunterricht und für viele angenehmer.'],
    ['Platztraining 9 Löcher', 'einzel', 120, 14900, 2,
     'Neun Löcher gemeinsam auf der Runde. Weniger Technik, mehr Entscheidungen: Schläger, Ziel, Risiko.'],
    ['Videoanalyse 60 Minuten', 'video', 60, 11900, 1,
     'Wir nehmen deinen Schwung auf und gehen ihn Bild für Bild durch. Die Aufnahme bekommst du mit.'],
    ['Platzreifekurs (8 Einheiten)', 'kurs', 90, 34900, 6,
     'Acht Einheiten von der ersten Berührung mit dem Schläger bis zur Prüfung. Leihschläger und Bälle sind dabei.'],
    ['Juniorentraining', 'gruppe', 60, 2200, 8,
     'Für Kinder und Jugendliche. Spielerisch, in kleinen Gruppen, mit Material in passender Größe.'],
    ['Online-Coaching (Videocheck)', 'online', 30, 4500, 1,
     'Du schickst ein Video, ich schicke die Analyse mit Übungen zurück.'],
];
$sids = [];
foreach ($dienste as $i => [$name, $art, $dauer, $preis, $kap, $text]) {
    $sids[] = Tenant::insert('services', [
        'name' => $name, 'slug' => Util::slug($name), 'art' => $art,
        'beschreibung' => $text, 'dauer_min' => $dauer, 'puffer_min' => $dauer >= 90 ? 15 : 10,
        'preis_cent' => $preis, 'steuersatz' => 19, 'kapazitaet' => $kap,
        'location_id' => $art === 'online' ? 0 : ($art === 'video' ? $indoor : $platz),
        'trainer_ids' => Util::json([$max]),
        'farbe' => ['#1E4B54','#2C6B77','#6b4ea8','#a6640d','#1d5fa8','#C9922E','#b4242b','#0ea5a5'][$i],
        'online_buchbar' => 1, 'vorlauf_stunden' => 12, 'stornofrist_stunden' => 24,
        'position' => $i, 'aktiv' => 1,
    ]);
}

foreach ([2 => [600, 1080], 3 => [600, 1080], 4 => [600, 1140], 5 => [600, 1020], 6 => [540, 900]] as $tag => [$v, $b]) {
    Tenant::insert('availability', [
        'user_id' => $max, 'location_id' => $platz,
        'wochentag' => $tag, 'von_min' => $v, 'bis_min' => $b, 'aktiv' => 1,
    ]);
}

echo "Workspace $ws angelegt, " . count($sids) . " Leistungen\n";
file_put_contents(__DIR__ . '/max-ids.json', Util::json(
    ['ws' => $ws, 'max' => $max, 'platz' => $platz, 'indoor' => $indoor, 'dienste' => $sids]));
