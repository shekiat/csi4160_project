#!/bin/bash

sudo cp data.csv /var/lib/mysql-files

# Check if the move was successful
if [ $? -eq 0 ]; then
    echo "File moved successfully."
else
    echo "Error moving the file."
fi
