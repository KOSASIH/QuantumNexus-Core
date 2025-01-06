#!/bin/bash

# Backup script to create a backup of specified directories and files

# Set variables
SOURCE_DIR="$1"  # The source directory to back up
DEST_DIR="$2"    # The destination directory for the backup
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")  # Create a timestamp
BACKUP_DIR="${DEST_DIR}/backup_${TIMESTAMP}"  # Create a timestamped backup directory

# Function to display usage
usage() {
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    usage
fi

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Create the backup directory
mkdir -p "$BACKUP_DIR"

# Copy files from the source directory to the backup directory
cp -r "$SOURCE_DIR/"* "$BACKUP_DIR/"

# Check if the copy was successful
if [ $? -eq 0 ]; then
    echo "Backup of '$SOURCE_DIR' completed successfully to '$BACKUP_DIR'."
else
    echo "Error: Backup failed."
    exit 1
fi

# Optional: Log the backup process
echo "$(date): Backup of '$SOURCE_DIR' completed successfully to '$BACKUP_DIR'." >> "${DEST_DIR}/backup_log.txt"

exit 0
