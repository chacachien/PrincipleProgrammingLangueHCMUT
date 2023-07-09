import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # def test_lowercase_identifier(self):
    #     """test identifiers"""
    #     input="#this is a comment"
    #     exp="<EOF>"
    #     self.assertTrue(TestLexer.test(input,exp,101))
    # def test_lowercase_identifier1(self):
    #     """test identifiers"""
    #     input="#this is a comment/*this is not mean"
    #     exp="<EOF>"
    #     self.assertTrue(TestLexer.test(input,exp,102))
    # def test_lowercase_identifier2(self):
    #     """test identifiers"""
    #     input="/*this is a comment*/"
    #     exp="<EOF>"
    #     self.assertTrue(TestLexer.test(input,exp,103))
    # def test_lowercase_identifier3(self):
    #     """test identifiers"""
    #     input="/*this is a comment #this is a comment*/"
    #     exp="<EOF>"
    #     self.assertTrue(TestLexer.test(input,exp,104))
    # def test5(self):
    #     """test identifiers"""
    #     input="{1,3}"
    #     exp='{,1,,,3,},'+"<EOF>"
    #     self.assertTrue(TestLexer.test(input,exp,105))
    @staticmethod
    def generate_test_method(testNumber,input,exp):
        def test_method(self):
            self.assertTrue(TestLexer.test(input,exp,testNumber))
        return test_method

f = open('D:/HDD/Documents/Uni/hk223/PPL/assignment/assignment 1/initial1/initial/draft/input.txt')
e = open('D:/HDD/Documents/Uni/hk223/PPL/assignment/assignment 1/initial1/initial/draft/exp.txt')

testcase=[]
exp = []
i=100
while True:
    input_str=''
    for x in f:
        input_str+=x
        if x.strip() == '---': break
    else: break
    start_string = f'testcase{i}:'
    end_string ='---'
    startIndex = input_str.index(start_string) + len(start_string)
    endIndex= input_str.index(end_string)
    content = input_str[startIndex:endIndex]
    testcase.append(content)
    i=i+1
i=100
while True:
    expStr=''
    for x in e:
        expStr+=x
        if x.strip()=='---': break
    else: break
    startStr = f'testcase{i}:'
    endStr = '---'
    startIndex = expStr.index(startStr) + len(startStr)
    endIndex = expStr.index(endStr)
    content = expStr[startIndex:endIndex]
    exp.append(content.strip())
    i=i+1
f.close()
e.close()
for i in range(len(testcase)):
    input = testcase[i]
    expindex = exp[i]
    test_method = LexerSuite.generate_test_method(i+100, input, expindex)
    setattr(LexerSuite, f"test{str(i)}", test_method)