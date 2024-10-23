<?php
$user = "******";		// * for privacy
$password = "********";		// * for privacy
$database = "milestones";
$table = "milestone_2";

try {
	//use PDO
	$db = new PDO("mysql:host=localhost;dbname=$database", $user, $password);
	$query = "SELECT DISTINCT name, time, confidence FROM $table";
	$params = [];

	// Check if the form has been submitted
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
	    $filter = $_POST['filter'];
	
	    if ($filter === 'name' && !empty($_POST['search-name'])) {
	    	$name = trim ($_POST['search-name']);
	        $query .= " WHERE name = :name";
	        $params[':name'] = $name;
	    } elseif ($filter === 'date' && !empty($_POST['search-date'])) {
	    	$date = $_POST['search-date'];
	        $query .= " WHERE DATE(time) = :date";
	        $params[':date'] = $date;
	    }
	}

	$stmt = $db->prepare($query);
	$stmt->execute($params);
	
	// Start the table
	 echo "<table border='1'>";
	 echo "<tr><th>Name</th><th>Time Stamp</th><th>Confidence %</th></tr>"; // Table headers
	
	 // Fetch data from the database
	    
	 // Loop through each row and create a table row
	while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
	     echo "<tr>";
	     echo "<td>" . htmlspecialchars($row["name"]) . "</td>";
	     echo "<td>" . htmlspecialchars($row["time"]) . "</td>";
	     echo "<td>" . htmlspecialchars($row["confidence"]) . "</td>";
	     echo "</tr>";
	}
	    
	 echo "</table>"; // End of the table
} catch (PDOException $e) {
	print "Error!: " . $e->getMessage() . "<br/>";
	die();
}
?>
