#!/bin/bash

# This file runs all testing scripts for the project

# Create filepaths
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

# Run the tests for the Primer class
echo "Running Tests for Primer Class"
python $DIR"/Primer_tests.py"

# Run the tests for the Forward_Primer class
echo "Running Tests for Forward_Primer Class"
python $DIR"/Forward_Primer_tests.py"

# Run the tests for the Reverse_Primer class
echo "Running Tests for Reverse_Primer Class"
python $DIR"/Reverse_Primer_tests.py"

# Run the tests for the Sequence class
echo "Running Tests for Sequence Class"
python $DIR"/Sequence_tests.py"

# Run the tests for the Amplicon class
echo "Running Tests for Amplicon Class"
python $DIR"/Amplicon_tests.py"

# Run the tests for the Unaligned_Amplicons class
echo "Running Tests for Unaligned_Amplicons Class"
python $DIR"/Unaligned_Amplicons_tests.py"
