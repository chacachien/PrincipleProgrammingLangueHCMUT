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
    # def test1(self):
    #     """array int"""
    #     input = """{1, 2, 3}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))
    # def test2(self):
    #     """array float"""
    #     input = """{2.3, 4.2, 102e3}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    # def test3(self):
    #     """array string"""
    #     input = """{"fdsaf", "fdsaf", "fdsaf fdsaf"}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,203))
    # def test4(self):
    #     """array bool"""
    #     input = """{true, false, true, false}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,204))
    @staticmethod
    def generate_test_method(index,input,exp):
        def test_method(self):
            self.assertTrue(TestParser.test(input,exp,index))
        return test_method
    
import re

with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/assignment 1/initial1/initial/draft/input.txt') as file:
    input = file.read()
with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/assignment 1/initial1/initial/draft/exp.txt') as file:
    exp = file.read()

testcase=[]
expstr = []

pattern= r"testcase(\d+):(.*?)---"
match = re.findall(pattern, input ,re.DOTALL) # review later!!!
match2 = re.findall(pattern, exp ,re.DOTALL)  # review later!!!
for m in match:
    testcase.append(m[1].strip())
for m in match2:
    expstr.append(m[1].strip())

for i in range(len(testcase)) :
    input = testcase[i]
    expindex = expstr[i]
    test_method = ParserSuite.generate_test_method(i+200, input, expindex)
    setattr(ParserSuite, f"test{str(i+200)}", test_method)
