###############################################################################
# File: Amplicon.py
# Author: Dennis Kovarik
# Purpose: Holds the Amplicon class
#
# Description:
#   This class represents an Amplicon, which is a sequence that has been 
#   amplified by artifical means such as PCR amplication.
###############################################################################
import os, sys, inspect
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Sequence import Sequence
from classes.Forward_Primer import Forward_Primer
from classes.Reverse_Primer import Reverse_Primer


class Amplicon():
    """
    Class that is used to represent an Amplicon.
    """
    def __init__(self, seq, fP=None, rP=None):
        """
        Initializes an instance of the Amplicon class.

        :param self: An instance of the Amplicon class.
        :param seq: The nucleotide sequence for the amplicon
        :param fP: The forward primer for the amplicon
        :param rP: The reverse primer for the amplicon
        """
        # Set the sequence for the amplicon
        if type(seq) == type("str"):
            self.sequence = Sequence(seq)
        elif type(seq) == type(Sequence("AAT")):
            self.sequence = seq
        else:
            raise Exception("Invalid sequence for Amplicon class")
        # Set the forward primer
        self.fP = None
        if fP is not None:
            if type(fP) != type(Forward_Primer("A", 1)):
                raise Exception("Invalid type for Forward Primer")
            self.fP = fP
        # Set the reverse primer
        self.rP = None
        if rP is not None:
            if type(rP) != type(Reverse_Primer("A", 2)):
                raise Exception("Invalid type for Reverse Primer")
            # Check that rP binds to sequence
            self.rP = rP
        self.count = 1

    def __eq__(self, other):
        """
        Overloaded equality operator.

        :param self: Instance of the Amplicon class.
        :param other: The other Amplicon to compare to.
        """
        if self.sequence != other.sequence:
            return False
        if self.fP != other.Fp:
            return False
        if self.rP != other.Rp:
            return False
        return True


    def __gt__(self, other):
        """
        The overloaded greater than operator.

        :param self: Instance of the Amplicon class.
        :param other: The other Amplicon to compare to.
        """
        return self.count > other.count


    def __lt__(self, other):
        """
        The overloaded less than operator.

        :param self: Instance of the Amplicon class.
        :param other: The other Amplicon to compare to.
        """
        return self.count < other.count
        


    def match_primers(self, fps, rps):
        """
        Determines which forward and reverse primers bind to this instance of
        the amplicon.

        :param self: This instance of the Amplicon class
        :param fps: A list of forward primers
        :param rps: A list of reverse primers
        """
        # Find the matching foward primer
        for f in fps:
            if f.binds_to(self.sequence):
                self.fP = f
        # Find the matching reverse primer
        for r in rps:
            if r.binds_to(self.sequence):
                self.rP = r


    def __str__(self):
        """
        Overloaded to string method for the class.
    
        :param self: An instance of the Amplicon class.
        """
        matches = ""
        # Indicated matching nucleotides between forward primer and sequence
        for i in range(len(self.fP)):
            if self.fP[i] == self.sequence[i]:
                matches += "|"
            else:
                matches += " "
        amp_str = str(self.fP) + "\n" + matches + "\n" + str(self.sequence.sequence[:len(self.fP)])
        return amp_str
