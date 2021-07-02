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
from classes.Sequence import Sequence
from classes.Nucleotide import Nucleotide
from classes.Primer import Primer


class Reverse_Primer(Primer):
    """
    Class that is used to represent a Reverse_Primer.
    """
    def __init__(self, seq):
        if type(seq) == type("str"):
            self.sequence = Sequence(seq).sequence
        elif type(seq) == type(Sequence("AAG")):
            self.sequence = seq.sequence
        else:
            raise Exception("Invalid sequence in Reverse_Primer class init()")
    

    def binds_to(self, seq):
        """
        Determines if this instance of the Forward_Primer class can bind
        to the Sequence object 'seq'.

        :param self: An instance of the Primer class
        :param seq: The sequence to try to bind to as a Sequence object
        """
        seq_start = len(seq.sequence) - len(self.sequence)
        for i in range(len(self.sequence)):
            seq_i = seq_start + i
            if not self.sequence[i].binds_to(seq.sequence[seq_i]):
                return False
        return True
