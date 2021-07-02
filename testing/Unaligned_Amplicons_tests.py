###############################################################################
# File: Unaligned_Amplicons_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Unaligned_Amplicons class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Unaligned_Amplicons import Unaligned_Amplicons


class Unaligned_Amplicons_Tests(unittest.TestCase):
    """
    Runs tests for the Unaligned_Amplicons class.
    """
    def testExecution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Unaligned_Amplicons_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
