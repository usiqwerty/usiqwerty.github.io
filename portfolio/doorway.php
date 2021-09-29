<link rel="stylesheet" href="style.css">
<?php
$dbconn = pg_connect("dbname=localdb user=postgres password=administrator host=127.0.0.1 port=5432");
if (!$dbconn){
	die('Could not connect: ' . pg_last_error());
}

$user=$_POST['username'];
$pass=md5($_POST['password']);
$q=$_POST['q'];
$query = "SELECT * FROM users WHERE name='" . $user . "';";

$result = pg_query($dbconn, $query) or die('Query failed: ' . pg_last_error());
$row=pg_fetch_row($result);



if ($row[1]!=$user)
	$unique=true;

function gencookie(){
	global $user, $pass;
	return md5( $user . $pass );
}

function reg(){
	if ($unique){
		global $dbconn, $user, $pass;
		$query = "INSERT INTO users (name, pass) VALUES ('$user', '$pass')";
		echo $query;
		pg_query($dbconn, $query) or die('Query failed: ' . pg_last_error($dbconn));
		print ("<body id=success>");
		print ("<center><h1>Welcome, " . $user . " </h1></center><marquee>Registration completed</marquee>");
		setcookie('username', $user, time()+2147483647);
		setcookie("login", gencookie(), time()+2147483647);
	}
	else {
		print("<center><h1>Username is already used</h1></center>");
	}
}
function login(){

	global $user, $pass, $row;
	print ($pass . " ");
	
	print ($row[2]);
	//md5 of input vs. md5 in DB
	if ($pass != $row[2]){
		print("<center><h1>You're wrong!</h1></center>");
	}
	else{
		print ( "<body id=success>");
		print ("<center><h1>Welcome, " . $user . " </h1></center><marquee>You have successfully logged in</marquee>");
		setcookie('username', $user, time()+2147483647);
		setcookie("login", gencookie(), time()+2147483647);
	}
}

if ($q=='r'){
	reg();
}
else{
	login();
}
pg_close($dbconn);
?>

</body>
