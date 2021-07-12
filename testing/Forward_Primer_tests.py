###############################################################################
# File: Forward_Primer_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Forward_Primer class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Sequence import Sequence
from classes.Forward_Primer import Forward_Primer
import pandas as pd
from testing.sol import *


class Forward_Primer_Tests(unittest.TestCase):
    """
    Runs tests for the Forward_Primer class.
    """         
    def test_forward_primer_sort(self):
        """
        Tests the Forward_Primer class 'sort()' on its ability to sort forward 
        primers by sequence.
        
        :param self: An instance of the Primer_Tests class
        """
        # Read in the forward primers
        path = parentdir + "/given/input_given/primers.xlsx"
        self.assertTrue(os.path.isfile(path))
        df = pd.read_excel(path)
        primers = []
        for index, row in df.iterrows():
            primers += [Forward_Primer(row['fP'], index)]

        primers = Forward_Primer.sort(primers)
        self.assertTrue(primers == forward_primer_sort_exp)


    def test_gt_seq(self):
        """
        Tests the overload less than operator with a sequence.

        :param self: An instance of the Forward_Primer_Tests class
        """
        seq1 = "AAAA"
        seq2 = "AAACAATTGCT"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # Test case 1
        self.assertTrue(Forward_Primer(seq1, 0) < Sequence(seq2))
        # Test case 2
        self.assertTrue(Forward_Primer(seq1, 0) < Sequence(seq2.lower()))
        seq1 = "AATGGCATGGC"
        seq2 = "GGTACCTAAGC"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # The test
        self.assertTrue(Forward_Primer(seq1, 0) < Sequence(seq2.lower()))
    

    def test_lt_seq(self):
        """
        Tests the overload less than operator with a sequence.

        :param self: An instance of the Forward_Primer_Tests class
        """
        seq1 = "AAAA"
        seq2 = "AAACAATTGCT"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # Test case 1
        self.assertTrue(Forward_Primer(seq1, 0) < Sequence(seq2))
        # Test case 2
        self.assertTrue(Forward_Primer(seq1, 0) < Sequence(seq2.lower()))
        seq1 = "AATGGCATGGC"
        seq2 = "GGTACCTAAGC"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # The test
        self.assertTrue(Forward_Primer(seq1, 0) < Sequence(seq2.lower()))
        # Test case 3
        self.assertTrue(Forward_Primer(seq1, 0) < Sequence(seq2.lower()))
        seq1 = "ATGCTT"
        seq2 = "ATGCTTGGTTG"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # The test
        self.assertFalse(Forward_Primer(seq1, 0) < Sequence(seq2.lower()))


    def test_len(self):
        """
        Tests the __len__() overloaded function
        
        :param self: An instance of the Forward_Primer_Tests class
        """
        fp = Forward_Primer("AAGTCCG", 0)
        self.assertTrue(len(fp) == 7)


    def test_getitem(self):
        """
        Tests indexing for the Reverse_Primer class
        
        :param self: An instance of the Reverse_Primer_Tests class
        """
        fp = Forward_Primer("AAGTCCG", 0)
        self.assertTrue(fp[3] == "T")

        
    def test_gt(self):
        """
        Tests the overload greater than operator.

        :param self: An instance of the Forward_Primer_Tests class
        """
        seq1 = "AAAA"
        seq2 = "AAAC"
        # Control for test
        self.assertTrue(seq2 > seq1) 
        # Test case 1
        self.assertTrue(Forward_Primer(seq2, 0) > Forward_Primer(seq1, 21))
        # Test case 2
        self.assertTrue(Forward_Primer(seq1, 0) < Forward_Primer(seq2.lower(), 21))
        seq1 = "AATGGCATGGC"
        seq2 = "GGTACCTAAGC"
        # Control for test
        self.assertTrue(seq2 > seq1) 
        # The test
        self.assertTrue(Forward_Primer(seq2, 0) > Forward_Primer(seq1.lower(), 21))

        
    def test_lt(self):
        """
        Tests the overload less than operator.

        :param self: An instance of the Forward_Primer_Tests class
        """
        seq1 = "AAAA"
        seq2 = "AAAC"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # Test case 1
        self.assertTrue(Forward_Primer(seq1, 0) < Forward_Primer(seq2, 21))
        # Test case 2
        self.assertTrue(Forward_Primer(seq1, 0) < Forward_Primer(seq2.lower(), 21))
        seq1 = "AATGGCATGGC"
        seq2 = "GGTACCTAAGC"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # The test
        self.assertTrue(Forward_Primer(seq1, 0) < Forward_Primer(seq2.lower(), 21))


    def test_sort(self):
        """
        Tests the sort static function for the class. 
        
        :param self: An instance of the Forward_Primer_Tests class
        """
        # Make the test
        test_seqs = ["TAT", "AAG", "TTA", "GCG", "AAC"]
        test = []
        for i in range(len(test_seqs)):
            test += [Forward_Primer(test_seqs[i], i)]
        # The expected answer
        answer = test_seqs
        answer.sort()
        # Run the test
        test = Forward_Primer.sort(test)
        for t, a in zip(test, answer):
            self.assertTrue(t == a)



    def test_eq(self):
        """
        Tests the overloaded equality operator. 
        
        :param self: An instance of the Forward_Primer_Tests class
        """
        seq1 = "AAT"
        seq2 = "GGG"
        fp1 = Forward_Primer(seq1, 0)
        fp2 = Forward_Primer(seq1, 1)
        fp3 = Forward_Primer(seq2, 2)
        self.assertTrue(fp1.index == 0)
        self.assertTrue(fp1 == fp2)
        self.assertTrue(fp1 == seq1)
        self.assertTrue(seq1 == fp2)
        self.assertTrue(fp1 != fp3)
        self.assertFalse(fp1 != fp2)
        self.assertFalse(fp1 != seq1)
        self.assertFalse(seq1 != fp2)
        self.assertFalse(fp1 == fp3)


    def test_str(self):
        """
        Tests the overload to string method for the Forward_Primer class.

        :param self: An instance of the Forward_Primer class
        """
        fp = Forward_Primer("AAA", 0)
        self.assertTrue(str(fp) == "AAA")


    def test_binds_to(self):
        """
        Tests the Foward_Primer class member function 'binds_to()' on its 
        ability to determine if it can bind to a sequence..
        
        :param self: An instance of the Forward_Primer_Tests class
        """
        # Test 1
        test_sequence1     = "GGAGAAGGGGGAGATGTTGAGCATGTTCAGCAGCGTGGCTTCGCTGGCTCCCACTTTGTCTCCAGTCTTGATCAGCTGCACATCACTCAGGATTTCAATGGTGCCCCTGGAGATTT"
        fp1 = Forward_Primer("ggagaagggggagatgttgagca", 56)
        self.assertTrue(fp1.binds_to(Sequence(test_sequence1)))
        # Test 2
        test_sequence2     = "CCCATGCCTGACAAGTACTCCTTAGAGCCATTTGCTGTAGAATTCAAATCTCTGCTGGGCAAGGATGTTCTGTTCTTGAAAGACTGTGTAGGCCCAGAAGTGGAGAAAGCCTGTGCCA"
        fp2 = Forward_Primer("cccatgcctgacaagtactccttaga", 49)
        self.assertTrue(fp2.binds_to(Sequence(test_sequence2)))
        # Test 3
        test_sequence3     = "ACTGGCTCTGTTACTGGTGCTGTGCAAATGCCTAAGCAAATGCAGGTATAGGGCGTAGGGTCAAGTCTTGGTTGTTTGCATCTTGGAAGGAGGCAGAGTGGCCATCGCT"
        fp3 = Forward_Primer("actggctctgttactggtgctg", 23)
        self.assertTrue(fp3.binds_to(Sequence(test_sequence3)))

   
    def test_init(self):
        """
        Tests the initialization of an instance of the Forward_Primer class.
        
        :param self: An instance of the Forward_Primer_Tests class
        """
        test_seq = "AATCGGTA"
        ref_seq = Sequence(test_seq)
        # Testing init with String sequence
        fp = Forward_Primer(test_seq, 3)
        self.assertTrue(type(fp.sequence) == type(ref_seq))
        # Testing init with Sequence object
        fp = Forward_Primer(ref_seq, 5)
        self.assertTrue(type(fp.sequence) == type(ref_seq))
        # Testing init with invalid sequence
        error = False
        try:
            fp = Forward_Primer([1,2,3])
            error = True
        except:
            self.assertTrue(True)
        finally:
            if error:
                self.assertTrue(False)


    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Forward_Primer_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
