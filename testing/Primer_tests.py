###############################################################################
# File: Primer_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Primer class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Primer import Primer
from classes.Reverse_Primer import Reverse_Primer
from classes.Forward_Primer import Forward_Primer
from classes.Sequence import Sequence
from classes.Amplicon import Amplicon
import pandas as pd


class Primer_Tests(unittest.TestCase):
    """
    Runs tests for the Primer class.
    """


    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Primer_Tests class
        """
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
