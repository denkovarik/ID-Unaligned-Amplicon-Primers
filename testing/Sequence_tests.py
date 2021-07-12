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
from classes.Primer import Primer
from classes.Reverse_Primer import Reverse_Primer
from classes.Forward_Primer import Forward_Primer
from classes.Sequence import Sequence
from classes.Amplicon import Amplicon
import pandas as pd


class Sequence_Tests(unittest.TestCase):
    """
    Runs tests for the Sequence class.
    """
    def primer_binary_srch(self):
        """
        Tests the Sequence class 'fp_binary_srch()' on its ability to find a 
        forward primer that it binds to from a list of forward primers
        
        :param self: An instance of the Primer_Tests class
        """
        # Read in the forward primers
        seq = Sequence('GCAGCTTTTGGAGTGGTTTTCATGTAAGGTTGCTGCT')
        path = parentdir + "/primers.xlsx"
        self.assertTrue(os.path.isfile(path))
        df = pd.read_excel(path)
        primers = []
        for index, row in df.iterrows():
            primers += [Forward_Primer(row['fP'], index)]
        primers = Primer.sort(primers)
        # Find the matching fP
        fP = seq.primer_binary_srch(primers)
        self.assertTrue(fP.sequence == 'GCAGCTTTTGGAGTGGTTTTCATGT')
        # Read in the reverse primers
        seq = Sequence('AAAAGGGGGAAAAGGGGAAAGTGCAGAGTCTTTGGGAGAAATGGC')
        path = parentdir + "/primers.xlsx"
        self.assertTrue(os.path.isfile(path))
        df = pd.read_excel(path)
        primers = []
        for index, row in df.iterrows():
            primers += [Reverse_Primer(row['rP'], index)]
        primers.sort()
        # Find the matching rP
        rP = seq.primer_binary_srch(primers)
        self.assertTrue(rP.sequence == 'GCCATTTCTCCCAAAGACTCTGCA')


    def test_primer_srch(self):
        """
        Tests the Sequence class 'fp_search()' on its ability to find a forward 
        primer that it binds to.
        
        :param self: An instance of the Primer_Tests class
        """
        # Read in the forward primers
        seq = Sequence('GCAGCTTTTGGAGTGGTTTTCATGTAAGGTTGCTGCT')
        path = parentdir + "/given/input_given/primers.xlsx"
        self.assertTrue(os.path.isfile(path))
        df = pd.read_excel(path)
        primers = []
        for index, row in df.iterrows():
            primers += [Forward_Primer(row['fP'], index)]
        # Find the matching fP
        fP = seq.primer_srch(primers)
        self.assertTrue(fP.sequence == 'GCAGCTTTTGGAGTGGTTTTCATGT')
        # Read in the reverse primers
        seq = Sequence('AAAAGGGGGAAAAGGGGAAAGTGCAGAGTCTTTGGGAGAAATGGC')
        path = parentdir + "/given/input_given/primers.xlsx"
        self.assertTrue(os.path.isfile(path))
        df = pd.read_excel(path)
        primers = []
        for index, row in df.iterrows():
            primers += [Reverse_Primer(row['rP'], index)]
        primers.sort()
        # Find the matching rP
        rP = seq.primer_srch(primers)
        self.assertTrue(rP.sequence == 'GCCATTTCTCCCAAAGACTCTGCA')


    def test_num_h_bonds(self):
        """ 
        Tests the Sequence.Nucleotide class on its ability to determine the 
        number of hydrogen bonds between a given nucleotide and its 
        compliment nucleotide
        
        :param self: An instance of the Sequence_Tests class
        """
        self.assertTrue(Sequence.Nucleotide.h_bonds["A"] == 2)
        self.assertTrue(Sequence.Nucleotide.h_bonds["a"] == 2)
        self.assertTrue(Sequence.Nucleotide.h_bonds["T"] == 2)
        self.assertTrue(Sequence.Nucleotide.h_bonds["t"] == 2)
        self.assertTrue(Sequence.Nucleotide.h_bonds["U"] == 2)
        self.assertTrue(Sequence.Nucleotide.h_bonds["u"] == 2)
        self.assertTrue(Sequence.Nucleotide.h_bonds["G"] == 3)
        self.assertTrue(Sequence.Nucleotide.h_bonds["g"] == 3)
        self.assertTrue(Sequence.Nucleotide.h_bonds["C"] == 3)
        self.assertTrue(Sequence.Nucleotide.h_bonds["c"] == 3)


    def test_hash(self):
        """
        Tests the overloaded __hash__ function so that Sequence class can be
        used as key in a python dictionary.

        :param self: An instance of the Sequence_Tests class
        """
        sq1 = Sequence("AAG")
        sq2 = Sequence("TTG")
        sq3 = Sequence("GGT")
        seqs = {}
        seqs[sq1] = "Hi"        
        seqs[sq2] = "there"
        seqs[sq3] = "friend"
        self.assertTrue(seqs[sq1] == "Hi")
        self.assertTrue(seqs[sq2] == "there")
        self.assertTrue(seqs[sq3] == "friend")

        
    def test_sort(self):
        """
        Tests sorting a list of sequences

        :param self: An instance of the Sequence_Tests class
        """
        # Make the test
        test_seqs = ["TAT", "AAG", "TTA", "GCG", "AAC"]
        test = []
        for i in test_seqs:
            test += [Sequence(i)]
        # The expected answer
        answer = test_seqs
        answer.sort()
        # Run the test
        test.sort()
        for t, a in zip(test, answer):
            self.assertTrue(t == a)

        
    def test_lt(self):
        """
        Tests the overload less than operator.

        :param self: An instance of the Sequence_Tests class
        """
        seq1 = "AAAA"
        seq2 = "AAAC"
        # Control for test
        self.assertTrue(seq1 < seq2) 
        # The test
        self.assertTrue(Sequence(seq1) < Sequence(seq2))


    def test_eq(self):
        """
        Tests the overload equality operator for the class.

        :param self: An instance of the Sequence_Tests class
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
        self.assertTrue(seq[0] == "A")


    def test_init(self):
        """
        Tests the initialization of the Sequence class.
        
        :param self: An instance of the Sequence_Tests class
        """
        # The same sequence as a String
        the_sequence = "AGAGTCG"
        sq = Sequence(the_sequence)
        self.assertTrue(sq.sequence[0] == "A")
        self.assertTrue(sq.sequence[1] == "G")
        self.assertTrue(sq.sequence[2] == "A")
        self.assertTrue(sq.sequence[3] == "G")
        self.assertTrue(sq.sequence[4] == "T")
        self.assertTrue(sq.sequence[5] == "C")
        self.assertTrue(sq.sequence[6] == "G") 
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

    
    def test_class_var_usage(self):
        """
        Testing for expected usage for Sequence class variables.

        :param self: An instance of the Sequence_Tests class
        """
        # Testing for correct nucleotide base symbols case insensitive
        self.assertTrue("A" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("C" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("G" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("T" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("U" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("a" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("c" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("g" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("t" in Sequence.Nucleotide.valid_symbols)
        self.assertTrue("u" in Sequence.Nucleotide.valid_symbols)
        # Testing for identifying correct nucleotide compliments
        self.assertTrue("A" in Sequence.Nucleotide.compl["T"])
        self.assertTrue("a" in Sequence.Nucleotide.compl["T"])
        self.assertTrue("A" in Sequence.Nucleotide.compl["t"])
        self.assertTrue("a" in Sequence.Nucleotide.compl["t"])
        self.assertTrue("A" in Sequence.Nucleotide.compl["U"])
        self.assertTrue("a" in Sequence.Nucleotide.compl["U"])
        self.assertTrue("A" in Sequence.Nucleotide.compl["u"])
        self.assertTrue("a" in Sequence.Nucleotide.compl["u"])
        self.assertTrue("C" in Sequence.Nucleotide.compl["G"])
        self.assertTrue("c" in Sequence.Nucleotide.compl["G"])
        self.assertTrue("C" in Sequence.Nucleotide.compl["g"])
        self.assertTrue("c" in Sequence.Nucleotide.compl["g"])
        self.assertTrue("G" in Sequence.Nucleotide.compl["C"])
        self.assertTrue("g" in Sequence.Nucleotide.compl["C"])
        self.assertTrue("G" in Sequence.Nucleotide.compl["c"])
        self.assertTrue("g" in Sequence.Nucleotide.compl["c"])
        self.assertTrue("T" in Sequence.Nucleotide.compl["A"])
        self.assertTrue("t" in Sequence.Nucleotide.compl["A"])
        self.assertTrue("T" in Sequence.Nucleotide.compl["a"])
        self.assertTrue("t" in Sequence.Nucleotide.compl["a"])
        self.assertTrue("U" in Sequence.Nucleotide.compl["A"])
        self.assertTrue("u" in Sequence.Nucleotide.compl["A"])
        self.assertTrue("U" in Sequence.Nucleotide.compl["a"])
        self.assertTrue("u" in Sequence.Nucleotide.compl["a"])

        
    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Sequence_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
