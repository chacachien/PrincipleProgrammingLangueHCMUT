import unittest
from TestUtils import TestAST
from AST import *

# class ASTGenSuite(unittest.TestCase):
#     def test_simple_program(self):
#         """Simple program: class main {} """
#         input = """class main {}"""
#         expect = str(Program([ClassDecl(Id("main"),[])]))
#         self.assertTrue(TestAST.test(input,expect,300))

#     def test_class_with_one_decl_program(self):
#         """More complex program"""
#         input = """class main {
#             a:integer;
#         }"""
#         expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
#         self.assertTrue(TestAST.test(input,expect,301))
    
#     def test_class_with_two_decl_program(self):
#         """More complex program"""
#         input = """class main {
#             a:integer;
#             b:integer;
#         }"""
#         expect = str(Program([ClassDecl(Id("main"),
#             [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
#              AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
#         self.assertTrue(TestAST.test(input,expect,302))
   
   


class ASTGenSuite(unittest.TestCase):
    def generate_test_method(testNumber,input,exp):
        
        def test_simple_program(self):
            """Simple program: class main {} """
            self.assertTrue(TestAST.test(input,exp,testNumber))
        return test_simple_program

import re
with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/code/PrincipleProgrammingLangueHCMUT/assignment2/testcasehandmade/input.txt') as f:
    f = f.read()
with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/code/PrincipleProgrammingLangueHCMUT/assignment2/testcasehandmade/exp.txt') as e:
    e = e.read()

testcase=[]
exp = []
pattern= r"testcase(\d+):(.*?)---"
match = re.findall(pattern, f,re.DOTALL)

for m in match:
    testcase.append(m[1].strip())

match = re.findall(pattern, e,re.DOTALL)
for m in match:
    exp.append(m[1].strip())
for i in range(len(testcase)):
    input = testcase[i]
    expindex = exp[i]
    test_method = ASTGenSuite.generate_test_method(i+300, input, expindex)
    setattr(ASTGenSuite, f"test{str(i)}", test_method)