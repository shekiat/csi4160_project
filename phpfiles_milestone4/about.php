<?php include("includes/a_config.php");?>
<!DOCTYPE html>
<html>
<head>
	<?php include("includes/head-tag-contents.php");?>
	<style>
		 table {
		 	 width: 60%;
	         border-collapse: collapse;
	         margin: 20px 0;
	     }
	     th, td {
	         border: 1px solid black;
	         padding: 8px;
	         text-align: left;
	     }
	     th {
	         background-color: #f2f2f2;
	     }
	</style>
</head>
<body>

<?php include("includes/design-top.php");?>
<?php include("includes/navigation.php");?>

<div class="container" id="main-content">
	<h2>Shift Schedule</h2>
	<p>Shift Schedule for 10/21/2024 - 10/28/2024</p>
	<table>
		 <tr>
		 	 <th>Employee Name</th>
	         <th>Shift Date</th>
	         <th>Shift Time</th>
	     </tr>
	     <?php
	     // Sample data for the shift schedule
	     $shifts = [
	         ['name' => 'Peyton', 'date' => '2024-12-10', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Danny', 'date' => '2024-12-10', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Ryan', 'date' => '2024-12-11', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Sam', 'date' => '2024-12-11', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Peyton', 'date' => '2024-12-11', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Keanu', 'date' => '2024-12-11', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Ryan', 'date' => '2024-12-12', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Danny', 'date' => '2024-12-12', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Peyton', 'date' => '2024-12-13', 'time' => '8:00 AM - 5:00 PM'],
	         ['name' => 'Sam', 'date' => '2024-12-13', 'time' => '8:00 AM - 5:00 PM']
	     ];
	
	     // Loop through the shift data and create table rows
	     foreach ($shifts as $shift) {
	         echo "<tr>";
	         echo "<td>{$shift['name']}</td>";
	         echo "<td>{$shift['date']}</td>";
	         echo "<td>{$shift['time']}</td>";
	         echo "</tr>";
	     }
	     ?>
	</table>
</div>

<?php include("includes/footer.php");?>

</body>
</html>
