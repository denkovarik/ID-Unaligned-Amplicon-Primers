import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Reverse_Primer import Reverse_Primer


class Reverse_Primer_Tests(unittest.TestCase):
    """
    Runs tests for the Reverse_Primer class.
    """
    def testExecution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Reverse_Primer_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
