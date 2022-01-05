<?php

function kwadratx($cos,$kolornr) {
                if ($kolornr == 1) {
                    $kolor = "red";
                }
                if ($kolornr == 2) {
                    $kolor = "blue";
                }
                if ($kolornr == 3) {
                    $kolor = "green";
                }
                if ($kolornr == 4) {
                    $kolor = "yellow";
                }
                if ($kolornr == 5) {
                    $kolor = "orange";
                }
                $pin = $_POST["pin"];
                echo "<div class='cos' style='background-color: $kolor; width:99%;'>$cos to jest $pin</div>"; 
            }

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