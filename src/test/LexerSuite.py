import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        input="#this is a comment"
        exp="<EOF>"
        self.assertTrue(TestLexer.test(input,exp,101))
    def test_lowercase_identifier1(self):
        """test identifiers"""
        input="#this is a comment/*this is not mean"
        exp="<EOF>"
        self.assertTrue(TestLexer.test(input,exp,102))
    def test_lowercase_identifier2(self):
        """test identifiers"""
        input="/*this is a comment*/"
        exp="<EOF>"
        self.assertTrue(TestLexer.test(input,exp,103))
    def test_lowercase_identifier3(self):
        """test identifiers"""
        input="/*this is a comment #this is a comment*/"
        exp="<EOF>"
        self.assertTrue(TestLexer.test(input,exp,104))
    def test5(self):
        """test identifiers"""
        input="{1,3}"
        exp=input+"<EOF>"
        self.assertTrue(TestLexer.test(input,exp,105))
