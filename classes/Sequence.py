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
        
