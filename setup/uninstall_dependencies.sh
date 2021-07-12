#!/bin/bash

# This script will uninstall the dependencies for the project.

# Uninstall pysam
pip uninstall pysam
# Uninstall xlrd
pip uninstall xlrd
# Uninstall pandas
pip uninstall pandas
# Uninstall progress bar
pip uninstall progress tqdm
# Uninstall xlwt
pip uninstall xlwt
# Uninstall openpyxl
pip uninstall openpyxl
# Uninstall NumPy
pip uninstall numpy
# Install Plotly
pip install plotly
