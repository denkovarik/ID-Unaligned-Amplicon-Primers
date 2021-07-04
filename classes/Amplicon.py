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
    def __init__(self, seq, fp=None, rp=None):
        """
        Initializes an instance of the Amplicon class.

        :param self: An instance of the Amplicon class.
        :param seq: The nucleotide sequence for the amplicon
        :param fp: The forward primer for the amplicon
        :param rp: The reverse primer for the amplicon
        """
        # Set the sequence for the amplicon
        if type(seq) == type("str"):
            self.sequence = Sequence(seq)
        elif type(seq) == type(Sequence("AAT")):
            self.sequence = seq
        else:
            raise Exception("Invalid sequence for Amplicon class")
        # Set the forward primer
        self.fp = None
        if fp is not None:
            if type(fp) != type(Forward_Primer("A", 1)):
                raise Exception("Invalid type for Forward Primer")
            # Check that fp binds to sequence
            if fp.binds_to(self.sequence):    
                self.fp = fp
            else:
                print("WARNING: Forward primger " + str(fp) \
                      + " doesn't bind to sequence " + str(self.sequence) \
                      + ". Forward primer will not be set")
        # Set the reverse primer
        self.rp = None
        if rp is not None:
            if type(rp) != type(Reverse_Primer("A", 2)):
                raise Exception("Invalid type for Reverse Primer")
            # Check that rp binds to sequence
            if rp.binds_to(self.sequence):    
                self.rp = rp
            else:
                print("WARNING: Reverse primger " + str(rp) \
                      + " doesn't bind to sequence " + str(self.sequence) \
                      + ". Reverse primer will not be set")


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
                self.fp = f
        # Find the matching reverse primer
        for r in rps:
            if r.binds_to(self.sequence):
                self.rp = r
