###############################################################################
# File: Nucleotide_tests.py
# Author: Dennis Kovarik
# Purpose: Testing file for the Nucleotide class
###############################################################################

import io
import os, sys, inspect
import unittest
# Get the current and parent folder that files are located in
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from classes.Nucleotide import Nucleotide


class Nucleotide_Tests(unittest.TestCase):
    """
    Runs tests for the Nucleotide class.
    """
    def test_binds_to(self):
        """
        Tests the Nucleotide class member function 'binds_to()' on its ability
        to determine if another instance of the nucleotide class binds to it 
        or not.
        
        :param self: An instance of the Nucleotide_Tests class
        """
        # The bases
        a = Nucleotide("A")
        g = Nucleotide("G")
        c = Nucleotide("C")
        t = Nucleotide("T")
        u = Nucleotide("U")
        
        # Testing Adenine binding rules
        self.assertTrue(a.binds_to(t))
        self.assertFalse(a.binds_to(a))
        self.assertFalse(a.binds_to(g))
        self.assertFalse(a.binds_to(c))
        self.assertTrue(a.binds_to(u))
        
        # Testing Uracil binding rules
        self.assertTrue(u.binds_to(a))
        self.assertFalse(u.binds_to(t))
        self.assertFalse(u.binds_to(g))
        self.assertFalse(u.binds_to(c))
        self.assertFalse(u.binds_to(u))
        
        # Testing Thymine binding rules
        self.assertTrue(t.binds_to(a))
        self.assertFalse(t.binds_to(t))
        self.assertFalse(t.binds_to(g))
        self.assertFalse(t.binds_to(c))
        self.assertFalse(t.binds_to(u))

        # Testing guanine binding rules
        self.assertTrue(g.binds_to(c))
        self.assertFalse(g.binds_to(a))
        self.assertFalse(g.binds_to(g))
        self.assertFalse(g.binds_to(t))
        self.assertFalse(g.binds_to(u))

        # Testing cytosine binding rules
        self.assertTrue(c.binds_to(g))
        self.assertFalse(c.binds_to(a))
        self.assertFalse(c.binds_to(c))
        self.assertFalse(c.binds_to(t))
        self.assertFalse(c.binds_to(u))        
        

    def test_init(self):
        """
        Tests the initialization of an instance of the Nucleotide class.
        
        :param self: An instance of the Nucleotide_Tests class
        """
        # Testing correct init with adenine
        try:
            nc = Nucleotide("A")
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        try:
            nc = Nucleotide("a")
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        # Testing correct init with guanine
        try:
            nc = Nucleotide("G")
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        # Testing correct init with cytosine
        try:
            nc = Nucleotide("C")
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        # Testing correct init with thymine
        try:
            nc = Nucleotide("T")
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        # Testing correct init with uracil
        try:
            nc = Nucleotide("U")
            self.assertTrue(True)
        except:
            self.assertTrue(False)
        # Testing incorrect init with no base
        error = False
        try: 
            nc = Nucleotide()
            error = True
        except:
            self.assertTrue(True)
        finally:
            if error:
                self.assertTrue(False)
        # Testing incorrect init with unknown base. Expect exception
        error = False
        try: 
            nc = Nucleotide("Q")
            error = True
        except:
            self.assertTrue(True)
        finally:
            if error:
                self.assertTrue(False)


    def test_execution(self):
        """
        Tests the general execuation of the testing file.
        
        :param self: An instance of the Nucleotide_Tests class
        """
        self.assertTrue(True)
          


if __name__ == '__main__':
    unittest.main()
