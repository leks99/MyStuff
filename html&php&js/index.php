<!doctype html> 
    |<head>
        <meta charset="utf8">
        <title>Moja Stronka :)</title>
        
        <style>
            .cos{
                padding: 5px;
                border: 2px solid black; 
            }
            .ball8{
                position: relative;
                text-align: center;
                color: white;
            }
            .ball8content{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 40px;
            }
        </style>

    </head>


    <body>
        <?php
        $height = 9;
        $index = 1;
        $s = (int) ($height-1);
        echo("<pre>");
        for($i = 0; $i<=$height; $i++) { 
            for($j = 0; $j<=$s;$j++) {
                echo (" ");
            }
            for($k = 0; $k<$index;$k++) {
                echo ("*");
            }
            echo("<br>");
            $index += 2;
            $s -= 1;
        }
        for($i=0;$i<(int)(($height*2)/2-1);$i++) {
            echo(" ");
        }
        echo("|_|");
        echo("</pre>");
        ?>
        <h1 style="color:rgb(5, 18, 196);font-size:50px;">dzień dobry</h1> 
        
        <?php 
            //-------------------------licznik bazy
            //połączenie
            $host = "localhost";
            $uname = "admin";
            $passwd = "admin";
            $base = "stronkaBaza";

            $conn = mysqli_connect($host, $uname, $passwd, $base);

            //połączenie check
            if(!$conn) {
                echo ("conn error: ").mysqli_connect_error();
            }

            //branie danch
            $sql = "SELECT * FROM wyswietlenia";
            $result = mysqli_query($conn, $sql);
            $wyswietleniaA = mysqli_fetch_all($result, MYSQLI_ASSOC);
            $wyswietlenia = $wyswietleniaA[0]["liczbaWyswietlen"]+1;
            //pisanie danych
            $wyswietleniaI = mysqli_real_escape_string($conn, $wyswietlenia);
            $sql = "UPDATE wyswietlenia SET liczbaWyswietlen = '$wyswietleniaI'";
            if(mysqli_query($conn, $sql)) {
                //dobrze
            }
            else {
                echo ('error: '.mysqli_error($conn)); //zle
            }

            //estetyka
            mysqli_free_result($result);
            mysqli_close($conn);

            //wyswietla
            echo("<b>liczba wyświetleń na tej stronie: </b>".$wyswietlenia);
        ?>
        
        
        <pre>



        </pre>
        
        <?php 
        include "skrypt.php";
        include "lekcja3.php";
        include "funkcje.php";

        //kom
        
        echo("cześć"); 
        /* kom blokowy
        i
        wgl */
        //-------------------------------------------lekcja3-------------------------------------------
        //$pin = $argv[1]; 
        ?>
        
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            wpisz pin:<br> <input type="tekst"  name="pin" id="pin">
        </form>

        <?php

            $pin = $_POST["pin"];
            if ($pin != "0"){
                echo $pin;
            }
        ?>
        <br>
        <?php
            //-------------------------------------------lekcja4-------------------------------------------
            include "lekcja4.php";
        ?>
        <pre>



        </pre>
        <?php 
            //------------------------------------------------lekcja5 - funkcje-----------------------------------------
        ?>

        <?php
            
            for ($i=1; $i<10; $i++) {
                kwadratx(rand(1, 99999),rand(1,5));
            }
        
        
        ?>
            
        <?php 
            //------------------------------------------------lekcja5 - funkcje-----------------------------------------
        ?> <br> <br> 
        
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            wpisz a funkcji:<br> <input type="float"  name="a" id="a">
        </form>

        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            wpisz b funkcji:<br> <input type="float"  name="b" id="b">
        </form>

        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            wpisz c funkcji:<br> <input type="float"  name="c" id="c">
        </form> 

        <?php
            $a = $_POST["a"];
            $b = $_POST["b"];
            $c = $_POST["c"];
            if ($a != "0"){
                echo "$a, $b, $c <br>";
            }
        ?>

        <?php 
        echo "a = $a, b = $b, c = $c <br>";
        if ($a == 0) {
            echo "to nie jest rownanie kwadratowe";
        }
        else {
            $delta = $b * $b - 4* $a * $c;
            echo "delta to $delta <br>";
            if ($delta < 0) {
                echo "i nie ma rozwiązań";
            }
            elseif ($delta == 0) {
                $wynik = -$b / 2*$a;
                echo "rozwiązanie: x = $wynik";
            }
            else {
                $wynik = (-$b + sqrt($delta)) / (2 * $a);
                echo "x1 = $wynik <br>";
                $wynik = (-$b - sqrt($delta)) / (2 * $a);
                echo "x2 = $wynik <br>";
            }
        }
        ?>
        <?php 
            //------------------------------------------------lekcja6-----------------------------------------
        ?> <br> <br>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            zadaj pytanie do all mighty cube-a:<br> <input type="text"  name="pytanie" id="pytanie">
        </form> <br>
        <?php
            $pytanie = " ";
            $odp = " ";
            $pytanie = $_POST["pytanie"];
            $losX = rand(1,9);
            if ($losX == 1) {
                $odp = "możliwe";
            }
            elseif ($losX == 2) {
                $odp = "prawdopodobnie tak";
            }
            elseif ($losX == 3) {
                $odp = "raczej nie";
            }
            elseif ($losX == 4) {
                $odp = "mało prawdopodobne";
            }
            elseif ($losX == 5) {
                $odp = "na pewno nie";
            }
            elseif ($losX == 6) {
                $odp = "na pewno tak";
            }
            elseif ($losX == 7) {
                $odp = "to zależy ";
            }
            elseif ($losX == 8) {
                $odp = "nawet kula tego nie wie";
            }
            elseif ($losX == 9) {
                $odp = "szanse na to są małe";
            }
            if ($odp != " ") {
                echo "pytanie:$pytanie <br> $odp";
            }
        ?>

        <div class="ball8">
            <img src="8ball.png" alt="ball" style="width:100%;">
            <div class="ball8content"><?php  echo "pytanie:$pytanie <br> $odp"; ?></div>
        </div> 

        <!-- tablice          0           1          2
            $table=array("element1", "element2", "element3"...) 
         -->

        <h3>Tablice</h3>
        <?php 
        
        $tanie_wina = [2.34, "Snajper", 3.45, "leśny dzban", 5.60, "Amarena", 4.50, "Mamarot"];
        $marki=array("opel","toyota","audi","ford","honda");
        echo count($marki); echo "<br>";
        print_r($marki);echo "<br>";
        echo implode(",", $marki);echo "<br>";
        echo count($tanie_wina); echo "<br>";
        print_r($tanie_wina);echo "<br>";
        echo implode(", ", $tanie_wina);echo "<br>";
        for ($i=0; $i<count($tanie_wina); $i = $i + 2) {
            $j = $i + 1;
            echo "$tanie_wina[$i]-$tanie_wina[$j]";echo "<br>";
        }

        echo("<br>");
        echo("------------------------");echo("<br>");echo("<br>");

        $liczba = 4;
        echo ($liczba);
        echo ("<br>");
        if (parzysta($liczba)) {
            echo("parzysta");
        }
        else {
            echo("nie parzysta");
        }

        echo ("<br>");
        if (pierwsza($liczba)) {
            echo("liczba jest pierwsza");
        }
        else {
            echo("liczba nie jest pierwsza");
        } echo ("<br>");

        echo("silnia =".silnia($liczba));echo("<br>");

        troj(2,3,5,4); echo("<br>");
        echo("---------------------------");
        echo("<br>");

        echo("odtworzenia strony: ");
        $plik = fopen("plik.txt","r");
        $x = fgets($plik);
        $x = $x+1;
        $plik = fopen("plik.txt", "w");
        fwrite($plik, $x);
        echo($x);
        fclose($plik);


        ?>

        <?php
            //----------------------------------------------------------------------
        ?> <br><br>
        <img src="1.gif" alt="this slowpoke moves"  width="250" />
        <p></p>
        <img src="2.gif" alt="this slowpoke moves"  width="250" />
        <p></p>
        <img src="3.gif" alt="this slowpoke moves"  width="250" />
        <p></p>
        <img src="4.gif" alt="this slowpoke moves"  width="250" />
        <p></p>
        <img src="5.gif" alt="this slowpoke moves"  width="250" />


    </body>




</html>

