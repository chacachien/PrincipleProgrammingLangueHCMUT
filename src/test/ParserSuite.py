import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))
    def test1(self):
        """array int"""
        input = """{1, 2, 3}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test2(self):
        """array float"""
        input = """{2.3, 4.2, 102e3}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test3(self):
        """array string"""
        input = """{"fdsaf", "fdsaf", "fdsaf fdsaf"}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test4(self):
        """array bool"""
        input = """{true, false, true, false}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        