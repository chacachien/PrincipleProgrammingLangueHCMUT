import unittest
from TestUtils import TestChecker
from AST import *



class CheckerSuite(unittest.TestCase):
    def generate_test_method(testNumber,input,exp):
        
        def test_simple_program(self):
            """Simple program: class main {} """
            self.assertTrue(TestChecker.test(input,exp,testNumber))
        return test_simple_program

import re

with open('C:/Users/OnDoing/PrincipleProgrammingLangueHCMUT/assignment3/testcasehandmade/input.txt') as f:
    f = f.read()
with open('C:/Users/OnDoing/PrincipleProgrammingLangueHCMUT/assignment3/testcasehandmade/exp.txt') as e:
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
    test_method = CheckerSuite.generate_test_method(i+400, input, expindex)
    setattr(CheckerSuite, f"test{str(i)}", test_method)
    
    


# class CheckerSuite(unittest.TestCase):
#     def test_undeclared_function(self):
#         """Simple program: int main() {} """
#         input = """
# class foo{}
# class main extends foo {
#     int b;
#     int a (){ 
#     this.foo();}
#     int b;
# }
#             """
#         expect = "Redeclared Attribute: b"
#         self.assertTrue(TestChecker.test(input,expect,400))
    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([],[
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    