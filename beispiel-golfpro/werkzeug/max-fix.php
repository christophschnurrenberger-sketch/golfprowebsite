<?php
require __DIR__ . '/cms/lib/bootstrap.php';
$ids = json_decode((string) file_get_contents(__DIR__ . '/max-ids.json'), true);
Tenant::setzen((int) $ids['ws']);
$n = 0;
foreach (Tenant::all('pages') as $s) {
    $alt = (string) $s['bloecke'];
    $neu = str_replace('?w=max&seite=', '?w=max&s=', $alt);
    if ($neu !== $alt) { Tenant::update('pages', (int) $s['id'], ['bloecke' => $neu]); $n++; }
}
echo "$n Seiten korrigiert\n";
