<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
        if(!isset($_GET["fpytanie"])) {
            $_GET["fpytanie"]="";
        }
        $pytanie = $_GET['fpytanie'];
        $fg = fopen("prezenty.txt", "a");
        if($pytanie!="") {

            fwrite($fg, "\n".$pytanie);
        }
        fclose($fg);

    ?>
    <?php
    echo("<ul>");
        $fg = fopen("prezenty.txt","r");
        while (!feof($fg)) {
            $prezent = trim(fgets($fg));
            echo("<li>$prezent</li>");
        }
    echo("</ul>");
    fclose($fg);
    ?>
    <br>
    <form action="prezenty.php" method="$_GET">
        rzyczenie:
        <input type="text" name="fpytanie">
        <input type="submit">
    </form>
</body>
</html>