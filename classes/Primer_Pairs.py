###############################################################################
# File: Primer_Pairs.py
# Author: Dennis Kovarik
# Purpose: Holds the Primer_Pairs class
#
# Description:
#   This class represents a primer pair. This class extends the primer 
#   class.
###############################################################################
import os, sys, inspect
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Sequence import Sequence
from classes.Primer import Primer


class Primer_Pair():
    """
    Class to represent a primer pair.
    """
    def __init__(self, fP, rP, count):
        """
        Inits an instance of the Primer_Pair class.

        :param self: An instance of the Primer_Pair class.
        :param fP: The forward primer in the pair
        :param rP: The reverse primer in the class
        """
        self.fP = fP
        self.rP = rP
        self.count = count
        ratio = 0

    def __eq__(self, other):
        """
        The overloaded equality operator.
    
        :param self: An instance of the class
        :param other: The other instance to compare to.
        """
        return self.fP == other.fP and self.rP == other.rP

    
    def __gt__(self, other):
        """
        The overloaded greater than operator for the class.
            
        :param self: An instance of the Primer_Pair class.
        :param other: The other primer pair to compare to.
        :return: True if self.count > other.count
        :return: False otherwise
        """
        return self.count > other.count


    def __hash__(self):
        """
        Overloaded hash function for the Primer_Pair class.

        :param self: An instance of the Primer_Pair class
        :return: The hash for the class instance
        """
        h = str(self.fP).strip() + " " + str(self.rP).strip()
        return hash(h)

    
    def __lt__(self, other):
        """
        The overloaded less than operator for the class.
            
        :param self: An instance of the Primer_Pair class.
        :param other: The other primer pair to compare to.
        :return: True if self.count < other.count
        :return: False otherwise
        """
        return self.count < other.count


    def __str__(self):
        """
        The overloaded to string function for the class.
            
        :param self: An instance of the Primer_Pair class.
        :return: The string representation of the instance
        """
        return str(self.fP) + " " + str(self.rP)
