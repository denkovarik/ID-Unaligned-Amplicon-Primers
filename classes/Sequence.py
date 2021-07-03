###############################################################################
# File: Sequence.py
# Author: Dennis Kovarik
# Purpose: Holds the Sequence class
#
# Description:
#   This class represents a sequence of nucleotides.
###############################################################################
import os, sys, inspect
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Nucleotide import Nucleotide

class Sequence():
    """
    Class that is used to represent a Sequence.
    """
    def __init__(self, seq):
        """
        Initializes an instance of the Sequence class.

        :param self: An instance of the Sequence class.
        :param seq: A sequence of nucleotides as a list of Nucleotides.
        """
        if type(seq) == type("string"):
            self.sequence = []
            for c in seq:
                self.sequence.append(Nucleotide(c))
        # See if seq is a list
        elif type(seq) == type([]):
            ref = Nucleotide("A")
            for nuc in seq:
                if type(nuc) != type(ref):
                    raise Exception("Invalid sequence of nucleotides for Sequence class.")
            self.sequence = seq
        else:
            raise Exception("Invalid sequence of nucleotides for Sequence class.")
        # Change sequence from list to tuple so is unchangeable
        self.sequence = tuple(self.sequence)
        self.sequence_str = self.to_string()
    

    def __eq__(self, other):
        """
        Overloaded equality operator for the class

        :param self: An instance of the Nucleotide class.
        :param other: An other nucleotide being compared
        """
        return str(self) == str(other)


    def __getitem__(self, index):
        """
        Overloaded function for indexing the Sequence class.

        :param self: An instance of the Sequence class
        :param index: The index of the sequence to access
        """
        if index < 0 or index >= len(self.sequence):
            raise Exception("Index is out of bounds")
        return self.sequence[index]

    
    def __len__(self):
        """
        Overloaded function for the sequence length for the Sequence class.

        :param self: An instance of the Sequence class
        """
        return len(self.sequence)


    def __lt__(self, other):
        """
        The overloaded less than operator.

        :param self: An instance of the Sequence class.
        :param other: Another instance of the Sequence class to compare to.
        """
        return self.sequence_str < other.sequence_str

    
    def __str__(self):
        """
        Overloaded function to convert the instance of the class to a string..

        :param self: An instance of the Sequence class
        """
        return self.sequence_str

        
    def to_string(self):
        """
        Returns the sequence as a String.        

        :param self: An instance of the Sequence class.
        """
        seq = ""
        for c in self.sequence:
            seq += str(c)
        return seq
