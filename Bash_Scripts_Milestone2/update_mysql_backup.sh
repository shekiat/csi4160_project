#!/bin/bash

# Location of source directory and backup archive file
SOURCE_DIR="/var/lib/mysql-files"
BACKUP_FILE="/usr/local/backup-mysql-files.tar.gz"

# Create a new tar.gz file, and overwrite the previous one
tar -czf $BACKUP_FILE $SOURCE_DIR

# Check if the tar command was successful
if [ $? -eq 0 ]; then
    echo "Backup successful: $(date)"
    echo "Backup successful: $(date)" >> /usr/local/backup_timestamp.log
else
    echo "Backup failed: $(date)" 
    echo "Backup failed: $(date)" >> /usr/local/backup_timestamp.log
fi
