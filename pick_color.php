<html>
<head>
<script type="text/javascript" src="jscolor/jscolor.js"></script>
</head>
<body>

<?php
$host = "192.168.1.235";
$port = "9999";
$socket  = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP)
        or die("Unable to create socket\n");


$color = $_GET['color'];

print '<form action="pick_color.php">';
print '<input class="color" value="' . $color . '" name="color" id="myColor">';
print '<input type="submit" value="Submit">';
print '</form>';

$r = substr($color,0,2);
$g = substr($color,2,2);
$b = substr($color,4,2);

$led = chr(hexdec($r)).chr(hexdec($g)).chr(hexdec($b));

for ($i=0; $i<144; $i++) {
  $msg .= $led;
}

$sock_data = socket_connect($socket, $host, $port);
$sock_data = socket_write($socket, $msg, strlen($msg));
socket_close($sock);


?>

</body>
</html>
