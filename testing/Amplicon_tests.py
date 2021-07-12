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
from classes.Sequence import Sequence
from classes.Forward_Primer import Forward_Primer
from classes.Reverse_Primer import Reverse_Primer


class Amplicon_Tests(unittest.TestCase):
    """
    Runs tests for the Amplicon class.
    """
    def test_match_primers(self):
        """
        Tests the Amplicon class member function 'match_primers()'
        
        :param self: An instance of the Amplicon_Tests class
        """
        # The amplicon to match the primer to
        amp = Amplicon("AAAGCGGTTTGT")
        # The Forward Primers
        fps =   [
                    Forward_Primer("TTT", 0),
                    Forward_Primer("GCC", 1),
                    Forward_Primer("GGG", 2),
                    Forward_Primer("AAA", 3),
                    Forward_Primer("ATA", 4),
                ]
        # The Reverse Primers
        rps =   [
                    Reverse_Primer("GGG", 0),
                    Reverse_Primer("ACC", 1),
                    Reverse_Primer("CCC", 2),
                    Reverse_Primer("ACA", 3),
                    Reverse_Primer("GGG", 4),
                ]
        # Run the Test for the forward primers
        amp.match_primers(fps, rps)
        self.assertTrue(amp.fP == fps[3])
        self.assertFalse(amp.fP == fps[1])
        self.assertFalse(amp.fP == fps[2])
        self.assertFalse(amp.fP == fps[0])
        self.assertFalse(amp.fP == fps[4])
        # Run the test for the reverse primers
        self.assertTrue(amp.rP == rps[3])
        self.assertFalse(amp.rP == rps[0])
        self.assertFalse(amp.rP == rps[1])
        self.assertFalse(amp.rP == rps[2])
        self.assertFalse(amp.rP == rps[4])
        

    def test_init(self):
        """
        Tests the initialization of an instance of the Amplicon class.
        
        :param self: An instance of the Amplicon_Tests class
        """
        test_seq = 'AAGCTTGAGGTCCAA'
        # Testing init with String sequence
        amp = Amplicon(test_seq)
        self.assertTrue(str(amp.sequence) == test_seq)
        self.assertTrue(amp.fP == None)
        self.assertTrue(amp.rP == None) 
        # Testing init with Sequence object sequence
        amp = Amplicon(Sequence(test_seq)) 
        self.assertTrue(str(amp.sequence) == test_seq)
        self.assertTrue(amp.fP == None)
        self.assertTrue(amp.rP == None) 
        # Testing with forward primer
        amp = Amplicon(Sequence(test_seq), Forward_Primer("AAG", 0))
        self.assertTrue(amp.fP == Forward_Primer("AAG", 0))
        # Testing with reverse primer
        amp = Amplicon(Sequence(test_seq), fP=None, rP=Reverse_Primer("TTG", 1))
        self.assertTrue(amp.fP == None)
        self.assertTrue(amp.rP == Reverse_Primer("TTG", 5))


    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Amplicon_Tests class
        """
        self.assertTrue(True)          


if __name__ == '__main__':
    unittest.main()
