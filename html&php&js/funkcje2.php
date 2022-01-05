<?php

function parzysta($liczba) {
    if ($liczba % 2 == 0) {
        return True;
    }
    else {
        return FALSE;
    }
}

function pierwsza($liczba) {
    $isPierwsza = TRUE;
    for ($i = 2; $i<$liczba-1; $i++) {
        if ($liczba % $i == 0) {
            $isPierwsza = FALSE;
        }
    }
    return $isPierwsza;
}

function troj($a, $b, $c, $h) {
    $obw = $a + $b + $c;
    $p = ($a * $h) / 2;
    echo("obw =".$obw);
    echo("<br>");
    echo("pole =".$p);
}

function silnia($a) {
    $wynik = 1;
    for ($i = 1; $i <= $a; $i++) {
        $wynik *= $i;
    }
    return $wynik;
}

?>