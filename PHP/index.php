<?php
//Sample Database Connection Syntax for PHP and MySQL.

//Connect To Database

$hostname="eventall.db.5516970.hostedresource.com";
$username="eventall";
$password="CuteF!re77";
$dbname="eventall";
$usertable="eventall2016";
$yourfield = "event_name";

mysql_connect($hostname,$username, $password) or die ("<html><script language='JavaScript'>alert('Unable to connect to database! Please try again later.'),history.go(-1)</script></html>");
mysql_select_db($dbname);

# Check If Record Exists

$query = "SELECT * FROM $usertable";

$result = mysql_query($query);
?>
<html>
    <head>
    </head>
    <body>
        <h1>Welcome to the #1 best event lister</h1>


<?php
if($result)
{
?>
        <table>
            <thead>
                <td>Events</td>
            </thead>
<?php
while($row = mysql_fetch_array($result))
  {
    $name = $row["$yourfield"];
    echo "<tr><td><p>".$name."</p></td></tr>";
  }
} else {
?>
<h2>Nothing to show</h2>
<?php
}
?>
        </table>
    </body>
</html>