#!/bin/bash

# Function to process each line
process_line() {
    local line=$1
    # Escape \ with \\
    line=${line//\\/\\\\}
    # Add \\ in front of $
    line=${line//\$/\\\\\$}
    # Escape " with \"
    line=${line//\"/\\\"}
    # Wrap line with double quotes and add a comma
    echo "\"$line\","
}

# Check if a file is provided
if [ $# -eq 1 ]; then
    # Read from file
    file=$1
    while IFS= read -r line; do
        process_line "$line"
    done < "$file"
else
    # Read from standard input
    echo "Enter text (Ctrl-D to finish):"
    while IFS= read -r line; do
        process_line "$line"
    done
fi
