<?php

$servername = "35.223.179.70";
$user = "****";
$password = "*****"; 
$database = "milestone4db";
$table = "timesheet";

try {
	$db = new PDO("mysql:host=$servername;dbname=$database", $user, $password);
	$query = "SELECT DISTINCT name, time, confidence, action, tardiness FROM $table WHERE name != 'Name' AND name != 'Unknown'";
	$params = [];

	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$filter = $_POST['filter'];
		if ($filter === 'name' && !empty($_POST['search-name'])) {
			$name = trim ($_POST['search-name']);
			$query .= " AND name = :name";
			$params[':name'] = $name;
		} elseif ($filter === 'date' && !empty($_POST['search-date'])) {
			$date = $_POST['search-date'];
			$query .= " AND DATE(time) = :date";
			$params[':date'] = $date;
		}
	}

	$stmt = $db->prepare($query);
	$stmt->execute($params);

	echo "<table border='1'>";
	echo "<tr><th>Name</th><th>Time</th><th>Confidence</th><th>Action</th><th>Tardiness</th></tr>";

	while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
		echo "<tr>";
		echo "<td>" . htmlspecialchars($row["name"]) . "</td>";
		echo "<td>" . htmlspecialchars($row["time"]) . "</td>";
		echo "<td>" . htmlspecialchars($row["confidence"]) . "</td>";
		echo "<td>" . htmlspecialchars($row["action"]) . "</td>";
		echo "<td>" . htmlspecialchars($row["tardiness"]) . "</td>";
		echo "</tr>";
	}

	echo "</table>";
	} catch (PDOException $e) {
		print "Error!: " . $e->getMessage() . "</br>";
		die();
	}
?>
