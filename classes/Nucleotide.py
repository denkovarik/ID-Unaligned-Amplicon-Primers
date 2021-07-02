###############################################################################
# File: Nucleotide.py
# Author: Dennis Kovarik
# Purpose: Holds the Nucleotide class
#
# Description:
#   This class represents a nucleotide in a DNA or RNA sequence.
###############################################################################


class Nucleotide():
    """
    Class that is used to represent a Nucleotide. The nucleotide bases for this
    class are represented by their symbols 'A', 'G', 'C', 'T', and 'U'.
    """
    valid_bases = set(("A", "G", "C", "T", "U"))
    def __init__(self, base):
        """
        Initializes an instance of the Nucleotide class.

        :param self: An instance of the Nucleotide class
        :param base: The nucleotide base for the instance
        """
        base = base.upper()
        # Make sure base is a valid nucleotide base
        if not base in Nucleotide.valid_bases:
            raise exception(str(base) + " is not a valid base for a nucleotide")
        self.base = base


    def binds_to(self, nuc):
        """
        Determines if this instance of the Nucleotide class binds the instance
        of the Nucleotide class passed into the function 'nuc'.

        :param self: An instance of the Nucleotide class.
        :param nuc: A instance of the Nucleotide class to check if this 
                    instance of the class binds to it or not.
        """
        if self.base == "A" and (nuc.base == "T" or nuc.base == "U"):
            return True
        elif self.base == "U" and nuc.base == "A":
            return True
        elif self.base == "T" and nuc.base == "A":
            return True
        elif self.base == "C" and nuc.base == "G":
            return True
        elif self.base == "G" and nuc.base == "C":
            return True
        return False
