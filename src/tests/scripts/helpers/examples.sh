#!/bin/bash

# Get the directory you are currently in
THIS_DIR="$(cd "$(dirname "$0")" && pwd)"

# Get the next directory up
NEXT_DIR_UP=$(dirname "$(dirname "$THIS_DIR")")

# --- Explicit test running ---
# Iterate through every (python) file in a directory
for test_file in "$TESTS_DIR/some-folder/"/*.py; do
    # Make sure file exists
    if [ ! -f "$test_file" ]; then
        continue
    fi

    # Check name of file against certain values
    if [ "$(basename "$test_file")" = "__init__.py" ]; then
        continue
    fi

    # Test the file!
    echo "===== Running tests in $test_file ====="
    pytest "$test_file"
done
