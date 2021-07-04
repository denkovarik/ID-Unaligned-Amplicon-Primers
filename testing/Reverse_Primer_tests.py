###############################################################################
# File: Reverse_Primer_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Reverse_Primer class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Reverse_Primer import Reverse_Primer
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Nucleotide import Nucleotide
from classes.Sequence import Sequence


class Reverse_Primer_Tests(unittest.TestCase):
    """
    Runs tests for the Reverse_Primer class.
    """
    def test_lt(self):
        """
        Tests the overloaded less than operator. 
        
        :param self: An instance of the Reverse_Primer_Tests class
        """
        pass
 

    def test_eq(self):
        """
        Tests the overloaded equality operator. 
        
        :param self: An instance of the Reverse_Primer_Tests class
        """
        seq1 = "AAT"
        seq2 = "GGG"
        rp1 = Reverse_Primer(seq1, 1)
        rp2 = Reverse_Primer(seq1, 2)
        rp3 = Reverse_Primer(seq2, 4)
        self.assertTrue(rp1.index == 1)
        self.assertTrue(rp1 == rp2)
        self.assertTrue(rp1 == seq1)
        self.assertTrue(seq1 == rp2)
        self.assertTrue(rp1 != rp3)
        self.assertFalse(rp1 != rp2)
        self.assertFalse(rp1 != seq1)
        self.assertFalse(seq1 != rp2)
        self.assertFalse(rp1 == rp3)


    def test_str(self):
        """
        Tests the overload to string method for the Forward_Primer class.

        :param self: An instance of the Forward_Primer class
        """
        rp = Reverse_Primer("AAA", 0)
        self.assertTrue(str(rp) == "AAA")


    def test_binds_to(self):
        """
        Tests the Reverse_Primer class member function 'binds_to()' on its 
        ability to determine if it can bind to a sequence..
        
        :param self: An instance of the Reverse_Primer_Tests class
        """
        # Test 1
        test_sequence1 = "GGAGAAGGGGGAGATGTTGAGCATGTTCAGCAGCGTGGCTTCGCTGGCTCCCACTTTGTCTCCAGTCTTGATCAGCTGCACATCACTCAGGATTTCAATGGTGCCCCTGGAGATTT"
        rp1 = Reverse_Primer("aaatctccaggggcaccattgaa", 56)
        self.assertTrue(rp1.binds_to(Sequence(test_sequence1)))
        # Test 2
        test_sequence2 = "CCCATGCCTGACAAGTACTCCTTAGCACCTGTTGCTGTTGAGCTCAAATCCTTGCTGGGCAAGGATGTTCTGTTCCTGAAGGACTGTGTAGGCGCAGAAGTGGAGAAAGCCTGTGCCA"
        rp2 = Reverse_Primer("tggcacaggctttctccacttc", 49)
        self.assertTrue(rp2.binds_to(Sequence(test_sequence2)))
        # Test 3
        test_sequence3 = "TCATCTGCCCAGCCCACTTCACAGTGCCCCGTGCTGCTCATGTGCCTCCTCCCCTTTCCTCTGCAAAGTTCCCAGCTGGGCTGCAAGTCTCGGGTACCTGCAGTGTTGACAGCGCAGAGCCCTCCCGTCACCTCCAGGCAGAGTGGCCATCGCT"
        rp3 = Reverse_Primer("agcgatggccactctgcc", 41)
        self.assertTrue(rp3.binds_to(Sequence(test_sequence3)))
        # Test 4
        self.assertFalse(rp1.binds_to(Sequence(test_sequence2)))
        self.assertFalse(rp2.binds_to(Sequence(test_sequence1)))
        self.assertFalse(rp3.binds_to(Sequence(test_sequence2)))

   
    def test_init(self):
        """
        Tests the initialization of an instance of the Reverse_Primer class.
        
        :param self: An instance of the Reverse_Primer_Tests class
        """
        test_seq = "AATCGGTA"
        ref_seq = Sequence(test_seq)
        # Testing init with String sequence
        rp = Reverse_Primer(test_seq, 13)
        self.assertTrue(type(rp.sequence) == type(ref_seq))
        # Testing init with Sequence object
        rp = Reverse_Primer(ref_seq, 15)
        self.assertTrue(type(rp.sequence) == type(ref_seq))
        # Testing init with invalid sequence
        error = False
        try:
            fp = Reverse_Primer([1,2,3])
            error = True
        except:
            self.assertTrue(True)
        finally:
            if error:
                self.assertTrue(False)


    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Reverse_Primer_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
