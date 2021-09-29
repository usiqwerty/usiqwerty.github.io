<?php
echo ('');

$dbconn = pg_connect("dbname=localdb user=postgres password=administrator host=127.0.0.1 port=5432");
if (!$dbconn){
	die('Could not connect: ' . pg_last_error());
}
$user=$_COOKIE['username'];

$query = "SELECT * FROM users WHERE name='" . $user . "';";
$result = pg_query($dbconn, $query) or die('Query failed: ' . pg_last_error());
$row=pg_fetch_row($result);

function gencookie(){
	global $row;
	return md5( $row[1] . $row[2] );
}

if ($_COOKIE['login'] == gencookie())
	header('Location: /home.php');
else
	echo (file_get_contents('index.html'));
pg_close($dbconn);
?>

