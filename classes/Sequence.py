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


class Sequence():
    """
    Class that is used to represent a Sequence.
    """
    class Nucleotide():
        """
        Inner class to provide useful functionality in regards to nucleotides. 
        This includes identifying which symbols are valid nucleotides whether
        to symbols for nucleotides are compliments of each other.
        """
        valid_symbols = set(("A","C","G","T","U","a","c","g","t","u"))
        compl = {
                    "A" : set(("t","T","u","U")),
                    "C" : set(("g","G")),
                    "G" : set(("c","C")),
                    "T" : set(("a","A")), 
                    "U" : set(("a","A")),
                    "a" : set(("t","T","u","U")),
                    "c" : set(("g","G")),
                    "g" : set(("c","C")),
                    "t" : set(("a","A")), 
                    "u" : set(("a","A")),
                }
        pass


    def __init__(self, seq):
        """
        Initializes an instance of the Sequence class.

        :param self: An instance of the Sequence class.
        :param seq: A sequence of nucleotides as a list of Nucleotides.
        """
        # Check the type of seq. Only strings are accepted
        if type(seq) == type("string"):
            # Make sure that valid sequence was passed in
            for nuc in seq:
                if not nuc in Sequence.Nucleotide.valid_symbols:
                    raise Exception("Invalid characters in sequence")
            self.sequence = seq.upper()
        else:
            raise Exception("Invalid typesequence of nucleotides for Sequence class.")
    

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
        return self.sequence < other.sequence

    
    def __str__(self):
        """
        Overloaded function to convert the instance of the class to a string..

        :param self: An instance of the Sequence class
        """
        return self.sequence
