import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    @staticmethod
    def generate_test_method(testNumber,input,exp):
        def test_method(self):
            self.assertTrue(TestLexer.test(input,exp,testNumber))
        return test_method
fstr="""
testcase100:/*this is a comment*/
---
testcase101:/*this is a comment #this is no meaning*/
---
testcase102:/*this is a comment
in many line */
---
testcase103: #this is also a comment in a line
---
testcase104: #this is a comment /* this is no effect
---
testcase105: class Shape
---
testcase106: static final int numOfShape = 0;
---
testcase107: final int immuAttribute = 0;
---
testcase108: float length,width;
---
testcase109: static int getNumOfShape(){}
---
testcase110: return numOfShape;
---
testcase111: class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
}
---
testcase112: final int My1stCons = 1 +5,My2ndCons = 2;
---
testcase113: static int x,y = 0;
---
testcase114: a := 5 #this is a line comment
---
testcase115: AbaA_9
---
testcase116: _hahaha
---
testcase117: 12hahaha
---
testcase118: ahahaha
---
testcase119: _hello9Fuincion hello
---
testcase120:boolean break class continue do else
extends float if int new string
then for return true false void
nil this final static to downto
---
testcase121:a+b
---
testcase122: a*b!c
---
testcase123:a\c/d
---
testcase124:ash?dasfj
---
testcase125: a<<<b<==
---
testcase126: a|||logical
---
testcase127: a!b!!c
---
testcase128: new a 
---
testcase129: a-b--c--d
---
testcase130:a%b-d%g
---
testcase131:a==>b
---
testcase132:d>=d>==e
---
testcase133:ed&&a&e
---
testcase134:a^d^^b
---
testcase135:a{hihi}()
---
testcase136: a[5],a[{.}]
---
testcase137: b.new;,()
---
testcase138:0 100 255 2500
---
testcase139: 878~45
---
testcase140:9.0 12e8 1. 0.33E-3 123e+42
---
testcase141:.13
---
testcase142:143e
---
testcase143:a = true, b =false
---
testcase144:"This is a string containing tab \t"
---
testcase145:"He asked me: \\"Where is John?\\""
---
testcase146:"this is a string contain backspace \b"
---
testcase147:"this is a string contain \f"
---
testcase148:"this is a string contain \\r"
---
testcase149:"this is a string contain \\n"
---
testcase150:"this is a string contain \\""
---
testcase151:"this is a string contain \\\\"
---
testcase152: {1,2,3}
---
testcase153:{2.3,4.2,102e3}
---
testcase154:int[5] a
---
testcase155:"this is a normal string"
---
testcase156: "this is a string" ^ "another string"
---
testcase157:"a
---
testcase158: "this is a array {a,d,d}"
---
testcase159:"this is a interger 3.22 and 34"
---
testcase160:"this is a new in string"
---
testcase161:'this is not s string'
---
testcase162:"this is a string
---
testcase163:"this is accessiblest
string
---
testcase164:"this is a ill \\a"
---
testcase165:a[3+x.foo(2)]
---
testcase166:#start of decl
float r,s
---
testcase167:this.a := 3.14;
---
testcase168:song  := a.func(5)
---
testcase169:song[4] :=song*2
---
testcase170:song[] =:=
---
testcase171: if flag then
---
testcase172: else 
io.writeStrLn("hahaha")
---
testcase173: for i:=0 to 100 do
---
testcase174: for x:=0 downto 2
---
testcase175: for 2 to 3 downto
---
testcase176: breaka break abreak
---
testcase177: return a returna return.
---
testcase178: returnbreaknil nil nill nul
---
testcase179:Shape.getNum();
---
testcase180: ioo oio
---
testcase181:class Axample1 { 
---
testcase182:if n == 0 then return 1
---
testcase183: else return n*this.factoria(n-1)
---
testcase184: e.10e8 e10.34 334e..23
---
testcase185: E.e10e EEE10 10.E
---
testcase186: 10,12 10.12 10...12 
---
testcase187: 10ee-9 10e-9 10e0 10.2e10
---
testcase188: void writeStrLn(anArg:string)
---
testcase189:string read:boolean
---
testcase190:x:=e10
---
testcase191:"Yankee-2017
"
---
testcase192:This@reallyrandom_bigIden
---
testcase193:/*Comment\nxuong hang*/
---
testcase194:#this is 134 / *\/''
---
testcase195:#this is a comment  " " "
---
testcase196:/* " " 
'''' % int 13.3
*/
---
testcase197:/*this is comment*/ but is not
---
testcase198:#this is comment /* this is comment */ and also this is
---
testcase199:"" "" "w
---
"""

