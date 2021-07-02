#!/bin/bash

# This file runs all testing scripts for the project

# Run the tests for the Nucleotide class
echo "Running Tests for Nucleotide Class"
python Nucleotide_tests.py

# Run the tests for the Primer class
echo "Running Tests for Primer Class"
python Primer_tests.py

# Run the tests for the Forward_Primer class
echo "Running Tests for Forward_Primer Class"
python Forward_Primer_tests.py

# Run the tests for the Reverse_Primer class
echo "Running Tests for Reverse_Primer Class"
python Reverse_Primer_tests.py

# Run the tests for the Sequence class
echo "Running Tests for Sequence Class"
python Sequence_tests.py

# Run the tests for the Amplicon class
echo "Running Tests for Amplicon Class"
python Amplicon_tests.py

# Run the tests for the Unaligned_Amplicons class
echo "Running Tests for Unaligned_Amplicons Class"
python Unaligned_Amplicons_tests.py
