#!/bin/bash

# Get the parent directory (src)
BASE_DIR=$(dirname "$(dirname "$(cd "$(dirname "$0")" && pwd)")")

# Set PYTHONPATH to point to src/Generator directory
export PYTHONPATH="$BASE_DIR/generator"

# Run all test files in the Tests folder
for test_file in "$BASE_DIR/tests"/*.py; do
    if [ -f "$test_file" ]; then
        # echo "Running tests in $test_file"
        pytest "$test_file"
        # echo "-------------------------------------------"
    fi
done
