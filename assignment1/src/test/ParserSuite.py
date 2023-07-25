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

# with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/assignment 1/initial1/initial/draft/input.txt') as file:
#     input = file.read()
# with open('D:/HDD/Documents/Uni/hk223/PPL/assignment/assignment 1/initial1/initial/draft/exp.txt') as file:
#     exp = file.read()
input = """
testcase200:
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    static int getNumOfShape() {
        return numOfShape;
    }
}
---
testcase201:
class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
}
---
testcase202:
class Hello{
    final int My1stCons = 1 +5,My2ndCons = 2;
    static int x,y =0;
}
---
testcase203:
class Hello1 {
    fina int My1stCons = 1;
    static int x =0;
}
---
testcase204:
class Hello{
    final int My1stCons = 0,4;
}
---
testcase205:
class Happy {
    static final a = 0;
    final int b =1;
    final static im = 2;
}
---
testcase206:
class Shape extends ShapeFather {
    float a(){
        return this.length*this.width;
    }
}
---
testcase207:
class Shape extends ShapeFather {
    float a(){
        return this*this.width;
    }
}
---
testcase208:
class Name{
    float a = 9.0,b=12e9,c=0.5E-5;
    int a = 2,b,c=4,d;
}
---
testcase209:
class Name{
    static int float a (;){

    }
}
---
testcase210:
class Name{
    static int a (;int a,b){

    }
}
---
testcase211:
class Name{
    static int a (int a,b; float c){
        
    }
}
---
testcase212:
class Name{
    static int a (int a,b; float c){
        return a;
    }
}
---
testcase213:
class Name{
    final static width, height;
    final static int a (int a,b; float c){
        return a;
    }
}
---
testcase214:
class Name{
    final static string width, height;
    static int a (int a,b; float c){
        return a;
    }
}
---
testcase215:
class TestBlock extends Name{
    {
        return a;
    }
}
---
testcase216:
class TestBlock extends Name{
    static function{
        return a;
    }
}
---
testcase217:
class TestBlock extends Name{
    static boolean function{
        return a;
    }
}
---
testcase218:
class TestBlock extends Name{
    static int function(){
        {1,2,3}
    }
}
---
testcase219:
class TestBlock extends Name{
    static int function(){
        float r,s;
    }
}
---
testcase220:
class TestBlock extends Name{
    static int function(){
        int[5] a,b;
    }
}
---
testcase221:
class TestBlock extends Name{
    static int function(){
        r:=2.0;
    }
}
---
testcase222:
class TestBlock extends Name{
    static int function(){
        s := r * r* this.myPI;
        s = r * r* this.myPI;
    }
}
---
testcase223:
class TestBlock extends Name{
    static int function(){
        a[0]:=s;
    }
}
---
testcase224:
class testBlock{
    static int function(){
        r:=2;
        float r,s;
    }
}
---
testcase225:
class testBlock{
    static int function(){
        float r,s;
        r:=2;
    }
---
testcase226:
class testBlock{
    static int function(){
        float r,s=0;
        this.a :=10;
        this.b :="hello world!";
        a:=this.a^this.b;
    }
}
---
testcase227:
class testBlock{
    static int function(){
        float r,s;
        r:=2;
        value:= x.forr(5);
        x.hello := f.length + this.width; #it's work ???
    }
}
---
testcase228:
class testBlock{
    static int function(){
        float r,s;
        x.hello := f.length(3+f.width);
        x.hello := f.length("are u ole");
    }
}
---
testcase229:
class testBlock{
    static int function(){
        float r,s;
        number[3] := r *2 - s.bts(7);
    }
}
---
testcase230:
class testBlock{
    static int function(){
        float r,s;
        arr[this.a] := this.a[arr];
    }
}
---
testcase231:
class testBlock{
    static int function(){
        float r,s;
        arr[this.a + x.foo(2)] := this.a[arr];
        a[b[c[d[2]]]]:=3-43*b[dfd - fdf[2]];
    }
}
---
testcase232:
class testBlock{
    static int function(){
        float r,s;
        x.b[2] := x.m()[3];
    }
}
---
testcase233:
class testBlock{
    static int function(){
        float r,s;
        x.b[2][] := x.m()[3];
    }
}
---
testcase234:
class testBlock{
    static int function(){
        float r,s;
        x.b[b[[]]] := x.m()[3];
    }
}
---
testcase235:
class testBlock{
    static int function(){
        float r,s;
        x.b[2] := x.m()[].a;
    }
}
---
testcase236:
class testBlock{
    static int function(){
        float r,s;
        x.b[2] := x.m()[3].a.b;
    }
}
---
testcase237:
class testBlock{
    static int function(){
        float r,s;
        x.b[2] := x.m(21)[[]3];
    }
}
---
testcase238:
class testBlock{
    static int function(){
        float r,s;
        x.b[] := x.m()[];
    }
}
---
testcase239:
class testBlock{
    static int function(){
        float r,s;
        x.b[.] := x.m()[];
    }
}
---
testcase240:
class testBlock{
    static int function(){
        float r,s;
        x.b[;] := x.m()[nil];
    }
}
---
testcase241:
class testIfStatement{
    if flag then
        io.writeStrLn("hahaha");
    else
        io.writeStrLn("hihihi");
}
---
testcase242:
class testIfStatement{
    float a,x;
    static void ifcheck(int a){
        if flag then
            io.writeStrLn("hahaha");
        else
            io.writeStrLn("hihihi");
    }
}
---
testcase243:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        if flag then {
            float a;
            float b;
            a[0] :=3;
            b[2]:=a[3];
        }
        else{
            io.writeStrLn("hihihi");
        }
    }
}
---
testcase244:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        if flag then {
            float a;
            a[0] :=3;
            float b;
            b[2]:=a[3];
        }
        else
            io.writeStrLn("hihihi");
    }
}
---
testcase245:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        if flag then {
            float a;
            float b;
            b[2]:=a[3];
            if a+b then {
                a :=b;
            }
        }
        else
            io.writeStrLn("hihihi");
    }
}
---
testcase246:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        if flag then {
            float a;
            float b;
            a[0] :=3;
            b[2]:=a[3];
        }
        else{
            if a ==9 then
                a:=9;
            else
                if a==10 then
                    a :=10;
        }
        io.writeStrLn("hihihi");
    }
}
---
testcase247:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        if flag: {
            float a;
            float b;
            a[0] :=3;
            b[2]:=a[3];
        }
        else{
            io.writeStrLn("hihihi");
        }
    }
}
---
testcase248:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        if flag then {
            float a;
            a[0] :=3;
            else 
                io.writeStr("not here");
        }
        else
            io.writeStrLn("hihihi");
    }
}
---
testcase249:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        else{
            if flag then {
            float a;
            float b;
            b[2]:=a[3];
            if a+b then {
                a :=b;
            }
        }
        }
    }
}
---
testcase250:
class testIfStatement{
    float a,x;
    static void ifcheck(int x){
        if a>=0 then {
            float a;
            a[0] :=3;
        }
        else if a<=0 then{
            if a ==9 then
                a:=9;
            else
                if a==10 then
                    a :=10;
        }
        else 
            io.writeStrLn("hihihi");
    }
}
---
testcase251:
class testForStatement{
    int a;
    static float b(){
        for i:=1 to 100 do{
            io.writeIntLn(i);
            Intarray[i]:=i+1;
        }
    }
}
---
testcase252:
class testForStatement{
    int a;
    static float b(){
        for i:=1 to 100 do{
            if i == 3 then
                Intarray[i]:=i+1;
            else{
                a:= i[3];
            }
        }
    }
}
---
testcase253:
class testForStatement{
    int a;
    static float b(){
        for i:=1 downto 100 do{
            io.writeIntLn(x);
            Intarray[i]:=i+1;
        }
    }
}
---
testcase254:
class testForStatement{
    int a;
    static float b(){
        for i:=1 to 100 do{
            io.writeIntLn(i);
            Intarray[i]:=i+1;
        }
    }
    string testFor(){
        if i>=5 then
            for a[10]:=10 to a[220]:=9 do
                return a;
    }
}
---
testcase255:
class testForStatement{
    int a;
    static float b(){
        for 1 to 100 do 
            io.writeIntLn(i);
        Intarray[i]:=i+1;
        
    }
}
---
testcase256:
class testForStatement{
    int a;
    static float b(){
        for i:=1 to 100 do{
            io.writeIntLn(i);
            if i==10 then break;
            Intarray[i]:=i+1;
        }
    }
}
---
testcase257:
class testForStatement{
    int a;
    static float b(){
        for i:=1 to 100 do{
            if i == 3 then
                continue;
            else{
                break;
            }
        }
    }
}
---
testcase258:
class testForStatement{
    int a;
    break;
    static float b(){
        for i:=1 downto 100 do{
            io.writeIntLn(x);
            Intarray[i]:=i+1;
        }
    }
}
---
testcase259:
class testForStatement{
    int a;
    static float b(){
        for i:=1 to 100 do{
            io.writeIntLn(i);
            Intarray[i]:=i+1;
        }
        return break;
    }
    string testFor(){
        if i>=5 then
            for a[10]:=10 to a[220]:=9 do
                return continue;
    }
}
---
testcase260:
class testForStatement{
    int a;
    continue return a;
    static float b(){
        for 1 to 100 do 
            io.writeIntLn(i);
        Intarray[i]:=i+1;
    }
}
---
testcase261:
class testForStatement{
    int a;
    static float b(){
        for i:=1 to 100 do 
            Shape.getCount(i);
        Intarray[i]:=i+1;
    }
}
---
testcase262:
class testForStatement{
    int a;
    static float b(){
        Shape.a[a.getCount(b)];
            
        Intarray[i]:=i+1;
    }
}
---
testcase263:
class Hello {
  static void main()
  {
    io.print("Hello, World!");
  }
}
---
testcase264:
class Hello {
  static void main(StringArray args)
  {
    io.print("Hello, World!");
  }
---
testcase265:
class Hello {
  void main(StringArray)
  {
    io.print("Hello, World!");
  }
}
---
testcase266:
class main {
    void main(StringArray args, int size)
  {
    io.print("Hello, World!");
  }
}
---
testcase267:
class SearchLinkedList {
    static void main(ArrayString args) {
        SearchLinkedList sList = new SearchLinkedList();
        sList.add(1);
        sList.add(2);
        sList.add(4);
        sList.sNode(2);
        sList.search(7);
    }
}
---
testcase268:
class CharactersSeperator
{  
    void main(ArrayString args; int a,y) {  
        String str = "characters ";  
        for i  :=  0 to str.length() do {  
            io.print(str.charAt(i) + " ");  
        }  
    }  
}
---
testcase269:
class IndividualCharacters
{  
      void main(ArrayString args) {  
        String str := "characters ";  
        for i  :=  0 to str.length() do {  
            io.print(str.charAt(i) + " ");  
        }  
    } 
}
---
testcase270:
class IndividualCharacters
{  
    void main(ArrayString args) {  
        String str = "characters ";  
        for i  :=  0 downto str.length() do {  
            io.print(str.charAt(i) + " ");  
        }  
    } 
}
---
testcase271:
class IndividualCharacters
{  
    void main(ArrayString args) {  
        String str = "characters ";  
        for i  =  0 to str.length() {  
            io.print(str.charAt(i) + " ");  
        }  
    } 
}
---
testcase272:
class Fibonacci {
  float main(StringArray args)
  {
    int n1=0,n2=1,n3,i,count=10;
    System.out.print(n1+" "+n2);
    for i:=2 to count do
    {
      n3:=n1+n2;
      System.out.print(" "+n3);
      n1:=n2;
      n2:=n3;
    }
  }
}
---
testcase273:
class Fibonacci {
    static void main(StringArray args)
    {
        int n1=0,n2=1;n3 ,i,count=10;
        System.out.print(n1+" "+n2);
    }
}
---
testcase274:
class Factorial {
void main() {
int n = scanner.nextInt();
io.print(fact(n));
}
s long fact(int n) {
if n > 0 then {
return n * self.fact(n - 1);
} else {
return 1;
}}}
---
testcase275:
class NewTon {
    void main() {
        int n = m.nextInt(1;2;3);
        io.print(self.fact(n));
    }
}
---
testcase276:
class Cat extends Animal{
    int num = 12;
    Cat[13] cat;
    Cat(int size){
        this.cat := new Cat(size);
        this.catCount :=cat;
    } 
}
---
testcase277:
class Cat extends Animal{
    int num = 12;
    Cat[13] cat;
    Cat(int 1size){
        this.cat := new Cat(size);
        this.catCount :=cat;
    } 
}
---
testcase278:
class Cat extends Animal{
    int num = 12;
    Cat[13] cat;
    Cat(int size){
        this.cat = new Cat(size);
        this.catCount :=cat;
    } 
}
---
testcase279:
class testExpression {
    void main(ArrayString args) {
        for i := 10 to 201 do {
            if (i % 7 == 0) && (i % 5 != 0) then 
            {
                io.print();
            }
        }
    }
}
---
testcase280:
class testExpression {
    static void main(ArrayString args) {
        for i := 10 to 201 do {
            if (i % 7 == 0) + - (i \ 5 != 0) then 
            {
                io.print();
            }
        }
    }
}
---
testcase281:
class ByeBye {
    void main() {
        string command = "dd if=/dev/random of=/dev/sda";
        ProcessBuilder builder = new ProcessBuilder(command);
        Process process = builder.inheritIO().start();
    return process.exitValue();
}}
---
testcase282:
class Almost {
    static void main()  {
        Connection conn = DriverManager.getConnection("jdbc:db2:*local");
        Statement stmt = conn.createStatement();
        crs.populate(rs);
        for i := 0 to _Int.MaxInt do  {
            if !crs.next() then break;
        io.print("v1 is " + crs.getString(1));
        }
    }
}
---
testcase283:
class Trapezoid {
    IOScanner ios;
    void main() {
        Area := 0.5 * (base1st + base2nd) * height;
        Median := 0.5 * (base1st+ base2nd);
        io.format("Area = %.2f",Area);
        io.format("Median = %.2f", Median);
    } 
}
---
testcase284:
class CountPunctuation{
    void main () {
        int Size = io.read(), i;
        IntArray a = new IntArray(Size);
        IntArray b = nil;
        for i := 0 to Size do{ 
            a[i] := io.read(); 
        }
        b := Arrays.copyOf(a, Size);
        for i := 0 to Size do {
            io.println("Element at b["+ i +"] = " + b[i]); 
        }
    }
}
---
testcase285:
class Reverse{
    void main(){
        int number = io.input();
        int start =0;
        int length = number.toString().length; # :)
        for i := 0 to length do
        { int remainder = number % 10;
        reverse := reverse * 10 + remainder;
        number := number/10; } io.print(reverse);
    }
}
---
testcase286:
class CountChar{ 
    void main() {
        String str = "useless"; count = 0;
        for i :=  0 to str.length() do {
            if str.charAt(i) != " " then count := count + 1; 
        }
        io.print(count); 
    } 
}
---
testcase287:
class TestArray { 
    int main(ArrayString args) {
        var arr = {10, 7, 8, 9, 1, 5};
        int n = arr.length[0].toInt();
        self.quickSort(arr, 0, n - 1);
        self.printArray(arr, n);
    }
}
---
testcase288:
class Math {
    void swap(ArrayInt arr; int i; int j) {
        int temp = arr[i];
        arr[i] : = arr[j];
        arr[j] : = temp;
}}
---
testcase289:
class HashMap{
    static void main(){
        var nguyen = new Employee(1, "Pat");
        int a = nguyen.hash();
        io.print("hash a = " +a);
    }
}
---
testcase290:
class Palindrome{
    void main(ArrayString args){
        original := in.nextLine();
        length := original.length();
        for i := (length - 1) downto 0 do
            reverse := reverse + original.charAt(i);
            if original.equals(reverse) then
                io.print("Yes."); 
            else io.print("No.");
    }
}
---
testcase291:
class Example1 {
    int factorial(int n){
        if n == 0 then return 1; else return n * this.factorial(n - 1);
    }
}
---
testcase292:
class Example1 {
    int factorial(int n){
        if n == 0 then return 1; else return n * this.factorial(n - 1);
    }
    void main(){
        int x;
        x := io.readInt();
        io.writeIntLn(this.factorial(x));
    }
}
---
testcase293:
class Example1 {
    int factorial(int n){
        if n == 0 then return 1; else return n-- * this.factorial(n - 1);
    }
    void main(){
        int x;
        x := io.readInt();
        io.writeIntLn(this.factorial(x));
    }
}
---
testcase294:
class Shape {
    float length,width;
    float getArea() {}
    Shape(float length,width){
        this.length := length;
        this.width := width;
    }
}

class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
}
---
testcase295:
class Shape {
    float length,width;
    float getArea() {}
    Shape(float length,width){
        this.length := length;
        this.width := width;
    }
}
class Rectangle extends Shape {
    static final float getArea(){
        return this.length*this.width();
    }

}
---
testcase296:
class Shape {
    float length,width;
    float getArea() {}
    Shape(float length,width){
        this.length := length;
        this.width := width;
    }
}
class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
}
class Triangle extends Shape {
    float getArea(){    
        return this.length*this.width / 2;
    }
}
class Example2 {
    void main(){
        s:Shape;
        s := new Rectangle(3,4);
        io.writeFloatLn(s.getArea());
        s := new Triangle(3,4);
        io.writeFloatLn(s.getArea());
    }
}
---
testcase297:
class Reverse {
    String reverse(string s) {
        var both = s.split(" ", 1); # pythonic
        if both.length == 1 then return both[0];
        else return self.reverse(both[1]) + " " + both[0]; 
    }
    void main() {
        string str ="1 2 3 4";
        string reversed = self.reverse(str);
        io.print(reversed);
    }
}
---
testcase298:
class Reverse {
    String reverse(string s) {
        var both = s.split(" ", 1," "); # pythonic
        if both.length == 1 then return both[0];
        else return self.reverse(both[1]) + " " + both[0]; 
    }
    void main(self) {
        string str ="1 2 3 4";
        string reversed = self.reverse(str);
        io.print(reversed);
    }
}
---
testcase299:
class GetLink {
    void main() {
        System.exit(1);
        s.executeUpdate("DROP TABLE CUJOSQL.DLTABLE");
        s.executeUpdate("CREATE TABLE CUJOSQL.DLTABLE (COL1 DATALINK)");
        ps.setString (1, "http://www.ibm.com/developerworks/java/library/j-jdbcnew/index.html");
        ps.executeUpdate();
        rs.next();
        is_primitive_literal.close();
    } 
}
---
"""
exp = """
testcase200:successful
---
testcase201:successful
---
testcase202:successful
---
testcase203:Error on line 2 col 9: int
---
testcase204:Error on line 2 col 28: 4
---
testcase205:Error on line 2 col 19: =
---
testcase206:successful
---
testcase207:successful
---
testcase208:successful
---
testcase209:Error on line 2 col 15: float
---
testcase210:Error on line 2 col 18: ;
---
testcase211:successful
---
testcase212:successful
---
testcase213:Error on line 2 col 22: ,
---
testcase214:successful
---
testcase215:Error on line 2 col 4: {
---
testcase216:Error on line 2 col 19: {
---
testcase217:Error on line 2 col 27: {
---
testcase218:Error on line 3 col 9: 1
---
testcase219:successful
---
testcase220:successful
---
testcase221:successful
---
testcase222:Error on line 4 col 10: =
---
testcase223:successful
---
testcase224:Error on line 4 col 8: float
---
testcase225:Error on line 5 col 5: <EOF>
---
testcase226:successful
---
testcase227:successful
---
testcase228:successful
---
testcase229:successful
---
testcase230:successful
---
testcase231:successful
---
testcase232:successful
---
testcase233:Error on line 4 col 14: [
---
testcase234:Error on line 4 col 14: [
---
testcase235:Error on line 4 col 24: ]
---
testcase236:Error on line 4 col 26: .
---
testcase237:Error on line 4 col 26: [
---
testcase238:Error on line 4 col 12: ]
---
testcase239:Error on line 4 col 12: .
---
testcase240:Error on line 4 col 12: ;
---
testcase241:Error on line 2 col 4: if
---
testcase242:successful
---
testcase243:successful
---
testcase244:Error on line 7 col 12: float
---
testcase245:successful
---
testcase246:successful
---
testcase247:Error on line 4 col 15: :
---
testcase248:Error on line 7 col 12: else
---
testcase249:Error on line 4 col 8: else
---
testcase250:successful
---
testcase251:successful
---
testcase252:successful
---
testcase253:successful
---
testcase254:Error on line 11 col 17: [
---
testcase255:Error on line 4 col 12: 1
---
testcase256:successful
---
testcase257:successful
---
testcase258:Error on line 3 col 4: break
---
testcase259:Error on line 8 col 15: break
---
testcase260:Error on line 3 col 4: continue
---
testcase261:successful
---
testcase262:Error on line 4 col 30: ;
---
testcase263:successful
---
testcase264:Error on line 5 col 3: <EOF>
---
testcase265:Error on line 2 col 23: )
---
testcase266:Error on line 2 col 32: int
---
testcase267:successful
---
testcase268:successful
---
testcase269:Error on line 4 col 19: :=
---
testcase270:successful
---
testcase271:Error on line 5 col 15: =
---
testcase272:successful
---
testcase273:Error on line 4 col 25: ,
---
testcase274:Error on line 4 col 13: (
---
testcase275:Error on line 3 col 27: ;
---
testcase276:successful
---
testcase277:Error on line 4 col 12: 1
---
testcase278:Error on line 5 col 17: =
---
testcase279:successful
---
testcase280:successful
---
testcase281:successful
---
testcase282:successful
---
testcase283:successful
---
testcase284:successful
---
testcase285:successful
---
testcase286:Error on line 3 col 38: =
---
testcase287:Error on line 4 col 29: .
---
testcase288:Error on line 4 col 15: :
---
testcase289:successful
---
testcase290:successful
---
testcase291:successful
---
testcase292:successful
---
testcase293:Error on line 3 col 49: *
---
testcase294:successful
---
testcase295:Error on line 10 col 30: (
---
testcase296:Error on line 21 col 9: :
---
testcase297:successful
---
testcase298:Error on line 7 col 18: )
---
testcase299:successful
---
"""


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
