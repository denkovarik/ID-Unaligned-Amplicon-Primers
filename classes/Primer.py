###############################################################################
# File: Primer.py
# Author: Dennis Kovarik
# Purpose: Holds the Primer class
#
# Description:
#   This class represents a primer. The primer class is extended by the
#   Forward_Primer and Reverse_Primer classes.
###############################################################################

from abc import ABC, abstractmethod


class Primer(ABC):
    """
    Class that is used to represent a Primer.
    """
    @ abstractmethod
    def binds_to(self, seq):
        """
        Abstract method that determines if this instance of the Primer can bind
        to the Sequence object 'seq'.

        :param self: An instance of the Primer class
        :param seq: The sequence to try to bind to as a Sequence object
        """
        pass
