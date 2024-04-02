#!/bin/bash

# Get the parent directory (src)
TESTS_DIR=$(dirname "$(cd "$(dirname "$0")" && pwd)")

# Run all test files in the unit-tests folder
for test_file in "$TESTS_DIR/unit-tests"/*.py; do
    if [ -f "$test_file" ]; then
        # echo "Running tests in $test_file"
        pytest "$test_file"
        # echo "-------------------------------------------"
    fi
done
