###############################################################################
# File: Amplicon_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Amplicon class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Amplicon import Amplicon


class Amplicon_Tests(unittest.TestCase):
    """
    Runs tests for the Amplicon class.
    """
    def testExecution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Amplicon_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
