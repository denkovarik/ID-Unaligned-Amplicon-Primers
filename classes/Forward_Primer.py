###############################################################################
# File: Forward_Primer.py
# Author: Dennis Kovarik
# Purpose: Holds the Forward_Primer class
#
# Description:
#   This class represents the Forward primer. This class extends the primer 
#   class.
###############################################################################
import os, sys, inspect
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Sequence import Sequence
from classes.Primer import Primer


class Forward_Primer(Primer):
    """
    Class that is used to represent a Forward_Primer.
    """
    def __init__(self, seq, index):
        if type(seq) == type("str"):
            self.sequence = Sequence(seq)
        elif type(seq) == type(Sequence("AAG")):
            self.sequence = seq
        else:
            raise Exception("Invalid sequence in Forward_Primer class init()")
        self.index = index

    
    def __eq__(self, other):
        """
        The overloaded equality operator for the class.

        :param self: An instance of the Forward_Primer class.
        :param other: Another instance of the Forward_Primer class to compare 
                      this instance to.
        """
        return str(self.sequence) == str(other)


    def __lt__(self, other):
        """
        The overloaded less than operator for the class.

        :param self: An instance of the Forward_Primer class.
        :param other: Another instance of the Forward_Primer class to compare.
        """
        return self.sequence < other.sequence


    def __getitem__(self, index):
        """
        Overloaded function for indexing the Sequence class.

        :param self: An instance of the Forward_Primer class
        :param index: The index of the sequence to access
        """
        if index < 0 or index >= len(self.sequence):
            raise Exception("Index is out of bounds")
        return self.sequence[index]

    
    def __len__(self):
        """
        Overloaded function for the sequence length for the Forward_Primer class.

        :param self: An instance of the Forward_Primer class
        """
        return len(self.sequence)


    @staticmethod
    def sort(fps):
        """
        Sorts a list of forward primers.

        :param self: An instance of the Forward_Primer class
        :param fps: A list of Forward_Primer objects
        """
        fps.sort()
        return fps


    def __str__(self):
        """
        The overloaded to string method for the class.

        :param self: An instance of the Forward_Primer class
        """
        return str(self.sequence)
    

    def binds_to(self, seq):
        """
        Determines if this instance of the Forward_Primer class can bind
        to the Sequence object 'seq'.

        :param self: An instance of the Primer class
        :param seq: The sequence to try to bind to as a Sequence object
        """
        for i in range(len(self.sequence)):
            if self.sequence[i] != seq[i]:
                return False
        return True
