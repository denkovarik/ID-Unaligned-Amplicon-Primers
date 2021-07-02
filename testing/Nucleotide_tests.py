###############################################################################
# File: Nucleotide_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Nucleotide class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Nucleotide import Nucleotide


class Nucleotide_Tests(unittest.TestCase):
    """
    Runs tests for the Nucleotide class.
    """
    def test_init(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Nucleotide_Tests class
        """
        self.assertTrue(True)


    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Nucleotide_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
