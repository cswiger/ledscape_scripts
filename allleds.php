<html>
<head/>
<body>

<?php 
$host = "192.168.1.235";
$port = "9999";
$socket  = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP)
	or die("Unable to create socket\n");

print 'sending to ledscape host '.$host.' and port '.$port.'<br />';

$r = $_GET["r"];
$g = $_GET["g"];
$b = $_GET["b"];

$led = chr($r).chr($g).chr($b);

for ($i=0; $i<144; $i++) {
  $msg .= $led;
}


$sock_data = socket_connect($socket, $host, $port);
$sock_data = socket_write($socket, $msg, strlen($msg));
socket_close($sock);

?>
</body>
</html>
