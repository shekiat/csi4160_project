# This file contains the Google Cloud Function called data_transfer that we implemented to insert new data from the bucket into our SQL Cloud database
import functions_framework
import os
import csv
from google.cloud import storage
import mysql.connector
from datetime import datetime

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def data_transfer(cloud_event):
    data = cloud_event.data

    # Extract event details
    event_id = cloud_event["id"]
    event_type = cloud_event["type"]
    bucket_name = data["bucket"]
    file_name = data["name"]

    # Log the event details
    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket_name}")
    print(f"File: {file_name}")

    # Only process the file if it's the 'data.csv'
    if file_name != 'data.csv':
        print(f"Not the target file ({file_name}), exiting.")
        return

    # Initialize Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Download the CSV file content as text
    csv_data = blob.download_as_text()

    # Connect to Cloud SQL
    try:
        print(f"Connecting to database...")
        connection = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME')
        )
        cursor = connection.cursor()
        print(f"Connection Successful!")

         # Check CSV data
        print(f"CSV data loaded with {len(csv_data.splitlines())} lines.")  # Debugging: check the number of lines in the CSV
        if not csv_data.strip():
            print("CSV data is empty or not read correctly.")

        # Process the CSV data and update the SQL database
        csv_reader = csv.reader(csv_data.splitlines())
        for i, row in enumerate(csv_reader):
            print(f"Row {i}: {row}")
            print(f"Processing row: {row}")
            if row[0] == "Name" and row[1] == "Time":
                print(f"Skipping header row.")
                continue
                
            try:
                time_value = datetime.strptime(row[1], '%Y-%m-%d %I:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S')
                print(f"Converted Time")
                if row[0] != "Name":
                    cursor.execute("SELECT COUNT(*) FROM timesheet WHERE name = %s AND time = %s", (row[0], time_value))
                    count = cursor.fetchone()[0]
                    if count == 0:  # No rows found, so insert the new row
                        print(f"Inserting row into database: {row[0]}, {time_value}, {row[2]}, {row[3]}, {row[4]}")
                        cursor.execute("INSERT INTO timesheet (name, time, confidence, action, tardiness) VALUES (%s, %s, %s, %s, %s)", 
                                       (row[0], time_value, row[2], row[3], row[4]))
                else:
                    print(f"skipping for now")
            except ValueError:
                print(f"Invalid time format for row: {row}")
                
        # Commit the changes
        connection.commit()
        print(f"Successfully updated database with data from {file_name}.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")