estr="""
testcase100:<EOF>
---
testcase101:<EOF>
---
testcase102:<EOF>
---
testcase103:<EOF>
---
testcase104:<EOF>
---
testcase105:class,Shape,<EOF>
---
testcase106:static,final,int,numOfShape,=,0,;,<EOF>
---
testcase107:final,int,immuAttribute,=,0,;,<EOF>
---
testcase108:float,length,,,width,;,<EOF>
---
testcase109:static,int,getNumOfShape,(,),{,},<EOF>
---
testcase110:return,numOfShape,;,<EOF>
---
testcase111:class,Rectangle,extends,Shape,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>
---
testcase112:final,int,My1stCons,=,1,+,5,,,My2ndCons,=,2,;,<EOF>
---
testcase113:static,int,x,,,y,=,0,;,<EOF>
---
testcase114:a,:=,5,<EOF>
---
testcase115:AbaA_9,<EOF>
---
testcase116:_hahaha,<EOF>
---
testcase117:12,hahaha,<EOF>
---
testcase118:ahahaha,<EOF>
---
testcase119:_hello9Fuincion,hello,<EOF>
---
testcase120:boolean,break,class,continue,do,else,extends,float,if,int,new,string,then,for,return,true,false,void,nil,this,final,static,to,downto,<EOF>
---
testcase121:a,+,b,<EOF>
---
testcase122:a,*,b,!,c,<EOF>
---
testcase123:a,\,c,/,d,<EOF>
---
testcase124:ash,Error Token ?
---
testcase125:a,<,<,<,b,<=,=,<EOF>
---
testcase126:a,||,Error Token |
---
testcase127:a,!,b,!,!,c,<EOF>
---
testcase128:new,a,<EOF>
---
testcase129:a,-,b,-,-,c,-,-,d,<EOF>
---
testcase130:a,%,b,-,d,%,g,<EOF>
---
testcase131:a,==,>,b,<EOF>
---
testcase132:d,>=,d,>=,=,e,<EOF>
---
testcase133:ed,&&,a,Error Token &
---
testcase134:a,^,d,^,^,b,<EOF>
---
testcase135:a,{,hihi,},(,),<EOF>
---
testcase136:a,[,5,],,,a,[,{,.,},],<EOF>
---
testcase137:b,.,new,;,,,(,),<EOF>
---
testcase138:0,100,255,2500,<EOF>
---
testcase139:878,Error Token ~
---
testcase140:9.0,12e8,1.,0.33E-3,123e+42,<EOF>
---
testcase141:.,13,<EOF>
---
testcase142:143,e,<EOF>
---
testcase143:a,=,true,,,b,=,false,<EOF>
---
testcase144:This is a string containing tab \t,<EOF>
---
testcase145:He asked me: \\"Where is John?\\",<EOF>
---
testcase146:this is a string contain backspace \b,<EOF>
---
testcase147:this is a string contain \f,<EOF>
---
testcase148:this is a string contain \\r,<EOF>
---
testcase149:this is a string contain \\n,<EOF>
---
testcase150:this is a string contain \\",<EOF>
---
testcase151:this is a string contain \\\\,<EOF>
---
testcase152:{,1,,,2,,,3,},<EOF>
---
testcase153:{,2.3,,,4.2,,,102e3,},<EOF>
---
testcase154:int,[,5,],a,<EOF>
---
testcase155:this is a normal string,<EOF>
---
testcase156:this is a string,^,another string,<EOF>
---
testcase157:Unclosed String: a
---
testcase158:this is a array {a,d,d},<EOF>
---
testcase159:this is a interger 3.22 and 34,<EOF>
---
testcase160:this is a new in string,<EOF>
---
testcase161:Error Token '
---
testcase162:Unclosed String: this is a string
---
testcase163:Unclosed String: this is accessiblest
---
testcase164:Illegal Escape In String: this is a ill \\a
---
testcase165:a,[,3,+,x,.,foo,(,2,),],<EOF>
---
testcase166:float,r,,,s,<EOF>
---
testcase167:this,.,a,:=,3.14,;,<EOF>
---
testcase168:song,:=,a,.,func,(,5,),<EOF>
---
testcase169:song,[,4,],:=,song,*,2,<EOF>
---
testcase170:song,[,],=,:=,<EOF>
---
testcase171:if,flag,then,<EOF>
---
testcase172:else,io,.,writeStrLn,(,hahaha,),<EOF>
---
testcase173:for,i,:=,0,to,100,do,<EOF>
---
testcase174:for,x,:=,0,downto,2,<EOF>
---
testcase175:for,2,to,3,downto,<EOF>
---
testcase176:breaka,break,abreak,<EOF>
---
testcase177:return,a,returna,return,.,<EOF>
---
testcase178:returnbreaknil,nil,nill,nul,<EOF>
---
testcase179:Shape,.,getNum,(,),;,<EOF>
---
testcase180:ioo,oio,<EOF>
---
testcase181:class,Axample1,{,<EOF>
---
testcase182:if,n,==,0,then,return,1,<EOF>
---
testcase183:else,return,n,*,this,.,factoria,(,n,-,1,),<EOF>
---
testcase184:e,.,10e8,e10,.,34,334,e,.,.,23,<EOF>
---
testcase185:E,.,e10e,EEE10,10.,E,<EOF>
---
testcase186:10,,,12,10.12,10.,.,.,12,<EOF> 
---
testcase187:10,ee,-,9,10e-9,10e0,10.2e10,<EOF>
---
testcase188:void,writeStrLn,(,anArg,:,string,),<EOF>
---
testcase189:string,read,:,boolean,<EOF>
---
testcase190:x,:=,e10,<EOF>
---
testcase191:Unclosed String: Yankee-2017
---
testcase192:This,Error Token @
---
testcase193:<EOF>
---
testcase194:<EOF>
---
testcase195:<EOF>
---
testcase196:<EOF>
---
testcase197:but,is,not,<EOF>
---
testcase198:<EOF>
---
testcase199:,,Unclosed String: w
---
"""
import re
testcase=[]
exp = []
# i=100
# input_str=''
# for x in fstr.splitlines():
#     input_str+=x
#     if x.strip() == '---':
#         start_string = f'testcase{i}:'
#         end_string ='---'
#         startIndex = input_str.index(start_string) + len(start_string)
#         endIndex= input_str.index(end_string)
#         content = input_str[startIndex:endIndex]
#         testcase.append(content)
#         i=i+1
#         input_str=''
# i=100
# expStr=''
# for x in estr.splitlines():
#     expStr+=x
#     if x.strip()=='---':
#         startStr = f'testcase{i}:'
#         endStr = '---'
#         startIndex = expStr.index(startStr) + len(startStr)
#         endIndex = expStr.index(endStr)
#         content = expStr[startIndex:endIndex]
#         exp.append(content.strip())
#         i=i+1
#         expStr=''

pattern= r"testcase(\d+):(.*?)---"
match = re.findall(pattern, fstr,re.DOTALL)

for m in match:
    testcase.append(m[1].strip())

match = re.findall(pattern, estr,re.DOTALL)
for m in match:
    exp.append(m[1].strip())
for i in range(len(testcase)):
    input = testcase[i]
    expindex = exp[i]
    test_method = LexerSuite.generate_test_method(i+100, input, expindex)
    setattr(LexerSuite, f"test{str(i)}", test_method)