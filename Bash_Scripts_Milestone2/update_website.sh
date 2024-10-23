#!/bin/bash

CSV_PATH="/var/lib/mysql-files/data.csv"      # The CSV file to monitor changes on.
USER="******"                        # Database information, hiding with ** for security
PASSWORD="*******"
DATABASE="milestones"
TABLE="milestone_2"
LOGFILE="/var/lib/mysql-files/changes.log"    # Log file for tracking changes

# Function to update the database with CSV data
update_database() {
   	# Read the CSV file line by line
   	while IFS=, read -r name time confidence; do
        # Skip the header row by checking if the first field is "Name"
        if [ "$name" != "Name" ]; then

			# SQL query to insert data into the table (using ON DUPLICATE KEY to update if the name already exists)
			query="INSERT INTO $TABLE (name, time, confidence) VALUES ('$name',STR_TO_DATE('$time', '%Y-%m-%d %h:%i:%s %p'), '$confidence') 
                   ON DUPLICATE KEY UPDATE time='$time', confidence='$confidence';"


			# Execute the SQL query
			mysql -u "$USER" -p"$PASSWORD" -e "$query" "$DATABASE"

       		# Log the action
       		echo "$(date) - Updated database with: $name, $time, $confidence" >> "$LOGFILE"
        fi

    done < "$CSV_PATH"

}

# Call the function to update the database
update_database
