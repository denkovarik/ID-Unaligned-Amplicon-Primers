###############################################################################
# File: Primer_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Primer class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Primer import Primer
from classes.Reverse_Primer import Reverse_Primer
from classes.Forward_Primer import Forward_Primer
from classes.Sequence import Sequence
import pandas as pd


class Primer_Tests(unittest.TestCase):
    """
    Runs tests for the Primer class.
    """
    def test_given_sequences_and_primers(self):
        """
        This tests ensures that this software can recreate the primer pairs
        from the given example excel files.
        
        :param self: An instance of the Primer_Tests class
        """
        # Filepaths
        output_NS_list_path = currentdir + "/testing_files/output_given/output_NS_list.xlsx"
        primers_path = currentdir + "/testing_files/primers.xlsx"
        # Ensure that files exist
        self.assertTrue(os.path.isfile(output_NS_list_path))
        self.assertTrue(os.path.isfile(primers_path))
        # Read excel files
        output_NS_list = pd.read_excel(output_NS_list_path)
        primers_df = pd.read_excel(primers_path)
        # Dictionary to contain primers
        primers = {}
        # Read in the NS_list
        test_seqs = {}
        for ind in output_NS_list.index:
            seq = output_NS_list['seq'][ind]
            count = int(output_NS_list['count'][ind])
            fP = output_NS_list['fP'][ind]
            if fP != fP:
                fP = None
            else:
                fP = int(fP)
            rP = output_NS_list['rP'][ind]
            if rP != rP:
                rP = None
            else:
                fP = int(fP)
            if not seq in test_seqs:
                test_seqs[seq] =    {
                                        "count" :   count, 
                                        "ratio" :   output_NS_list['ratio'][ind],
                                        "fP"    :   fP,
                                        "rP"    :   fP,
                                    }
            else:
                print("Duplicate sequence")
        for s in test_seqs.keys():
            print(test_seqs[s]["fP"])
        # Read in the Primers
        for ind in primers_df.index:
            index = int(primers_df['index'][ind])
            primers[index] =    {
                                    "fP" : Forward_Primer(primers_df['fP'][ind], index),
                                    "rP" : Reverse_Primer(primers_df['rP'][ind], index)
                                }



    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Primer_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
