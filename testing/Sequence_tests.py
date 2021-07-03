###############################################################################
# File: Sequence_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Sequence class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Sequence import Sequence
from classes.Nucleotide import Nucleotide

class Sequence_Tests(unittest.TestCase):
    """
    Runs tests for the Sequence class.
    """
    def test_eq(self):
        """
        Tests the overload equality operator for the class.

        :param self: An instance of the Sequence class
        """
        seq1 = Sequence("AGT")
        seq2 = Sequence("AGT")
        seq3 = Sequence("TTT")

        self.assertTrue(seq1 == seq2)
        self.assertTrue("AGT" == seq2)
        self.assertTrue(seq1 == "AGT")
        self.assertTrue(seq1 != seq3)
        self.assertTrue("AGT" != seq3)
        self.assertTrue(seq1 != "TTT")
        
        self.assertFalse(seq1 != seq2)
        self.assertFalse("AGT" != seq2)
        self.assertFalse(seq1 != "AGT")
        self.assertFalse(seq1 == seq3)
        self.assertFalse("AGT" == seq3)
        self.assertFalse(seq1 == "TTT")


    def test_str(self):
        """
        Tests the functionality of the overloaded to string function for the
        Sequence class.

        :param self: An instance of the Sequence_Tests class
        """
        seq = Sequence("AAG")
        self.assertTrue(str(seq) == "AAG")


    def test_len(self):
        """
        Tests the functionality of the overloaded len() function for the 
        Sequence class.

        :param self: An instance of the Sequence_Tests class
        """
        seq = Sequence("AATTGGCC")
        self.assertTrue(len(seq) == len(seq.sequence))        

        
    def test_indexing(self):
        """
        Tests indexing the Sequence class.
        
        :param self: An instance of the Sequence_Tests class
        """
        seq = Sequence("AATTGGCC")
        self.assertTrue(seq[0].base == "A")


    def test_init(self):
        """
        Tests the initialization of the Sequence class.
        
        :param self: An instance of the Sequence_Tests class
        """
        # The sequence as a list of Nucleotides
        the_sequence = [Nucleotide("A"),Nucleotide("G"),Nucleotide("A"), \
                        Nucleotide("G"),Nucleotide("T"),Nucleotide("C"), \
                        Nucleotide("G")]
        sq = Sequence(the_sequence)
        self.assertTrue(sq.to_string() == "AGAGTCG")
        self.assertTrue(sq.sequence[0].base == "A")
        self.assertTrue(sq.sequence[1].base == "G")
        self.assertTrue(sq.sequence[2].base == "A")
        self.assertTrue(sq.sequence[3].base == "G")
        self.assertTrue(sq.sequence[4].base == "T")
        self.assertTrue(sq.sequence[5].base == "C")
        self.assertTrue(sq.sequence[6].base == "G")

        # The same sequence as a String
        the_sequence = "AGAGTCG"
        sq = Sequence(the_sequence)
        self.assertTrue(sq.sequence[0].base == "A")
        self.assertTrue(sq.sequence[1].base == "G")
        self.assertTrue(sq.sequence[2].base == "A")
        self.assertTrue(sq.sequence[3].base == "G")
        self.assertTrue(sq.sequence[4].base == "T")
        self.assertTrue(sq.sequence[5].base == "C")
        self.assertTrue(sq.sequence[6].base == "G") 

        # The same sequence as a list of Strings
        the_sequence = ["A","G","A","G","T","C","G"]
        error = False
        try:
            sq = Sequence(the_sequence)
            error = True
        except:
            self.assertTrue(True)
        finally:
            if error:
                self.assetTrue(False)
        #self.assertTrue(sq.sequence[0].base == "A")
        #self.assertTrue(sq.sequence[1].base == "G")
        #self.assertTrue(sq.sequence[2].base == "A")
        #self.assertTrue(sq.sequence[3].base == "G")
        #self.assertTrue(sq.sequence[4].base == "T")
        #self.assertTrue(sq.sequence[5].base == "C")
        #self.assertTrue(sq.sequence[6].base == "G") 

        
    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Sequence_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
