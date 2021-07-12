###############################################################################
# File: Reverse_Primer.py
# Author: Dennis Kovarik
# Purpose: Holds the Reverse_Primer class
# Description:
#   This class represents the reverse primer. This class extends the primer 
#   class.
###############################################################################
import os, sys, inspect
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Sequence import *
from classes.Primer import Primer


class Reverse_Primer(Primer):
    """
    Class that is used to represent a Reverse_Primer.
    """
    def __init__(self, seq, index):
        if type(seq) == type("str"):
            self.sequence = Sequence(seq)
        elif type(seq) == type(Sequence("AAG")):
            self.sequence = seq
        else:
            raise Exception("Invalid sequence in Reverse_Primer class init()")
        self.index = index
        self.reverse_comp = ""
        self.make_reverse_comp()    


    def binds_to(self, seq):
        """
        Determines if this instance of the Forward_Primer class can bind
        to the Sequence object 'seq'.

        :param self: An instance of the Primer class
        :param seq: The sequence to try to bind to as a Sequence object
        """
        for i in range(len(self.sequence)):
            if not seq[len(seq)-i-1] in Sequence.Nucleotide.compl[self[i]]:
                return False
        return True

    
    def __eq__(self, other):
        """
        The overloaded equality operator for the class.

        :param self: An instance of the Reverse_Primer class.
        :param other: Another instance of the Reverse_Primer class to compare 
                      this instance to.
        """
        return str(self.sequence) == str(other)


    def __getitem__(self, index):
        """
        Overloaded function for indexing the Sequence class.

        :param self: An instance of the Reverse_Primer class
        :param index: The index of the sequence to access
        """
        if index < 0 or index >= len(self.sequence):
            raise Exception("Index is out of bounds")
        return self.sequence[index]

    
    def __len__(self):
        """
        Overloaded function for the sequence length for the Reverse_Primer class.

        :param self: An instance of the Reverse_Primer class
        """
        return len(self.sequence)


    def __gt__(self, other):
        """
        The overloaded greater than operator for the class.

        :param self: An instance of the Reverse_Primer class.
        :param other: Another instance of the Reverse_Primer class to compare.
        """
        if type(other.sequence) == type(""):
            l = min(len(self.reverse_comp), len(other.sequence))
            for i in range(l):
                self_nuc = self.reverse_comp[len(self.reverse_comp)-i-1]
                other_nuc = other.sequence[len(other.sequence)-i-1]
                if self_nuc != other_nuc:
                    return self_nuc > other_nuc
        l = min(len(self.reverse_comp), len(other.reverse_comp))
        for i in range(l):
            self_nuc = self.reverse_comp[len(self.reverse_comp)-i-1]
            other_nuc = other.reverse_comp[len(other.reverse_comp)-i-1]
            if self_nuc != other_nuc:
                return self_nuc > other_nuc


    def __lt__(self, other):
        """
        The overloaded less than operator for the class.

        :param self: An instance of the Reverse_Primer class.
        :param other: Another instance of the Reverse_Primer class to compare.
        """
        if type(other.sequence) == type(""):
            l = min(len(self.reverse_comp), len(other.sequence))
            for i in range(l):
                self_nuc = self.reverse_comp[len(self.reverse_comp)-i-1]
                other_nuc = other.sequence[len(other.sequence)-i-1]
                if self_nuc != other_nuc:
                    return self_nuc < other_nuc
        l = min(len(self.reverse_comp), len(other.reverse_comp))
        for i in range(l):
            self_nuc = self.reverse_comp[len(self.reverse_comp)-i-1]
            other_nuc = other.reverse_comp[len(other.reverse_comp)-i-1]
            if self_nuc != other_nuc:
                return self_nuc < other_nuc

    def make_reverse_comp(self):
        """
        Constructs the reverse compliment of the sequence for the Reverse 
        Primer.

        :param self: An instance of the Reverse_Primer class
        """
        self.reverse_comp = ""
        seq_len = len(self.sequence)
        for i in range(seq_len):
            index = seq_len - i - 1
            self.reverse_comp += Sequence.Nucleotide.get_compl[self.sequence[index]]


    def __str__(self):
        """
        The overloaded to string method for the class.

        :param self: An instance of the Reverse_Primer class
        """
        return str(self.sequence)
