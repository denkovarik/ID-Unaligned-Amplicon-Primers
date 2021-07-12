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
        # Set to indicated the valid nucleotide symbols
        valid_symbols = set(("A","C","G","T","U","a","c","g","t","u"))
        # Dictionary to identify nucleotide complements. Should be faster than
        # if statements
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
        # Dictionary used for constructing complimentary sequences
        get_compl =     {
                            "A" : "T",
                            "a" : "t",
                            "T" : "A",
                            "t" : "a",
                            "G" : "C",
                            "g" : "c",
                            "C" : "G",
                            "c" : "g",
                        }
        # Dictionary for identifying the number of hydrogen bonds between a 
        # given nucleotide and its compliment
        h_bonds =   {
                        "A" : 2,
                        "a" : 2,
                        "T" : 2,
                        "t" : 2,
                        "U" : 2,
                        "u" : 2,
                        "G" : 3,
                        "g" : 3,
                        "C" : 3,
                        "c" : 3,
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
            self.sequence = seq.upper()
        else:
            raise Exception("Invalid typesequence of nucleotides for Sequence class.")
    

    def __eq__(self, other):
        """
        Overloaded equality operator for the class

        :param self: An instance of the Nucleotide class.
        :param other: An other nucleotide being compared
        :return: Bool indicating if this seq is equal to other
        """
        return str(self) == str(other)


    def __getitem__(self, index):
        """
        Overloaded function for indexing the Sequence class.

        :param self: An instance of the Sequence class
        :param index: The index of the sequence to access
        :return: The corresponding base at 'index'
        """
        if index < 0 or index >= len(self.sequence):
            raise Exception("Index is out of bounds")
        return self.sequence[index]


    def __hash__(self):
        """
        Overloaded hash function for the Sequence class.

        :param self: An instance of the Sequence class
        :return: The has for the class instance
        """
        return hash(self.sequence)

    
    def __len__(self):
        """
        Overloaded function for the sequence length for the Sequence class.

        :param self: An instance of the Sequence class
        :return: The length of the sequence as an int
        """
        return len(self.sequence)


    def __lt__(self, other):
        """
        The overloaded less than operator.

        :param self: An instance of the Sequence class.
        :param other: Another instance of the Sequence class to compare to.
        :return: Boolean indicating whether this sequence is less than the 
                 other.
        """
        return self.sequence < other.sequence


    def primer_binary_srch(self, primers):
        """
        Searches a list of forward primers for one that binds to this instance 
        of the sequence class. The search is completed via binary search, and 
        a fP that binds to a search is one in which every base in the forward 
        primer matches the corresponding base in the sequence.

        :param self: An instance of the Sequence class
        :param primers: A list of primers to match to
        :return: The Forward_Primer that binds to the sequence
        """
        l = 0
        r = len(primers) - 1
        while l <= r:
            m = l + int((r - l) / 2) 
            if primers[m].binds_to(self):
                return primers[m]
            elif primers[m] < self:
                l = m + 1
            else:
                r = m - 1
        return None


    def primer_srch(self, primers):
        """
        Searches a list of forward primers for one that binds to this instance 
        of the sequence class. The search is completed by brute force, and a fP 
        that binds to a search is one in which every base in the forward primer 
        matches the corresponding base in the sequence.

        :param self: An instance of the Sequence class
        :param primers: A list of primers to match to
        :return: The Forward_Primer that binds to the sequence
        """
        for fP in primers:
            if fP.binds_to(self):
                return fP
        

    
    def __str__(self):
        """
        Overloaded function to convert the instance of the class to a string.

        :param self: An instance of the Sequence class
        :return: The string representation of the class.
        """
        return self.sequence
