<?php include("includes/a_config.php");?>

<!DOCTYPE html>
<html>
<head>
	<?php include("includes/head-tag-contents.php");?>
	<style>
		table {
			 width: 50%;
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

	    #filter-selections {
	    	display:flex;
	    	gap: 1em;
	    }

	    #search-name {
	    	
	    }
	    .filter {
	         margin-bottom: 20px;
	    }
	    .hidden {
	      	 display: none;
	    }
	 </style>
</head>
<body>

<?php include("includes/design-top.php");?>
<?php include("includes/navigation.php");?>

<div class="container" id="main-content">
	<h2>Clock In/Clock Out Data</h2>
	<p>This page is used to display the name, timestamp, and confidence level for each face detected</p>
	<form method="POST" class="filter" id="filter-selections">
		<label>
			<input type="radio" name="filter" value="all" <?php if (isset($_POST['filter']) && $_POST['filter'] === 'all') echo 'checked'; ?>> Show All
		</label><br>
		<label>
		    <input type="radio" name="filter" value="name" <?php if (isset($_POST['filter']) && $_POST['filter'] === 'name') echo 'checked'; ?>> Filter by Name
		</label>
		<input type="text" name="search-name" id="search-name" class="<?php if (isset($_POST['filter']) && $_POST['filter'] === 'name') echo ''; else echo 'hidden'; ?>" placeholder="Enter name" value="<?php if (isset($_POST['search-name'])) echo htmlspecialchars($_POST['search-name']); ?>"><br>
		    
		<label>
		    <input type="radio" name="filter" value="date" <?php if (isset($_POST['filter']) && $_POST['filter'] === 'date') echo 'checked'; ?>> Filter by Date
		</label>
		<input type="date" name="search-date" id="search-date" class="<?php if (isset($_POST['filter']) && $_POST['filter'] === 'date') echo ''; else echo 'hidden'; ?>" value="<?php if (isset($_POST['search-date'])) echo htmlspecialchars($_POST['search-date']); ?>"><br>
		    
		<input type="submit" value="Filter">
	</form>
	<?php include("timesheet.php");?>

	<script>
	    // Show/hide input fields based on selected filter type
	    const filters = document.querySelectorAll('input[name="filter"]');
	    const nameInput = document.getElementById('search-name');
	    const dateInput = document.getElementById('search-date');
	
	    filters.forEach(filter => {
	        filter.addEventListener('change', () => {
	            nameInput.classList.add('hidden');
	            dateInput.classList.add('hidden');
	            if (filter.value === 'name') {
	                nameInput.classList.remove('hidden');
	            } else if (filter.value === 'date') {
	                dateInput.classList.remove('hidden');
	            }
	        });
	    });
	</script>
</div>

<?php include("includes/footer.php");?>

</body>
</html>
