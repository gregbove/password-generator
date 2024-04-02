#!/bin/bash

# Get the parent directory (src)
TESTS_DIR=$(dirname "$(cd "$(dirname "$0")" && pwd)")
echo $TESTS_DIR

# Run all test files in the tests folder
pytest $TESTS_DIR
