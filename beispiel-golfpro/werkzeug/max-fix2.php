<?php
require __DIR__ . '/cms/lib/bootstrap.php';
$ids = json_decode((string) file_get_contents(__DIR__ . '/max-ids.json'), true);
Tenant::setzen((int) $ids['ws']);
$n = 0;
foreach (Tenant::all('pages') as $s) {
    if ((int) $s['startseite'] === 1) { continue; }   // Startseite behält das Bild
    $b = json_decode((string) $s['bloecke'], true);
    foreach ($b as &$block) {
        if ($block['typ'] === 'hero') { $block['daten']['ausrichtung'] = 'mitte'; $n++; }
    }
    unset($block);
    Tenant::update('pages', (int) $s['id'], ['bloecke' => Util::json($b)]);
}
echo "$n Aufmacher auf 'mitte' gestellt\n";
