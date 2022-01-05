<!doctype html>
 <head>

 </head>
 <body>
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
            
            for ($i=1; $i<1000; $i++) {
                kwadratx(rand(1, 99999),rand(1,5));
            }
        
        
        ?>
 </body>
</html>