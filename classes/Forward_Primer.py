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
from classes.Nucleotide import Nucleotide
from classes.Primer import Primer


class Forward_Primer(Primer):
    """
    Class that is used to represent a Forward_Primer.
    """
    def __init__(self, seq):
        if type(seq) == type("str"):
            self.sequence = Sequence(seq).sequence
        elif type(seq) == type(Sequence("AAG")):
            self.sequence = seq.sequence
        else:
            raise Exception("Invalid sequence in Forward_Primer class init()")
    

    def binds_to(self, seq):
        """
        Determines if this instance of the Forward_Primer class can bind
        to the Sequence object 'seq'.

        :param self: An instance of the Primer class
        :param seq: The sequence to try to bind to as a Sequence object
        """
        for fp_nuc, seq_nuc in zip(self.sequence, seq.sequence):
            if not fp_nuc.binds_to(seq_nuc):
                return False
        return True
