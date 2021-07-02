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
    def test_ne(self):
        """
        Tests the overload inequality operator for the class.
        
        :param self: An instance of the Nucleotide_Tests class
        """
        a = Nucleotide("A")
        g = Nucleotide("G")
        c = Nucleotide("C")
        t = Nucleotide("T")
        u = Nucleotide("U")
        a2 = Nucleotide("A")
        g2 = Nucleotide("G")
        c2 = Nucleotide("C")
        t2 = Nucleotide("T")
        u2 = Nucleotide("U")
        # Testing for Adenine
        self.assertTrue(a != g)
        self.assertTrue(a != 'g')
        self.assertFalse(a != a)
        self.assertFalse(a != 'a')
        self.assertFalse('a' != a)


    def test_eq(self):
        """
        Tests the overload equality operator for the class.
        
        :param self: An instance of the Nucleotide_Tests class
        """
        a = Nucleotide("A")
        g = Nucleotide("G")
        c = Nucleotide("C")
        t = Nucleotide("T")
        u = Nucleotide("U")
        a2 = Nucleotide("A")
        g2 = Nucleotide("G")
        c2 = Nucleotide("C")
        t2 = Nucleotide("T")
        u2 = Nucleotide("U")
        # Testing for Adenine
        self.assertTrue(a == a)
        self.assertTrue(a == a2)
        self.assertTrue(a == 'a')
        self.assertTrue(a == 'A')
        self.assertTrue('a' == a)
        self.assertFalse(a == g)
        self.assertFalse(a == c)
        self.assertFalse(a == t)
        self.assertFalse(a == u)
        # Testing for Cytosine
        self.assertTrue(c == c2)
        self.assertFalse(c == g)
        self.assertFalse(c == a)
        self.assertFalse(c == t)
        self.assertFalse(c == u)
        # Testing for Guanine
        self.assertTrue(g == g)
        self.assertTrue(g == g2)
        self.assertFalse(g == c)
        self.assertFalse(g == a)
        self.assertFalse(g == t)
        self.assertFalse(g == u)
        # Testing for Thymine
        self.assertTrue(t == t)
        self.assertTrue(t == t2)
        self.assertFalse(t == c)
        self.assertFalse(t == a)
        self.assertFalse(t == g)
        # Testing for uracil
        self.assertTrue(u == u)
        self.assertTrue(u == u2)
        self.assertFalse(u == c)
        self.assertFalse(u == a)
        self.assertFalse(u == t)
        self.assertFalse(u == g)


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
        self.assertTrue(a.complement(t))
        self.assertFalse(a.complement(a))
        self.assertFalse(a.complement(g))
        self.assertFalse(a.complement(c))
        self.assertTrue(a.complement(u))
        
        # Testing Uracil binding rules
        self.assertTrue(u.complement(a))
        self.assertFalse(u.complement(t))
        self.assertFalse(u.complement(g))
        self.assertFalse(u.complement(c))
        self.assertFalse(u.complement(u))
        
        # Testing Thymine binding rules
        self.assertTrue(t.complement(a))
        self.assertFalse(t.complement(t))
        self.assertFalse(t.complement(g))
        self.assertFalse(t.complement(c))
        self.assertFalse(t.complement(u))

        # Testing guanine binding rules
        self.assertTrue(g.complement(c))
        self.assertFalse(g.complement(a))
        self.assertFalse(g.complement(g))
        self.assertFalse(g.complement(t))
        self.assertFalse(g.complement(u))

        # Testing cytosine binding rules
        self.assertTrue(c.complement(g))
        self.assertFalse(c.complement(a))
        self.assertFalse(c.complement(c))
        self.assertFalse(c.complement(t))
        self.assertFalse(c.complement(u))        
        

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
