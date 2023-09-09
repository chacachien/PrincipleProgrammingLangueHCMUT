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

f = '''
testcase400:
class foo{}
class main extends foo {
    void aa (){    
        this.aa();
    }
}
---
testcase401:
class foo{}
class main extends foo {
    int b;
    int a (){ 
        int b;
    }
    int b;
}
---
testcase402:
class foo{}
class main extends foo {
    int b;
    int a (){}
    int a(){}
}
---
testcase403:
class foo{}
class main extends foo {
    int b;
    int a (int a; int b, a){ 
    this.foo();}
    int a(){}
}
---
testcase404:
class main extends foo {
    int b;
    int a (int a; int b){ 
    this.foo();}
}
---
testcase405:
class foo{}
class main extends foo {
    int b;
    int a (int a; int a){ 
    this.foo();}
}
class foo{}
---
testcase406:
class foo{}
class main extends foo {
    int b;
    int a (int a; int b){ 
    return this.b;}
}
class foo{}
---
testcase407:
class foo{}
class main extends foo {
    int b;
    int a (int a; int b){ 
        float a;
    this.foo();}
}
class foo{}
---
testcase408:
class foo{}
class main extends foo {
    int b;
    int a (int a; int b){ 
        final float a;
        this.foo();}
    int c(){
        int a;
    }
}
class foo{}
---
testcase409:
class foo{}
class main extends foo {
    int b;
    int a (int a; int b){ 
        this.foo();
        }
    int c(){
        int a;
    }
}
class foo{}
---
testcase410:
class foo{}
class main extends foo {
    int b = a;
    int a (int a; int b){ 
        this.foo();}
    int c(){
        int a;
    }
}
class foo{}
---
testcase411:
class foo{}
class main extends foo {
    final int b = a;
    int a (int a; int b){ 
        this.foo();}
    int c(){
        int a;
    }
}
class foo{}
---
testcase412:
class foo{}
class main extends foo {
    final int b = 323;
    int a (int a; int b){ 
        foo fo = new foo();
    }
    int c(){
        int a;
    }
}
---
testcase413:
class foo{}
class main extends foo {
    final int b = 21.5;
    int a (int a; int b){ 
        this.foo();}
    int c(){
        int a;
    }
}
---
testcase414:
class foo{}
class main extends foo {
    boolean b = 21.5;
    int a (int a; int b){ 
        this.foo();}
    int c(){
        int a;
    }
}
---
testcase415:
class foo{}
class main extends foo {
    A b = 21.5;
    int a (int a; int b){ 
        this.foo();}
    int c(){
        int a;
    }
}
---
testcase416:
class foo{}
class A {}
class main extends foo {
    A b = new A();
    int a (int a; int b){ 
        if a ==3 then{
            return b;
        }
        }
    int c(){
        int a;
    }
}
---
testcase417:
class foo{}
class A {}
class B {}
class main extends foo {
    A b = new B();
    int a (int a; int b){ 
        this.foo();}
    int c(){
        int a;
    }
}
---
testcase418:
class foo{}
class A {}
class B extends A{
    A b = new B();
    int a (int a; int b){ 
        return this.a;}
    int c(){
        int a;
    }
}
---
testcase419:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int c = this.a;
}
---
testcase420:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int c = this.b.a;
}
---
testcase421:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int c = this.b.a;
    int foo(int a){
        int b;
        int a;
    }
}
---
testcase422:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int c = this.b.a;
    int foo(int a){
        int b = a;
        float c = b;
        boolean d = a;
    }
}
---
testcase423:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int c = this.b.a;
    int foo(int a; float e){
        float b = a;
        float c = b;
        boolean d = a;
    }
}
---
testcase424:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int c = A.a;
    int foo(int a; float e){
        float b = a;
        float c = b;
        boolean d = a;
    }
}
---
testcase425:
class foo{}
class A {
    static int a;
}
class B extends A {
    A b = new B();
    int c = this.a;
    int foo(int a; float e){
        float b = a;
        float c = b;
        boolean d = a;
    }
}
---
testcase426:
class foo{}
class A {
    static int a;
}
class B extends A {
    A b = new B();

    int foo(int a; float e){
        float b = this.a;
    }
}
---
testcase427:
class foo{}
class A {
    static int a;
}
class B extends A {
    static A b = new B();

    int foo(int a; float e){
        float b = B.b;
    }
}
---
testcase428:
class foo{}
class A {
    static int a;
}
class B extends A {
    A b = new B();

    int foo(int a; float e){
        float b = new B();
    }
}
---
testcase429:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();

    int foo(int a; float e){
        float b = this.b.a;
    }
}
---
testcase430:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        B d = new B();
        int f = a;
        float g = e;
    }
}
---
testcase431:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        C d = new B();
        int f = a;
        float g = e;
    }
}
---
testcase432:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        
        int f = this.g;
    }
}
---
testcase433:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        
        int f = g;
    }
}
---
testcase434:
class foo{}
class A {
    static int a = 3;
}
class B extends A {
    A b = new B();

    int foo(int a; float e){
        final float b = this.a;
    }
}
---
testcase435:
class foo{}
class A {
    static int a;
}
class B extends A {
    static A b = new B();

    int foo(int a; float e){
        final float b = B.b;   # assign a class to constant
    }
}
---
testcase436:
class foo{}
class A {
    static int a;
}
class B extends A {
    A b = new B();

    int foo(int a; float e){
       final float b = new B();
    }
}
---
testcase437:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();

    int foo(int a; float e){
        final float b = this.b.a;
    }
}
---
testcase438:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){                # check it later when para into a
        final float b = 30.5;
        A c = new A();
        B d = new B();
        final int f = a;
        final float g = e;
    }
}
---
testcase439:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; boolean e){
        float b = 30.5;
        A c = new A();
        C d = new B();
        int f = a;
        final float g = e;
    }
}
---
testcase440:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        final int f = 1100;
    }
}
---
testcase441:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        final boolean f = g;
    }
}
---
testcase442:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        final float f = a + b; 
    }
}
---
testcase443:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; float e){
        float b = 30.5;
        A c = new A();
        final float f = a + b; 
        int h = a * b + c - d;
    }
}
---
testcase444:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        A c = new A();
        final float f = a % e \ b; 
    }
}
---
testcase445:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        A c = new A();
        boolean x = a >= e;
        boolean z = a == e;
        boolean y = a != b; #error here
        final float f = a == b; 
    }
}
---
testcase446:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        A c = new A();
        boolean x = a >= e;
        boolean z = a == e;
        float y = - b + +a; 
        final float f = a == b; 
    }
}
---
testcase447:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        A c = new A();
        boolean x = a >= e;
        boolean z = a == e;
        float y = - b + +a; 
        return a;
    }
}
---
testcase448:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c;
        c:= 10;
    }
}
---
testcase449:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        c:= 10;
    }
}
---
testcase450:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        if a == 3 then
            return a;
        else 
            return c;
    }
}
---
testcase451:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        if a - 2 then
            return a;
        else 
            return b;
    }
}
---
testcase452:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        if (a==2) && (b >=3) then
            return a;
        else 
            return b;
    }
}
---
testcase453:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            if (a==2) && (b >=3) then
                return a;
            else 
                a := b + 1;
        }

    }
}
---
testcase454:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= b to 10 do {
            if (a==2) && (b >=3) then
                return a;
            else 
                a := b + 1;
        }

    }
}
---
testcase455:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for c:= b to 10 do {
            if (a==2) && (b >=3) then
                return a;
            else 
                a := b + 1;
        }

    }
}
---
testcase456:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int[11] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            int[10] x;
            if (a==2) && (b >=3) then
                return a;
            else 
                x := this.y;
        }

    }
}

---
testcase457:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            int[10] x;
            if (a==2) && (b >=3) then
                return a;
            else 
                x := this.y;
        }

    }
}
---
testcase458:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            int[10] x;
            if (a==2) && (b >=3) then
                return a;
            else 
                x := this.foo(a-1, e-1);
        }

    }
}
---
testcase459:
class foo{}
class A {
    int a;
}
class B extends A {
    A b = new B();
    int[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            int[10] x;
            if (a==2) && (b >=3) then
                return a;
            else 
                x[0] := this.foo(a-1, e-1);
        }

    }
}
---
testcase460:
class foo{}
class A {
    int a;
    int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    int[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            int[10] x;
            if (a==2) && (b >=3) then
                return a;
            else 
                x[0] := this.A(a-1, e-1);
        }

    }
}
---
testcase461:
class foo{
    void count(int a; float b){
        
    }
}
class A extends foo{
    int a;
    int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    int[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            int[10] x;
            if (a==2) && (b >=3) then
                return a;
            else 
                x[0] := this.count(a-1, e-1);
        }

    }
}
---
testcase462:
class foo{
    int count(int a; float b){
        
    }
}
class A extends foo{
    int a;
    int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    int[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:= 3 to 10 do {
            int[10] x;
            if (a==2) && (b >=3) then
                return a;
            else 
                x[0] := this.b.count(1,a);
        }

    }
}
---
testcase463:
class foo{
    int count(int a; float b){
        
    }
}
class A extends foo{
    int a;
    int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    int[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        if a == 3 then
            this.foo(a -1, c-2);
        else
            b.count(a +1, b +c);

    }
}
---
testcase464:
class foo{
    int count(int a; float b){
        
    }
}
class A extends foo{
    int a;
    int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        continue;
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                break;
            }
        }
    }
}
---
testcase465:
class foo{
    int count(int a; float b){
        
    }
}
class A extends foo{
    int a;
    int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                break;
            }
        }
        if b >= 3.0 then
             break;
        else
           continue;
    }
}
---
testcase466:
class foo{
    int count(int a; float b){
        
    }
}
class A extends foo{
    final int a = 4;
    int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                break;
            }
        }
    }
}
---
testcase467:
class foo{
    int count(int a; float b){
        if A.b then 
            return a;
        else
            return b;
    }
}
class A extends foo{
    final int a = 4;
    static int b;
    A (int a; int b){
        this.a := a;
        this.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                break;
            }
        }
    }
}
---
testcase468:
class foo{
    float count(int a; float b){
        return a * b - a +b;
    }
}
class A extends foo{
    int a = 4;
    static int b;
    A (int a; int b){
        this.a := a;
        A.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    int foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                if a - 2 > 4.0 then
                    return c / 3 \\4;
            }
        }
    }
}
---
testcase469:
class foo{
    float count(int a; float b){
        return a * b - a +b;
    }
}
class A extends foo{
    int a = 4;
    static int b;
    A (int a; int b){
        this.a := a;
        A.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                if a - 2 > 4.0 then
                    return c / (3 \ 4);
            }
        }
    }
}
---
testcase470:
class foo{
    float count(int a; float b){
        return a * b - a +b;
    }
}
class A extends foo{
    int a = 4;
    static int b;
    A (int a; int b){
        this.a := a;
        A.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                if a - 2 > 4.0 then
                    return c / 3 \ 4;
            }
        }
    }
}
---
testcase471:
class foo{
    float count(int a; float b){
        return a * b - a +b;
    }
}
class A extends foo{
    int a = 4;
    static int b;
    A (int a; int b){
        this.a := a;
        A.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                if a - 2 > 4.0 then{
                    int d;
                    c := d;
                }
            }
        }
    }
}
---
testcase472:
class foo{
    float count(int a; float b){
        return a * b - a +b;
    }
}
class A extends foo{
    int a = 4;
    static int b;
    A (int a; int b){
        this.a := a;
        A.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                int c;
                if a - 2 > 4.0 then{
                    int d;
                    c := {1, 2, 3.0};
                    d := {1.2, 2,3,4};
                }
            }
        }
    }
}
---
testcase473:
class foo{
    float count(int a; float b){
        return a * b - a +b;
    }
}
class A extends foo{
    int a = 4;
    static int b;
    A (int a; int b){
        this.a := a;
        A.b := b;
    }
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        for a:=3 to 10 do {
            if a %2 ==0 then{
                b:= a*2 +1;
                this.y[a]:= b;
            }
            else {
                int[4] c;
                if a - 2 > 4.0 then{
                    int d;
                    c := {1,2,3};
                    d := {1.2, 2,3,4};
                }
            }
        }
    }
}
---
testcase474:
class foo{

}
class A extends foo{

}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            float[3] c;
            if a - 2 > 4.0 then{
                int d;
                c := {1,2,3};
                d := {1.2, 2,3,4};
            }
        }
        return c;
        
    }
}
---
testcase475:
class foo{

}
class A extends foo{

}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            int[3] c;
            if a - 2 > 4.0 then{
                int d;
                c := {1,2,3,4};
                d := {1.2, 2,3,4};
            }
        }
        return c;
        
    }
}
---
testcase476: 
class foo{

}
class A extends foo{

}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            int[3] c;
            if a - 2 > 4.0 then{
                int d;
                c := {1,2,3}; 
                c[3] := 5;
                c[2] := 5.0;
                d := {1.2, 2,3,4};
            }
        }
        return c;
    }
}
---
testcase477:
class foo{

}
class A extends foo{

}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            int[3] c;
            if a - 2 > 4.0 then{
                int d;
                c := {1,2,3}; 
                c[3] := 5;
                
                d := {1.2, 2.2, 3.4, 4.6};
                c := d;
            }
        }
        return c;
    }
}
---
testcase478:
class foo{

}
class A extends foo{

}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            int[3] c;
            if a - 2 > 4.0 then{
                int[3] d;
                c := {1,2,3}; 
                c[3] := 5;
                
                d := {5,3,5};
                c := d;
            }
        }
        return c;
    }
}
---
testcase479:
class foo{

}
class A extends foo{
    static void writeIntLn(int arg){}
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            A.writeIntLn(3);
            
        }
        return c;
    }
}
---
testcase480:
class foo{
}
class A extends foo{
    static void writeIntLn(int arg){}
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            io.writeIntLn(3);
            
        }
        return c;
    }
}
---
testcase481:
class foo{
}
class A extends foo{
    static void writeIntLn(int arg){}
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            int f = io.readInt();
            if f >3 then{
                io.writeInt(f);
            }
            else
                return io.readFloat();
            
        }
        return c;
    }
}
---
testcase482:
class foo{
}
class A extends foo{
    static void writeIntLn(int arg){}
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            int f = io.readInt();
            if f >3 then{
                io.writeInt(b); #error here Type Mismatch In Statement: Call(Id(io),Id(writeInt),[Id(b)])
            }
            else
                return io.readFloat();
            
        }
        return c;
    }
}
---
testcase483:
class foo{
}
class A extends foo{
    static void writeIntLn(int arg){}
}
class B extends A {
    A b = new B();
    float[10] y;
    float foo(int a; int e){
        float b = 30.5;
        final int c = 10;
        
        if a %2 ==0 then{
            b:= a*2 +1;
            this.y[a]:= b;
        }
        else {
            int f = io.readInt();
            if f >3 then{
                io.writeInt(f); 
            }
            else
                return io.readStr(); #error here
            
        }
        return c;
    }
}
---
testcase484:
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
testcase485:
class Example1 {
    int factorial(int n){
        if n == 0 then return true; else return n * this.factorial(n - 1);
    }
    void main(){
        int x;
        x := io.readInt();
        io.writeIntLn(this.factorial(x));
    }
}
---
testcase486:
class Example1 {
    int factorial(int n){
        if n == 0 then return 1; else return n / this.factorial(n - 1);
    }
    void main(){
        int x;
        x := io.readInt();
        io.writeIntLn(this.factorial(x));
    }
}
---
testcase487:
class Example1 {
    int factorial(int n){
        Example1 e = new Example1();
        if n == 0 then return 1; else return e * this.factorial(n - 1);
    }
    void main(){
        int x;
        x := io.readInt();
        io.writeIntLn(this.factorial(x));
    }
}
---
testcase488:
class SuperComplexTest {
    float customPower(float base; int exponent) {
        if (exponent == 0) then {
            return 1;
        } else if (exponent % 2 == 0) then {
            float temp = this.customPower(base, exponent / 2);
            return temp * temp;
        } else {
            float temp = this.customPower(base, (exponent - 1) / 2);
            return base * temp * temp;
        }
    }

    static int fibonacci(int n) {
        if (n <= 1) then {
            return n;
        } else {
            return this.fibonacci(n - 1) + this.fibonacci(n - 2);
        }
    }

    static void main() {
        float sum = 0;
        int finalValue = 0;
        for i := 1 to 10 do {
            int factorial = 1;
            int fibonacciSum = 0;

            for j := 1 to i do {
                factorial := factorial * j;
                fibonacciSum := fibonacciSum + this.fibonacci(j);
            }
            {
            float customPowerResult = this.customPower(factorial, i);
            sum := sum + customPowerResult * fibonacciSum;
            }
        }

        

        for k := 1 to 5 do {
            if (k % 2 == 0)then {
                finalValue := finalValue + this.customPower(sum, k) + k;
            } else {
                finalValue := finalValue - this.customPower(sum, k) - k;
            }
        }

        io.writeStrLn("Final Value: " ^ finalValue);
    }
}
---
testcase489:
class SuperComplexTest {
    float customPower(float base; int exponent) {
        if (exponent == 0) then {
            return 1;
        } else if (exponent % 2 == 0) then {
            float temp = this.customPower(base, exponent \ 2);
            return temp * temp;
        } else {
            float temp = this.customPower(base, (exponent - 1) \ 2);
            return base * temp * temp;
        }
    }

    static int fibonacci(int n) {
        if (n <= 1) then {
            return n;
        } else {
            return this.fibonacci(n - 1) + this.fibonacci(n - 2);
        }
    }

    static void main() {
        float sum = 0;
        int finalValue = 0;
        for i := 1 to 10 do {
            int factorial = 1;
            int fibonacciSum = 0;

            for j := 1 to i do {
                factorial := factorial * j;
                fibonacciSum := fibonacciSum + this.fibonacci(j);
            }
            {
            float customPowerResult = this.customPower(factorial, i);
            sum := sum + customPowerResult * fibonacciSum;
            }
        }

        

        for k := 1 to 5 do {
            if (k % 2 == 0)then {
                finalValue := finalValue + this.customPower(sum, k) + k;
            } else {
                finalValue := finalValue - this.customPower(sum, k) - k;
            }
        }

        io.writeStrLn("Final Value: " ^ finalValue);
    }
}
---
testcase490:
class SuperComplexTest {
    float customPower(float base; int exponent) {
        if (exponent == 0) then {
            return 1;
        } else if (exponent % 2 == 0) then {
            float temp = this.customPower(base, exponent \ 2);
            return temp * temp;
        } else {
            float temp = this.customPower(base, (exponent - 1) \ 2);
            return base * temp * temp;
        }
    }

    static int fibonacci(int n) {
        if (n <= 1) then {
            return n;
        } else {
            return SuperComplexTest.fibonacci(n - 1) + SuperComplexTest.fibonacci(n - 2);
        }
    }

    static void main() {
        float sum = 0;
        int finalValue = 0;
        for i := 1 to 10 do {
            int factorial = 1;
            int fibonacciSum = 0;

            for j := 1 to i do {
                factorial := factorial * j;
                fibonacciSum := fibonacciSum + this.fibonacci(j);
            }
            {
            float customPowerResult = this.customPower(factorial, i);
            sum := sum + customPowerResult * fibonacciSum;
            }
        }

        

        for k := 1 to 5 do {
            if (k % 2 == 0)then {
                finalValue := finalValue + this.customPower(sum, k) + k;
            } else {
                finalValue := finalValue - this.customPower(sum, k) - k;
            }
        }

        io.writeStrLn("Final Value: " ^ finalValue);
    }
}
---
testcase491:
class SuperComplexTest {
    float customPower(float base; int exponent) {
        if (exponent == 0) then {
            return 1;
        } else if (exponent % 2 == 0) then {
            float temp = this.customPower(base, exponent \ 2);
            return temp * temp;
        } else {
            float temp = this.customPower(base, (exponent - 1) \ 2);
            return base * temp * temp;
        }
    }

    static int fibonacci(int n) {
        if (n <= 1) then {
            return n;
        } else {
            return SuperComplexTest.fibonacci(n - 1) + SuperComplexTest.fibonacci(n - 2);
        }
    }

    static void main() {
        float sum = 0;
        int finalValue = 0;
        int i, j , k;
        for i := 1 to 10 do {
            int factorial = 1;
            int fibonacciSum = 0;
            int j;
            for j := 1 to i do {
                factorial := factorial * j;
                fibonacciSum := fibonacciSum + SuperComplexTest.fibonacci(j);
            }
            {
            float customPowerResult = this.customPower(factorial, i);
            sum := sum + customPowerResult * fibonacciSum;
            }
        }
        
        for k := 1 to 5 do {
            if (k % 2 == 0)then {
                finalValue := finalValue + this.customPower(sum, k) + k;
            } else {
                finalValue := finalValue - this.customPower(sum, k) - k;
            }
        }

        io.writeStrLn("Final Value: " ^ finalValue);
    }
}
---
testcase492:
class SuperComplexTest {
    float customPower(float base; int exponent) {
        if (exponent == 0) then {
            return 1;
        } else if (exponent % 2 == 0) then {
            float temp = this.customPower(base, exponent \ 2);
            return temp * temp;
        } else {
            float temp = this.customPower(base, (exponent - 1) \ 2);
            return base * temp * temp;
        }
    }

    static int fibonacci(int n) {
        if (n <= 1) then {
            return n;
        } else {
            return SuperComplexTest.fibonacci(n - 1) + SuperComplexTest.fibonacci(n - 2);
        }
    }

    static void main() {
        float sum = 0;
        int finalValue = 0;
        int i, j , k;
        for i := 1 to 10 do {
            int factorial = 1;
            int fibonacciSum = 0;
            int j;
            for j := 1 to i do {
                factorial := factorial * j;
                fibonacciSum := fibonacciSum + SuperComplexTest.fibonacci(j);
            }
            {
            float customPowerResult = this.customPower(factorial, i);
            sum := sum + customPowerResult * fibonacciSum;
            }
        }
        
        for k := 1 to 5 do {
            float finalValue;
            if (k % 2 == 0)then {
                finalValue := finalValue + this.customPower(sum, k) + k;
            } else {
                finalValue := finalValue - this.customPower(sum, k) - k;
            }
        }

        io.writeStrLn("Final Value: " ^ finalValue);
    }
}
---
testcase493:
class SuperComplexTest {
    float customPower(float base; int exponent) {
        if (exponent == 0) then {
            return 1;
        } else if (exponent % 2 == 0) then {
            float temp = this.customPower(base, exponent \ 2);
            return temp * temp;
        } else {
            float temp = this.customPower(base, (exponent - 1) \ 2);
            return base * temp * temp;
        }
    }

    static int fibonacci(int n) {
        if (n <= 1) then {
            return n;
        } else {
            return SuperComplexTest.fibonacci(n - 1) + SuperComplexTest.fibonacci(n - 2);
        }
    }

    static void main() {
        float sum = 0;
        int finalValue = 0;
        int i, j , k;
        float finalValue;
        for i := 1 to 10 do {
            int factorial = 1;
            int fibonacciSum = 0;
            int j;
            for j := 1 to i do {
                factorial := factorial * j;
                fibonacciSum := fibonacciSum + SuperComplexTest.fibonacci(j);
            }
            {
            float customPowerResult = this.customPower(factorial, i);
            sum := sum + customPowerResult * fibonacciSum;
            }
        }
        
        for k := 1 to 5 do {
            if (k % 2 == 0)then {
                finalValue := finalValue + this.customPower(sum, k) + k;
            } else {
                finalValue := finalValue - this.customPower(sum, k) - k;
            }
        }

        io.writeStrLn("Final Value: ");
        io.writeIntLn(finalValue);
    }
}
---
testcase494:
class MergeSort {
    void merge(int left,middle; int right) {
        int n1 = middle - left + 1;
        int n2 = right - middle;
        int[0] leftArray;
        int[0] rightArray;
        int i,j,k;
        for i := 0 to n1 - 1 do
            leftArray[i] := arr[left + i];

        for j := 0 to n2 - 1 do
            rightArray[j] := arr[middle + 1 + j];

         i := 0;
         j := 0;
         k := left;

        for k := left to right do{
            if i < n1 && ((j >= n2) || (leftArray[i] <= rightArray[j])) then{
                arr[k] := leftArray[i];
                i := i + 1;
            }
            else{
                arr[k] := rightArray[j];
                j := j + 1;
            }
        }
    }

    void mergeSort(int left; int right) {
        if left < right then {
            int middle = left + (right - left) / 2;
            this.mergeSort(arr, left, middle);
            this.mergeSort(arr, middle + 1, right);
            this.merge(arr, left, middle, right);
        }
    }
}
---
testcase495:
class MergeSort {
    void merge(int left,middle; int right; int[10] arr) {
        int n1 = middle - left + 1;
        int n2 = right - middle;
        int[0] leftArray;
        int[0] rightArray;
        int i,j,k;
        for i := 0 to n1 - 1 do
            leftArray[i] := arr[left + i];

        for j := 0 to n2 - 1 do
            rightArray[j] := arr[middle + 1 + j];

         i := 0;
         j := 0;
         k := left;

        for k := left to right do{
            if i < n1 && ((j >= n2) || (leftArray[i] <= rightArray[j])) then{
                arr[k] := leftArray[i];
                i := i + 1;
            }
            else{
                arr[k] := rightArray[j];
                j := j + 1;
            }
        }
    }

    void mergeSort(int left; int right) {
        if left < right then {
            int middle = left + (right - left) / 2;
            this.mergeSort(arr, left, middle);
            this.mergeSort(arr, middle + 1, right);
            this.merge(arr, left, middle, right);
        }
    }
}
---
testcase496:
class MergeSort {
    void merge(int left,middle; int right; int[10] arr) {
        int n1 = middle - left + 1;
        int n2 = right - middle;
        int[0] leftArray;
        int[0] rightArray;
        int i,j,k;
        for i := 0 to n1 - 1 do
            leftArray[i] := arr[left + i];

        for j := 0 to n2 - 1 do
            rightArray[j] := arr[middle + 1 + j];

         i := 0;
         j := 0;
         k := left;

        for k := left to right do{
            if (i < n1) && ((j >= n2) || (leftArray[i] <= rightArray[j])) then{
                arr[k] := leftArray[i];
                i := i + 1;
            }
            else{
                arr[k] := rightArray[j];
                j := j + 1;
            }
        }
    }

    void mergeSort(int left; int right) {
        if left < right then {
            int middle = left + (right - left) \ 2;
            this.mergeSort(arr, left, middle);
            this.mergeSort(arr, middle + 1, right);
            this.merge(arr, left, middle, right);
        }
    }
}
---
testcase497:
class MergeSort {
    void merge(int left,middle; int right; int[10] arr) {
        int n1 = middle - left + 1;
        int n2 = right - middle;
        int[0] leftArray;
        int[0] rightArray;
        int i,j,k;
        for i := 0 to n1 - 1 do
            leftArray[i] := arr[left + i];

        for j := 0 to n2 - 1 do
            rightArray[j] := arr[middle + 1 + j];

         i := 0;
         j := 0;
         k := left;

        for k := left to right do{
            if (i < n1) && ((j >= n2) || (leftArray[i] <= rightArray[j])) then{
                arr[k] := leftArray[i];
                i := i + 1;
            }
            else{
                arr[k] := rightArray[j];
                j := j + 1;
            }
        }
    }

    void mergeSort( int[10] arr; int left; int right) {
        if left < right then {
            int middle = left + (right - left) \ 2;
            this.mergeSort(arr, left, middle);
            this.mergeSort(arr, middle + 1, right);
            this.merge(arr, left, middle, right);
        }
    }
}
---
testcase498:
class MergeSort {
    void merge(int left,middle; int right; int[10] arr) {
        int n1 = middle - left + 1;
        int n2 = right - middle;
        int[0] leftArray;
        int[0] rightArray;
        int i,j,k;
        for i := 0 to n1 - 1 do
            leftArray[i] := arr[left + i];

        for j := 0 to n2 - 1 do
            rightArray[j] := arr[middle + 1 + j];

         i := 0;
         j := 0;
         k := left;

        for k := left to right do{
            if (i < n1) && ((j >= n2) || (leftArray[i] <= rightArray[j])) then{
                arr[k] := leftArray[i];
                i := i + 1;
            }
            else{
                arr[k] := rightArray[j];
                j := j + 1;
            }
        }
    }

    void mergeSort( int[10] arr; int left; int right) {
        if left < right then {
            int middle = left + (right - left) \ 2;
            this.mergeSort(arr, left, middle);
            this.mergeSort(arr, middle + 1, right);
            this.merge( left, middle, right, arr);
        }
    }
}
---
testcase499:
class Student {
    string name;
    int age;
    float gpa;

    Student(string name; int age; float gpa) {
        this.name := name;
        this.age := age;
        this.gpa := gpa;
    }

    void display() {
        io.writeStrLn("Name:" ^ this.name);
        io.writeStrLn("Age:" );
        io.writeIntLn(this.age);
        io.writeStrLn("GPA:");
        io.writeFloat(this.gpa);
    }

    string getGrade() {
        if (this.gpa >= 3.5) then return "A";
        else {
            if (this.gpa >= 3.0) then return "B";
            else {
                if (this.gpa >= 2.0) then return "C";
                else {
                    if (this.gpa >= 1.0) then return "D";
                    else return "F";
                }
                return this.name;
            }
        }
    }
}

class Test {
    void main() {
        Student s1 = new Student("Alice", 20, 3.8);
        Student s2 = new Student("Bob", 19, 2.9);

        s1.display();
        io.writeStrLn("Grade:" ^ s1.getGrade());

        s2.display();
        io.writeStrLn("Grade:" ^ s2.getGrade("a"));
    }
}
---
'''
e = '''
testcase400:[]
---
testcase401: Redeclared Attribute: b
--- 
testcase402: Redeclared Method: a
---
testcase403: Redeclared Parameter: a
---
testcase404: Undeclared Class: foo
---
testcase405: Redeclared Parameter: a
---
testcase406: Redeclared Class: foo
---
testcase407: Redeclared Variable: a
---
testcase408: Redeclared Constant: a
---
testcase409: Undeclared Method: foo
---
testcase410: Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(b),IntType,Id(a)))
---
testcase411: Undeclared Identifier: a
---
testcase412:[]
---
testcase413: Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,FloatLit(21.5))
---
testcase414: Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(b),BoolType,FloatLit(21.5)))
---
testcase415: Undeclared Class: A 
---
testcase416:[]
---
testcase417: Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(A)),NewExpr(Id(B),[])))
---          
testcase418: Type Mismatch In Expression: FieldAccess(Self(),Id(a))
---
testcase419: []
---
testcase420: []
---
testcase421: Redeclared Variable: a
---
testcase422: Type Mismatch In Statement: VarDecl(Id(d),BoolType,Id(a))
---
testcase423: Type Mismatch In Statement: VarDecl(Id(d),BoolType,Id(a))
---
testcase424: Illegal Member Access: FieldAccess(Id(A),Id(a))
---
testcase425: Illegal Member Access: FieldAccess(Self(),Id(a))
---
testcase426: Illegal Member Access: FieldAccess(Self(),Id(a))
---
testcase427: Type Mismatch In Statement: VarDecl(Id(b),FloatType,FieldAccess(Id(B),Id(b))) 
---
testcase428: Type Mismatch In Statement: VarDecl(Id(b),FloatType,NewExpr(Id(B),[]))
---
testcase429: []
---
testcase430: []
---
testcase431: Undeclared Class: C 
---
testcase432: Undeclared Attribute: g
---
testcase433: Undeclared Identifier: g
---
testcase434: Illegal Member Access: FieldAccess(Self(),Id(a))
---
testcase435: Type Mismatch In Constant Declaration: ConstDecl(Id(b),FloatType,FieldAccess(Id(B),Id(b))) 
---
testcase436: Type Mismatch In Constant Declaration: ConstDecl(Id(b),FloatType,NewExpr(Id(B),[]))
---
testcase437: Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(b)),Id(a))
---
testcase438: []
---
testcase439: Undeclared Class: C 
---
testcase440: []
---
testcase441: Undeclared Identifier: g
---
testcase442: []
---
testcase443: Type Mismatch In Expression: BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c))
---
testcase444: Type Mismatch In Expression: BinaryOp(\,BinaryOp(%,Id(a),Id(e)),Id(b))
---
testcase445: Type Mismatch In Expression: BinaryOp(!=,Id(a),Id(b))
---
testcase446: Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))
---
testcase447: []
---
testcase448: Illegal Constant Expression: None
---
testcase449: Cannot Assign To Constant: AssignStmt(Id(c),IntLit(10)) 
---
testcase450: []
---
testcase451: Type Mismatch In Statement: If(BinaryOp(-,Id(a),IntLit(2)),Return(Id(a)),Return(Id(b)))
---
testcase452: Type Mismatch In Statement: Return(Id(b))
---
testcase453: Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,Id(b),IntLit(1)))
---
testcase454: Type Mismatch In Statement: For(Id(a),Id(b),IntLit(10),True,Block([],[If(BinaryOp(&&,BinaryOp(==,Id(a),IntLit(2)),BinaryOp(>=,Id(b),IntLit(3))),Return(Id(a)),AssignStmt(Id(a),BinaryOp(+,Id(b),IntLit(1))))])])
---
testcase455: Cannot Assign To Constant: AssignStmt(Id(c),Id(b))
---
testcase456: Type Mismatch In Statement: AssignStmt(Id(x),FieldAccess(Self(),Id(y)))
---
testcase457: []
---
testcase458: Type Mismatch In Statement: AssignStmt(Id(x),CallExpr(Self(),Id(foo),[BinaryOp(-,Id(a),IntLit(1)),BinaryOp(-,Id(e),IntLit(1))]))
---
testcase459: []
---
testcase460: Undeclared Method: A
---
testcase461: Type Mismatch In Expression: CallExpr(Self(),Id(count),[BinaryOp(-,Id(a),IntLit(1)),BinaryOp(-,Id(e),IntLit(1))])
---
testcase462: []
---
testcase463: Type Mismatch In Statement: Call(Self(),Id(foo),[BinaryOp(-,Id(a),IntLit(1)),BinaryOp(-,Id(c),IntLit(2))])
---
testcase464: Continue Not In Loop
---
testcase465: Break Not In Loop
---
testcase466: Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),Id(a))
---
testcase467: Type Mismatch In Statement: If(FieldAccess(Id(A),Id(b)),Return(Id(a)),Return(Id(b)))
---
testcase468: Type Mismatch In Expression: BinaryOp(\,BinaryOp(/,Id(c),IntLit(3)),IntLit(4))
---
testcase469: []
---
testcase470: Type Mismatch In Expression: BinaryOp(\,BinaryOp(/,Id(c),IntLit(3)),IntLit(4))
---
testcase471: Cannot Assign To Constant: AssignStmt(Id(c),Id(d))
---
testcase472: Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3.0)]
---
testcase473: Type Mismatch In Statement: AssignStmt(Id(c),[IntLit(1),IntLit(2),IntLit(3)])
---
testcase474: Illegal Array Literal: [FloatLit(1.2),IntLit(2),IntLit(3),IntLit(4)]
---
testcase475: Type Mismatch In Statement: AssignStmt(Id(c),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])
---
testcase476: Type Mismatch In Statement: AssignStmt(ArrayCell(Id(c),IntLit(2)),FloatLit(5.0))
---
testcase477: Type Mismatch In Statement: AssignStmt(Id(d),[FloatLit(1.2),FloatLit(2.2),FloatLit(3.4),FloatLit(4.6)])
---
testcase478: Type Mismatch In Statement: Return(Id(c))
---
testcase479: []
---
testcase480: []
---
testcase481: []
---
testcase482: Type Mismatch In Statement: Call(Id(io),Id(writeInt),[Id(b)])
---
testcase483: Type Mismatch In Statement: Return(CallExpr(Id(io),Id(readStr),[]))
---
testcase484: []
---
testcase485: Type Mismatch In Statement: Return(BooleanLit(True))
---
testcase486: Type Mismatch In Statement: Return(BinaryOp(/,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))])))
---
testcase487: Type Mismatch In Expression: BinaryOp(*,Id(e),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]))
---
testcase488: Type Mismatch In Expression: CallExpr(Self(),Id(customPower),[Id(base),BinaryOp(/,Id(exponent),IntLit(2))])
---
testcase489: Illegal Member Access: CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(n),IntLit(1))])
---
testcase490: Undeclared Identifier: i
---
testcase491: Type Mismatch In Statement: AssignStmt(Id(finalValue),BinaryOp(+,BinaryOp(+,Id(finalValue),CallExpr(Self(),Id(customPower),[Id(sum),Id(k)])),Id(k)))
---
testcase492: Type Mismatch In Expression: BinaryOp(^,StringLit(Final Value: ),Id(finalValue))
---
testcase493: Redeclared Variable: finalValue
---
testcase494: Undeclared Identifier: arr
---
testcase495: Type Mismatch In Expression: BinaryOp(&&,Id(n1),BinaryOp(||,BinaryOp(>=,Id(j),Id(n2)),BinaryOp(<=,ArrayCell(Id(leftArray),Id(i)),ArrayCell(Id(rightArray),Id(j)))))
---
testcase496: Undeclared Identifier: arr
---
testcase497: Type Mismatch In Statement: Call(Self(),Id(merge),[Id(arr),Id(left),Id(middle),Id(right)])
---
testcase498: []
---
testcase499: Type Mismatch In Expression: CallExpr(Id(s2),Id(getGrade),[StringLit(a)])
---

'''


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
#         input = '''
# class Student {
#     string name;
#     int foo(int a, b){
#         int c,d;
#         if c >1 then {
#             int e;
#             float f;
#             int g;
#             int e = 1;
#         }
#     }
# }
#         '''
            
#         expect = "Redeclared Variable: e"
#         self.assertTrue(TestChecker.test(input,expect,400))
        
        
        
#     def test_diff_numofparam_stmt(self):
#         """More complex program"""
#         input = Program([ClassDecl(Id("Ex"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),FieldAccess(Id("Ex"),Id("a"))))])])
#         expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
#         self.assertTrue(TestChecker.test(input,expect,401))
    
#     def test_diff_numofparam_expr(self):
#         """More complex program"""
#         input = Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(2),FloatLiteral(1.2),NullLiteral()])))])])
#         expect = "Illegal Array Literal: [IntLit(2),FloatLit(1.2),NullLiteral()]"
#         self.assertTrue(TestChecker.test(input,expect,402))

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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
