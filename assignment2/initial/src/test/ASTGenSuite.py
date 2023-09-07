import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def generate_test_method(testNumber,input,exp):
        
        def test_simple_program(self):
            """Simple program: class main {} """
            self.assertTrue(TestAST.test(input,exp,testNumber))
        return test_simple_program

import re


# with open('C:/Users/OnDoing/PrincipleProgrammingLangueHCMUT/assignment2/testcasehandmade/input.txt') as f:
#     f = f.read()
# with open('C:/Users/OnDoing/PrincipleProgrammingLangueHCMUT/assignment2/testcasehandmade/exp.txt') as e:
#     e = e.read()


f = """
testcase300:
class a{
    float b, c;
}
---
testcase301:
class a{
    float b = 3, d = 3, c = 3+4; 
}
---
testcase302:
class a{
    static final boolean c = 2;
}
---
testcase303:
class a{
    final static int c;
    
}
---
testcase304:
class a{
    static float a;
}
---
testcase305:
class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
}
---
testcase306:
class Rectangle extends Shape {
    float getArea(){
        return this.length*this.width;
    }
    float getLength(){
        return this.length+this.width;
    }
}
---
testcase307:
class Shape {
    float length,width;
    static int getNumOfShape() {
        return numOfShape;
    }
}
---
testcase308:
class Rectangle{
    float getArea(float a,b ; int c){
        return this.length*this.width;
    }
}
---
testcase309:
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length, width;

    static int getNumOfShape() {
        return numOfShape;
    }
}

class Rectangle extends Shape {
    float getArea() {
        return this.length * this.width;
    }
}
---
testcase310:
class Test {
    int a;
    float b;
    boolean c;
}
---
testcase311:
class Circle extends Shape{
    float getArea() {
        return 3.14 * this.radius * this.radius;
    }
}
---
testcase312:
class Test{void printMessage() {io.writeStrLn("Hello, World!");}}
---
testcase313:
class Math{
    static int max(int a; int b) {
        if (a > b) then return a;
        else return b;
    }
}
---
testcase314:
class Circle extends Shape {
    float getArea() {
        return 3.14 * this.radius * this.radius;
    }
}
class Square extends Shape {
    float getArea() {
        return this.length * this.length;
    }
}
class Test {
    void main() {
        Shape c, s;
        float area1, area2;
        
        c := new Circle();
        s := new Square();
        area1 := c.getArea();
        area2 := s.getArea();
        io.writeStrLn("Area of Circle: " ^ area1);
        io.writeStrLn("Area of Square: " ^ area2);
    }
}
---
testcase315:
class Shape {
    float length, width;
    Shape(float l, w) {
        this.length := l;
        this.width := w;
    }
}
class Circle extends Shape {
    float getArea() {
        return 3.14 * this.radius * this.radius;
    }
}
class Test {
    void main() {
        Circle c = new Circle(5.0, 5.0);
        float area = c.getArea();
        io.writeStrLn("Area of Circle: " ^ area);
    }
}
---
testcase316:
class Animal {
    string name;
    int age;

    Animal(string name; int age) {
        this.name := name;
        this.age := age;
    }

    void makeSound() { }
}

class Dog extends Animal {
    string breed;

    Dog(string name; int age; string breed) {
        this.Animal(name, age);
        this.breed := breed;
    }

    void makeSound() {
        io.writeStrLn("Woof! Woof!");
    }

    void fetch() {
        io.writeStrLn("Fetching the ball!");
    }
}

class Cat extends Animal {
    string furColor;

    Cat(string name; int age; string furColor) {
        this.Animal(name, age);
        this.furColor := furColor;
    }

    void makeSound() {
        io.writeStrLn("Meow!");
    }

    void climbTree() {
        io.writeStrLn("Climbing the tree!");
    }
}

class Test {
    void main() {
        Dog dog = new Dog("Buddy", 3, "Labrador");
        Cat cat = new Cat("Whiskers", 2, "Gray");
        Animal animal1 = dog;
        Animal animal2 = cat;
        dog.makeSound();
        cat.makeSound();

        io.writeStrLn("Dog's breed: " ^ dog.breed);
        io.writeStrLn("Cat's fur color: " ^ cat.furColor);

        animal1.makeSound();
        animal2.makeSound();

        animal1.fetch();
        animal2.climbTree();
    }
}
---
testcase317:
class Point {
    int x, y;

    Point(int x; int y) {
        this.x := x;
        this.y := y;
    }

    void display() {
        io.writeStrLn("x: " ^ this.x ^ ", y: " ^ this.y);
    }

    static Point add(Point p1, p2) {
        return new Point(p1.x + p2.x, p1.y + p2.y);
    }
}

class Test {
    void main() {
        Point p1 = new Point(3, 5);
        Point p2 = new Point(-2, 7);
        Point sum = Point.add(p1, p2);

        p1.display();
        p2.display();
        sum.display();
    }
}
---
testcase318:
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
        io.writeStrLn("Age:" ^ this.age);
        io.writeStrLn("GPA:" ^ this.gpa);
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
        io.writeStrLn("Grade:" ^ s2.getGrade());
    }
}
---
testcase319:
class Math {
    static int factorial(int n) {
        if (n == 0) then {
            return 1;
        } else {
            return n * this.factorial(n - 1);
        }
    }

    static int fibonacci(int n) {
        if (n <= 1) then {
            return n;
        } else {
            return this.fibonacci(n - 1) + this.fibonacci(n - 2);
        }
    }
}

class Test {
    void main() {
        int num1 = 5;
        int num2 = 6;

        int factNum1 = Math.factorial(num1);
        int factNum2 = Math.factorial(num2);

        int fibNum1 = Math.fibonacci(num1);
        int fibNum2 = Math.fibonacci(num2);

        io.writeStrLn("Factorial_of" ^ num1 ^ ":" ^ factNum1);
        io.writeStrLn("Factorial_of" ^ num2 ^ ":" ^ factNum2);
        io.writeStrLn("Fibonacci_of" ^ num1 ^ ":" ^ fibNum1);
        io.writeStrLn("Fibonacci_of" ^ num2 ^ ":" ^ fibNum2);
    }
}
---
testcase320:
class Bank {
    float interestRate;

    Bank(float rate) {
        this.interestRate := rate;
    }

    float calculateInterest(float principal) {
        return principal * this.interestRate;
    }
}

class SavingsAccount extends Bank {
    SavingsAccount(float rate) {
        this.Bank(rate);
    }

    float calculateInterestReal(float principal) {
        return this.calculateInterest(principal) + 100;
    }
}

class FixedDeposit extends Bank {
    FixedDeposit(float rate) {
        this.Bank(rate);
    }

    float calculateInterestReal(float principal; int years) {
        return this.calculateInterest(principal) * years;
    }
}

class Test {
    void main() {
        Bank bank1, bank2;
        float principal = 1000.0;
        float interest1, interest2;


        bank1 := new SavingsAccount(0.05);
        bank2 := new FixedDeposit(0.08);


        interest1 := bank1.calculateInterest(principal);
        interest2 := bank2.calculateInterest(principal, 5);

        io.writeStrLn("Interest_from_Savings_Account:" ^ interest1);
        io.writeStrLn("Interest_from_Fixed Deposit:" ^ interest2);
    }
}
---
testcase321:
class Test {
    void main() {
        int a = 5, b = 10;
        int c = 15;
        boolean result = a + b * c >= c - b / a && !(a > b);
        io.writeStrLn("Result: " ^ result);
    }
}
---
testcase322:
class Test {
    static void main() {
        boolean p = true;
        boolean q = false;
        boolean result = p && q || !p;
        io.writeStrLn("Result:" ^ result);
    }
}
---
testcase323:
class Test {
    static void main() {
        int a = 5;
        int b = 10, c = 15;

        boolean result1 = (a + b) * c > a + b * c;
        boolean result2 = (a >= b) && (c < a) || (b <= c);
        boolean result3 = !((a == b) || c != b) && !(c > a && (b < c));

        io.writeStrLn("Result 1: " ^ result1);
        io.writeStrLn("Result 2: " ^ result2);
        io.writeStrLn("Result 3: " ^ result3);
    }
}
---
testcase324:
class Person {
    string name;
    int age;
    
    Person(string n; int a) {
        this.name := n;
        this.age := a;
    }
    
    void display() {
        io.writeStrLn("Name:" ^ this.name);
        io.writeStrLn("Age:" ^ this.age);
    }
}
---
testcase325:
class Test {
    static void main() {
        Person[3] persons;
        int totalAge = 0;
        persons[0] := new Person("Alice", 25);
        persons[1] := new Person("Bob", 30);
        persons[2] := new Person("Charlie", 22);
        io.writeStrLn("Total Age:" ^ totalAge);
    }
}
---
testcase326:
class Library {
    Book[5] books;
    
    Library(Book[5] b) {
        books := b;
    }
    
    void displayBooks() {
        io.writeStrLn("Library_Catalog:");
        for i := 0 to books.length do {
            (books[i]).displayInfo();
        }
    }
}

class Test {
    void main() {
        Book[3] bookList;
        Library myLibrary = new Library(bookList);
        bookList[0] := new Book("HarryPotter", "J.K.Rowling");
        bookList[1] := new Book("TheHobbit", "J.R.R.Tolkien");
    }
}
---
testcase327:
class array {
    void test() {
        x.b[2] := x.m()[3];
    }
}
---
testcase328:
class array {
    void test() {
        a[3+x.foo(2)] := a[b[2]] +3;
    }
}
---
testcase329:
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    static int getNumOfShape() {
        return numOfShape;
    }
}
---
testcase330:
class test {
    void main(){
        Shape s;
        s := new Rectangle(3,4);
        s := new Triangle(3,4);
    }
}
---
testcase331:
class test {
    void main(){
        Shape s = new Shape(5, 10);
    }
}
---
testcase332:
class test {
    void main(){
        this.aPI := 3.14;
        value := x.foo(5);
        l[3] := value * 2;
    }
}
---
testcase333:
class test {
    void main(){
        float r,s;
        int[5] a,b;
        r:=2.0;
        s:=r*r*this.myPI;
        a[0]:= s;
    }
}
---
testcase334:
class testForLoop {
    void main(){
        for i := 1 to 100 do {
            io.writeIntLn(i);
            Intarray[i] := i + 1;
        }
        for x := 5 downto 2 do
            io.writeIntLn(x);
    }
}
---
testcase335:
class testBrS {
    void main(){
        break;
    }
}
---
testcase336:
class testConS {
    void main(){
        continue;
    }
}
---
testcase337:
class fac {
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
testcase338:
class decl {
	int a, b, c;
	float x, y;
	string z = "abc";
	static boolean d = true;
}
---
testcase339:
class test {
    int a;
    float b;
    string z;
    float nml () {
        for i:= a to b do this.hahaha();
            for i := 4 downto -5 do h := 6;
        return 1;
    }
}
---
testcase340:
class testPrecedence {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 && -7)*(1+2+3)-(4+5*6/abc && (123))] := a[(((-5)))];
	}
}
---
testcase341:
class testPrecedence {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 || 7)*(1+2+3)-(4+5*6/abc && !(123))] := a[(((-5)))];
	}
}
---
testcase342:
class testFor {
	int foo() {
		for i := 1 to 10+5-4*e+x do break;
	}
}
---
testcase343:
class String1 {
	string a = "chacachien";
	string getString(){
		return this.a;
	}
}
class String2 {
	string b = "NguyenPhat";
	string getString(){
		return this.b;
	}
}
class Example {
	void main(){
		String1 str1;
		String2 str2;
		string result;
		result := str1.getString ^ str2.getString;
	}
}
---
testcase344:
class Animal {
	void move(){}
	void eat(){}
	void label() {
		System.out.println("Animal's data:");
	}
}
class Bird extends Animal {

	void move() {
		 System.out.println("Moves by flying.");
     }
	void eat() {
		 System.out.println("Eats birdfood.");
	}	 
}

class Fish extends Animal {
		 void move() {
			 System.out.println("Moves by swimming.");
	     }
		 void eat() {
			 System.out.println("Eats seafood.");
		 }
}
class TestBird {
	static void main() {
		Animal myBird;
		myBird := new Bird();

		myBird.label();
		myBird.move();
		myBird.eat();
	}
}

class TestFish {
	static void main() {
		Animal myFish;
		myFish := new Fish();

		myFish.label();
		myFish.move();
		myFish.eat();
	}
}
---
testcase345:
class testArray {
	int foo() {
		int[3] a = {5.1, 6.2, true};
	}
}
---
testcase346:
class a extends b 
{
    int c = this.ok().not_ok.very_ok().pho.rose.uu / 2 \ 5;
}
---
testcase347:
class Shape {
    static final int numOfShape = 0;
    final int immuAttribute = 0;
    float length,width;
    static int getNumOfShape() {
        return numOfShape;
    }
}
---
testcase348:
class a extends b 
{
    final int c = da != 5;
    int cactus;
    void kori() 
    {
        int x;
        final float x = 1.224;
        b := this.call(leftRecursive, rightRecursive);
    }
    void main() 
    {
        for x := 1 downto -1 do
        {
            x := x + 5;
        }
    }
}
---
testcase349:
class Understandable extends GoodBoy {
    void Void() {}
}
---
testcase350:
class Point 
{
    int x, y;
    static float length(Point a; Point b) 
    {
        return Math.sqrt(Math.sqr(a.x - b.x) - (a.y - b.y));
    }
}
class Triangle 
{
    Point point1, point2, point3;
    float edge1, edge2, edge3;
    Triangle(Point p1; Point p2; Point p3) 
    {
        this.point1 := p1;
        this.point2 := p2;
        this.point3 := p3;
        this.edge1 := Point.length(p1, p2);
        this.edge2 := Point.length(p2, p3);
        this.edge3 := Point.length(p3, p1);
    }
    float circumference() 
    {
        return (this.edge1 + this.edge2 + this.edge3) / 2;
    }
    float area() 
    {
        float p;
        p := this.circumference();
        return Math.sqrt(p * (p - this.edge1) * (p - this.edge2) * (p - this.edge3));
    }
} 
class Program
{
    void main() 
    {
        Point p1, p2, p3;
        Triangle abc;
        float area;
        p1 := new Point(0, 0);
        p2 := new Point(0, 1);
        p3 := new Point(1, 0);
        abc := new Triangle(p1, p2, p3);
        area := abc.area();
        io.writeLn("Area of triangle: ", area);
    }
} 
---
testcase351:
class scope 
{
    int x()
    {
        int x;
        {
            int x = 10;
            {
                final int x = 10;
                {
                    final float x = 4.12342421312312e-234125;
                }
            }
        }
    }
}
---
testcase352:
class a extends b 
{
    a() {}
    int count(int a; Shape b; string c, d, e) {}
    float[5] getFloatArray() {}
    void main() 
    {
        a := 2;
        a.b := 5;
        for x := 5 to 10 do
            x := x + 5;
    }
    int okay() 
    {
        a := 2;
        a.b := 5;
        for x := 5 to 10 do
        {
            break;
            continue;
            return x == y;
        }
    }
}
---
testcase353:
class Rectangle extends Shape {
    float getArea(){
        if a + b == 5 then 
            a := b;
        continue;
    }
}
---
testcase354:
class a extends b 
{
    final int c = daaaaaa != 5;
    int cactus;
    void kori() 
    {
        int x;
        final float x = 1.224;
        b := this.call(leftRecursive, rightRecursive);
    }
    static void main() 
    {
        for x := 1 downto -1 do
        {
            x := x + 5;
        }
    }
}
---
testcase355:
class Point 
{
    int x, y;
    static float length(Point a; Point b) 
    {
        return Math.sqrt(Math.sqr(a.x - b.x) - (a.y - b.y));
    }
}
---
testcase356:
class Triangle 
{
    Point point1, point2, point3;
    float edge1, edge2, edge3;
    Triangle(Point p1; Point p2; Point p3) 
    {
        this.point1 := p1;
        this.point2 := p2;
        this.point3 := p3;
        this.edge1 := Point.length(p1, p2);
        this.edge2 := Point.length(p2, p3);
        this.edge3 := Point.length(p3, p1);
    }
    float circumference() 
    {
        return (this.edge1 + this.edge2 + this.edge3) / 2;
    }
    float area() 
    {
        float p;
        p := this.circumference();
        return Math.sqrt(p * (p - this.edge1) * (p - this.edge2) * (p - this.edge3));
    }
} 
class Program
{
    void main() 
    {
        Point p1, p2, p3;
        Triangle abc;
        float area;
        p1 := new Point(0, 0);
        p2 := new Point(0, 1);
        p3 := new Point(1, 0);
        abc := new Triangle(p1, p2, p3);
        area := abc.area();
        io.writeLn("Area of triangle: ", area);
    }
}
---
testcase357:
class test 
    {
        int foo()
        {
            a := b / 2 * n / 4 && 5 % g || 2 * 9 / 4 % 2;
        }
    }
---
testcase358:        
class test 
{
    static void main() 
    {
        int[5] Kori = {1,2,3,4,5};
        Kori[5] := 7;
        this.print(Kori, 0, 4);
    }
}
---
testcase359:
class a extends b 
{
    static int a, b = 5, c = 66, d, e, f = 77, g = 8;
    final static int a = 1, b = 2, c = 3;
}
---
testcase360:
class Employee {
    string name;
    int age;

    Employee(string n; int a) {
        this.name := n;
        this.age := a;
    }

    void display() {
        io.writeStrLn("Employee Name: " ^ this.name);
        io.writeStrLn("Employee Age: " ^ this.age);
    }
}
---
testcase361:
class Manager extends Employee {
    string department;

    Manager(string n; int a; string dept) {
        this.Employee(n, a);
        this.department := dept;
    }

    void display() {
        io.writeStrLn("Manager Name: " ^ this.name);
        io.writeStrLn("Manager Age: " ^ this.age);
        io.writeStrLn("Manager Department: " ^ this.department);
    }
}
---
testcase362:
class Developer extends Employee {
    string programmingLanguage;

    Developer(string n; int a; string lang) {
        this.Employee(n, a);
        this.programmingLanguage := lang;
    }

    void display() {
        io.writeStrLn("Developer Name: " ^ this.name);
        io.writeStrLn("Developer Age: " ^ this.age);
        io.writeStrLn("Programming Language: " ^ this.programmingLanguage);
    }
}
---
testcase363:
class Test { /*
    static void main() { 
        Employee emp = new Employee("John Doe", 30);
        Manager manager = new Manager("Alice Smith", 40, "HR");
        Developer developer = new Developer("Bob Johnson", 25, "Java");
        Employee e1 = manager;
        Employee e2 = developer;
        emp.display();
        e1.display();
        e2.display();
    }*/
}
---
testcase364:
class test {
    void foo(int a,b;float c) {
    string _str_,o,c;
    }
}
---
testcase365:
class test {
    void main() {
        a := +a;
    }
}
---
testcase366:
        class ABC /* extends ABC {}
        {string terrorist = "ho" */
        {}
---
testcase367:
class PPL {
    string PPL = "Principles of Programming Languages";
    string lecturer = "Dr. Nguyen Hua Phung";
    void main(){
        string con;
        con := lecturer ^ " - ";
    }
}
---
testcase368:
class test {
    int foo() {
        a [(1 + 2 * 3 - 4 / 5 && 6 || 7)*(1+2+3)-(4+5*6/abc && !(123))] := a[(((-5)))];
    }
}
---
testcase369:
class main {
    float getArea(){
        a[3+x.foo(2)] := a[b[2]] +3;
        return this.length*this.width;
    }
}
---
testcase370:
class main {
            float getArea(){
        x.b[2] := x.m()[3];
        #start of declaration part
        {
float r,s;
int[5] a,b;
#list of statements
r:=2.0;
s:=r*r*this.myPI;
a[0]:= s;
}
                return this.length*this.width;
                }
           }
---
testcase371:
class a {
           }
class b {
    a bb(){continue;xxx.xxx[2] := aaa.aaa(a)[aaa];}
}
---
testcase372:
class Vehicle {
    void move() {
        io.writeStrLn("Vehicle is moving.");
    }
}
---
testcase373:
class Car extends Vehicle {
    void move() {
        io.writeStrLn("Car is driving on the road.");
    }
}
---
testcase374:
class Bicycle extends Vehicle {
    void move() {
        io.writeStrLn("Bicycle is pedaling on the path.");
    }
}
---
testcase375:
class Test {
    void main() {
        Vehicle[5] vehicles;
        vehicles[0] := new Vehicle();
        vehicles[1] := new Car();
        vehicles[2] := new Bicycle();
        
        for v:=0 to vehicles do {
            v.move();
        }
    }
}
---
testcase376:
class Vehicle {
    void move() {
        io.writeStrLn("Vehicle is moving.");
    }
}
class Car extends Vehicle {
    void move() {
        io.writeStrLn("Car is driving on the road.");
    }
}

class Bicycle extends Vehicle {
    void move() {
        io.writeStrLn("Bicycle is pedaling on the path.");
    }
}

class Test {
    void main() {
        Vehicle[5] vehicles;
        vehicles[0] := new Vehicle();
        vehicles[1] := new Car();
        vehicles[2] := new Bicycle();
        
        for v:=0 to vehicles do {
            v.move();
        }
    }
}
---
testcase377:
class Character {
    string name;
    int level;

    Character(string n; int l) {
        this.name := n;
        this.level := l;
    }

    void displayInfo() {
        io.writeStrLn("Name: " ^ this.name);
        io.writeStrLn("Level: " ^ this.level);
    }
}
---
testcase378:
class Warrior extends Character {
    string weapon;

    Warrior(string n; int l, w) {
        this.Character(n, l);
        this.weapon := w;
    }

    void displayInfo() {
        io.writeStrLn("Warrior:");
        this.Character.displayInfo();
        io.writeStrLn("Weapon: " ^ this.weapon);
    }
}
---
testcase379:
class Mage extends Character {
    string spell;

    Mage(string n; int l, s) {
        this.Character(n, l);
        this.spell := s;
    }

    void displayInfo() {
        io.writeStrLn("Mage:");
        this.Character.displayInfo();
        io.writeStrLn("Spell: " ^ this.spell);
    }
}
---
testcase380:
class Test {
    static void main() {
        Warrior warrior = new Warrior("Conan", 25, "Greatsword");
        Mage mage = new Mage("Gandalf", 30, "Fireball");

        Character[2] characters;
        characters[0] := warrior;
        characters[1] := mage;

        for c:=lemgth downto characters do {
            c.displayInfo();
            io.writeStrLn();
        }
    }
}
---
testcase381:
class Character {
    string name;
    int level;

    Character(string n; int l) {
        this.name := n;
        this.level := l;
    }

    void displayInfo() {
        io.writeStrLn("Name: " ^ this.name);
        io.writeStrLn("Level: " ^ this.level);
    }
}

class Warrior extends Character {
    string weapon;

    Warrior(string n; int l, w) {
        this.Character(n, l);
        this.weapon := w;
    }

    void displayInfo() {
        io.writeStrLn("Warrior:");
        this.Character.displayInfo();
        io.writeStrLn("Weapon: " ^ this.weapon);
    }
}

class Mage extends Character {
    string spell;

    Mage(string n; int l, s) {
        this.Character(n, l);
        this.spell := s;
    }

    void displayInfo() {
        io.writeStrLn("Mage:");
        this.Character.displayInfo();
        io.writeStrLn("Spell: " ^ this.spell);
    }
}

class Test {
    void main() {
        Warrior warrior = new Warrior("Conan", 25, "Greatsword");
        Mage mage = new Mage("Gandalf", 30, "Fireball");

        Character[2] characters;
        characters[0] := warrior;
        characters[1] := mage;

        for c:=0 to characters do {
            c.displayInfo();
            io.writeStrLn();
        }
    }
}
---
testcase382:
class MergeSort {
    void merge(int left,middle; int right) {
        int n1 = middle - left + 1;
        int n2 = right - middle;
        int[0] leftArray;
        int[0] rightArray;

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
testcase383:
class TestMergeSort {
    static void main() {
        int[10] numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6, 0};
        MergeSort sorter = new MergeSort();
        sorter.mergeSort(numbers, 0, numbers.length - 1);

        io.writeStrLn("Sorted Array:");
        for i := 0 to numbers.length - 1 do{
            io.writeInt(numbers[i]);
            io.writeChar(" ");
        }
    }
}
---
testcase384:
class BubbleSort {
    void sort(int[10] arr) {
        int temp;
        for i := 0 to length - 2 do {
            for j := 0 to length - 2 - i do {
                if arr[j] > arr[j + 1] then {
                   temp := arr[j];
                    arr[j] := arr[j + 1];
                    arr[j + 1] := temp;
                }
            }       
        }
    }

    void printArray(int[10] arr) {
        for i := 0 to length - 1 do {
            io.writeInt(arr[i]);
            io.writeChar(" ");
        }
    }
}
---
testcase385:
class TestBubbleSort {
    static void main() {
        int[7] array = {64, 34, 25, 12, 22, 11, 90};
        BubbleSort sorter = new BubbleSort();

        io.writeStrLn("Original array:");
        sorter.printArray(array);

        io.writeStrLn("\\nSorted array:");
        sorter.sort(array);
        sorter.printArray(array);
    }
}
---
testcase386:
class MergeSort {
    void merge(int left,middle; int right) {
        int n1 = middle - left + 1;
        int n2 = right - middle;
        int[0] leftArray;
        int[0] rightArray;

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

class TestMergeSort {
    static void main() {
        int[10] numbers = {5, 2, 8, 1, 9, 3, 7, 4, 6, 0};
        MergeSort sorter = new MergeSort();
        sorter.mergeSort(numbers, 0, numbers.length - 1);

        io.writeStrLn("Sorted Array:");
        for i := 0 to numbers.length - 1 do{
            io.writeInt(numbers[i]);
            io.writeChar(" ");
        }
    }
}
---
testcase387:
class BubbleSort {
    void sort(int[10] arr) {
        int temp;
        for i := 0 to length - 2 do {
            for j := 0 to length - 2 - i do {
                if arr[j] > arr[j + 1] then {
                   temp := arr[j];
                    arr[j] := arr[j + 1];
                    arr[j + 1] := temp;
                }
            }       
        }
    }

    void printArray(int[10] arr) {
        for i := 0 to length - 1 do {
            io.writeInt(arr[i]);
            io.writeChar(" ");
        }
    }
}

class TestBubbleSort {
    static void main() {
        int[7] array = {64, 34, 25, 12, 22, 11, 90};
        BubbleSort sorter = new BubbleSort();

        io.writeStrLn("Original array:");
        sorter.printArray(array);

        io.writeStrLn("\\nSorted array:");
        sorter.sort(array);
        sorter.printArray(array);
    }
}
---
testcase388:
class BinarySearch {
    int search(int[10] arr; int target; int low; int high) {
        int mid;
        if low > high then
            return -1; # Element not found
        
        mid := (low + high) / 2;
        
        if arr[mid] == target then
            return mid; # Element found at index 'mid'
        else 
            if arr[mid] > target then
                return this.search(arr, target, low, mid - 1); # Search in the left half
            else
            return this.search(arr, target, mid + 1, high); # Search in the right half
    }
}
---
testcase389:
class TestBinarySearch {
    static void main() {
        int[10] sortedArray = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;
        
        BinarySearch searchAlgorithm = new BinarySearch();
        int result = searchAlgorithm.search(sortedArray, target, 0, sortedArray.length - 1);
        
        if result != -1 then
            io.writeStrLn("Element " ^ target ^ " found at index " ^ result);
        else
            io.writeStrLn("Element " ^ target ^ " not found in the array");
    }
}
---
testcase390:
class BinarySearch {
    int search(int[10] arr; int target; int low; int high) {
        int mid;
        if low > high then
            return -1; # Element not found
        
        mid := (low + high) / 2;
        
        if arr[mid] == target then
            return mid; # Element found at index 'mid'
        else 
            if arr[mid] > target then
                return this.search(arr, target, low, mid - 1); # Search in the left half
            else
            return this.search(arr, target, mid + 1, high); # Search in the right half
    }
}

class TestBinarySearch {
    static void main() {
        int[10] sortedArray = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
        int target = 23;
        
        BinarySearch searchAlgorithm = new BinarySearch();
        int result = searchAlgorithm.search(sortedArray, target, 0, sortedArray.length - 1);
        
        if result != -1 then
            io.writeStrLn("Element " ^ target ^ " found at index " ^ result);
        else
            io.writeStrLn("Element " ^ target ^ " not found in the array");
    }
}
---
testcase391:
class Account {
    int accountNumber;
    float balance;

    Account(int number) {
        this.accountNumber := number;
        this.balance := 0.0;
    }

    void deposit(float amount) {
        this.balance := this.balance + amount;
    }

    void withdraw(float amount) {
        if amount <= this.balance then
            this.balance := this.balance - amount;
    
    }

    float getBalance() {
        return this.balance;
    }
}
---
testcase392:
class SavingsAccount extends Account {
    float interestRate;

    SavingsAccount(int number; float rate) {
        this.Account(number);
        this.interestRate := rate;
    }

    void applyInterest() {
        float interest = this.balance * this.interestRate;
        this.deposit(interest);
    }
}
---
testcase393:
class CheckingAccount extends Account {
    float overdraftLimit;

    CheckingAccount(int number; float limit) {
        this.Account(number);
        this.overdraftLimit := limit;
    }

    void withdraw(float amount) {
        if amount <= this.balance + this.overdraftLimit then
            this.balance := this.balance - amount;
    }
}
---
testcase394:
class Bank {
    Account[10] accounts;

    Bank(int numAccounts) {
        this.accounts := new Account();
        for i := 0 to numAccounts - 1 do
            if i % 2 == 0 then
                this.accounts[i] := new SavingsAccount(i, 0.05);
            else
                this.accounts[i] := new CheckingAccount(i, 500.0);
        
        
    }

    void simulateTransactions() {
        for i := 0 to this.accounts.length - 1 do
            if this.accounts[i] == SavingsAccount then {
                SavingsAccount sa = this.accounts[i];
                sa.deposit(100.0);
                sa.applyInterest();
            }
            else{
                CheckingAccount ca = this.accounts[i];
                ca.deposit(200.0);
                ca.withdraw(300.0);
            }
        
    }

    void printAccountBalances() {
        for i := 0 to this.accounts.length - 1 do
            io.writeStrLn("Account " ^ i ^ " Balance: " ^ (this.accounts[i]).getBalance());
        
    }
}
---
testcase395:
class TestBank {
    void main() {
        Bank bank = new Bank(10);
        bank.simulateTransactions();
        bank.printAccountBalances();
    }
}
---
testcase396:
class Account {
    int accountNumber;
    float balance;

    Account(int number) {
        this.accountNumber := number;
        this.balance := 0.0;
    }

    void deposit(float amount) {
        this.balance := this.balance + amount;
    }

    void withdraw(float amount) {
        if amount <= this.balance then
            this.balance := this.balance - amount;
    
    }

    float getBalance() {
        return this.balance;
    }
}

class SavingsAccount extends Account {
    float interestRate;

    SavingsAccount(int number; float rate) {
        this.Account(number);
        this.interestRate := rate;
    }

    void applyInterest() {
        float interest = this.balance * this.interestRate;
        this.deposit(interest);
    }
}

class CheckingAccount extends Account {
    float overdraftLimit;

    CheckingAccount(int number; float limit) {
        this.Account(number);
        this.overdraftLimit := limit;
    }

    void withdraw(float amount) {
        if amount <= this.balance + this.overdraftLimit then
            this.balance := this.balance - amount;
    }
}

class Bank {
    Account[10] accounts;

    Bank(int numAccounts) {
        this.accounts := new Account();
        for i := 0 to numAccounts - 1 do
            if i % 2 == 0 then
                this.accounts[i] := new SavingsAccount(i, 0.05);
            else
                this.accounts[i] := new CheckingAccount(i, 500.0);
        
        
    }

    void simulateTransactions() {
        for i := 0 to this.accounts.length - 1 do
            if this.accounts[i] == SavingsAccount then {
                SavingsAccount sa = this.accounts[i];
                sa.deposit(100.0);
                sa.applyInterest();
            }
            else{
                CheckingAccount ca = this.accounts[i];
                ca.deposit(200.0);
                ca.withdraw(300.0);
            }
        
    }

    void printAccountBalances() {
        for i := 0 to this.accounts.length - 1 do
            io.writeStrLn("Account " ^ i ^ " Balance: " ^ (this.accounts[i]).getBalance());
        
    }
}

class TestBank {
    void main() {
        Bank bank = new Bank(10);
        bank.simulateTransactions();
        bank.printAccountBalances();
 
   }
}
---
testcase397:
class OperatorTest {
    void main() {
        {
        int a = 10;
        int b = 20;
        float x = 15.5;
        boolean condition = true;

        int result1 = (a + b) * (b - a) / 2;
        float result2 = (a * b + x) / (x - b);
        boolean result3 = (a < b) && (x >= a) || condition;

        io.writeStrLn("Result 1: " ^ result1);
        io.writeStrLn("Result 2: " ^ result2);
        io.writeStrLn("Result 3: " ^ result3);
        }
        {
        int[5] numbers = {1, 2, 3, 4, 5};
        int sum = 0;
        for i := 0 to numbers.length - 1 do {
            sum := sum + numbers[i];
        }

        if sum % 2 == 0 then {
            io.writeStrLn("Sum of numbers is even.");
        } else {
            io.writeStrLn("Sum of numbers is odd.");
        }
        }
    }
}
---
testcase398:
class SuperComplexTest {
    static float customPower(float base; int exponent) {
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
testcase399:
class UltraComplexTest {
    static int factorial(int n) {
        if (n <= 1)then {
            return 1;
        } else {
            return n * this.factorial(n - 1);
        }
    }

    static int gcd(int a, b) {
        if (b == 0) then {
            return a;
        } else {
            return this.gcd(b, a % b);
        }
    }

    static float computeSeries(int x) {
        float result = 0;

        for i := 1 to 10 do {
            result := result + this.customPower(x, i) / this.factorial(i);
        }

        return result;
    }

    static float customPower(float base; int exponent) {
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

    static void main() {
        int finalResult = 0;

        for a := 1 to 5 do {
            for b := 1 to 5 do {
                if (a != b) then {
                    for c := 1 to 5 do {
                        for d := 1 to 5 do {
                            if (c != d) then {
                                int gcdValue = this.gcd(a * b, c * d);
                                int sum = a + b + c + d;

                                float seriesResult = this.computeSeries(sum);

                                if (gcdValue % 2 == 0) then {
                                    finalResult := finalResult + (seriesResult * gcdValue);
                                } else {
                                    finalResult := finalResult -  (seriesResult / gcdValue);
                                }
                            }
                        }
                    }
                }
            }
        }

        io.writeStrLn("Final Result: " ^ finalResult);
    }
}
---

"""
e ="""
testcase300:Program([ClassDecl(Id(a),[AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType))])])
---
testcase301:Program([ClassDecl(Id(a),[AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,BinaryOp(+,IntLit(3),IntLit(4))))])])
---
testcase302:Program([ClassDecl(Id(a),[AttributeDecl(Static,ConstDecl(Id(c),BoolType,IntLit(2)))])])
---
testcase303:Program([ClassDecl(Id(a),[AttributeDecl(Static,ConstDecl(Id(c),IntType,None))])])
---
testcase304:Program([ClassDecl(Id(a),[AttributeDecl(Static,VarDecl(Id(a),FloatType))])])
---
testcase305:Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])
---
testcase306:Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))])),MethodDecl(Id(getLength),Instance,[],FloatType,Block([],[Return(BinaryOp(+,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])
---
testcase307:Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))])])
---
testcase308:Program([ClassDecl(Id(Rectangle),[MethodDecl(Id(getArea),Instance,[param(Id(a),FloatType),param(Id(b),FloatType),param(Id(c),IntType)],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])
---
testcase309:Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])
---
testcase310:Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),BoolType))])])
---
testcase311:Program([ClassDecl(Id(Circle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,BinaryOp(*,FloatLit(3.14),FieldAccess(Self(),Id(radius))),FieldAccess(Self(),Id(radius))))]))])])
---
testcase312:Program([ClassDecl(Id(Test),[MethodDecl(Id(printMessage),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Hello, World!)])]))])])
---
testcase313:Program([ClassDecl(Id(Math),[MethodDecl(Id(max),Static,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[If(BinaryOp(>,Id(a),Id(b)),Return(Id(a)),Return(Id(b)))]))])])
---
testcase314:Program([ClassDecl(Id(Circle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,BinaryOp(*,FloatLit(3.14),FieldAccess(Self(),Id(radius))),FieldAccess(Self(),Id(radius))))]))]),ClassDecl(Id(Square),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(length))))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(c),ClassType(Id(Shape))),VarDecl(Id(s),ClassType(Id(Shape))),VarDecl(Id(area1),FloatType),VarDecl(Id(area2),FloatType)],[AssignStmt(Id(c),NewExpr(Id(Circle),[])),AssignStmt(Id(s),NewExpr(Id(Square),[])),AssignStmt(Id(area1),CallExpr(Id(c),Id(getArea),[])),AssignStmt(Id(area2),CallExpr(Id(s),Id(getArea),[])),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Area of Circle: ),Id(area1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Area of Square: ),Id(area2))])]))])])
---
testcase315:Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(l),FloatType),param(Id(w),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(length)),Id(l)),AssignStmt(FieldAccess(Self(),Id(width)),Id(w))]))]),ClassDecl(Id(Circle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,BinaryOp(*,FloatLit(3.14),FieldAccess(Self(),Id(radius))),FieldAccess(Self(),Id(radius))))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(c),ClassType(Id(Circle)),NewExpr(Id(Circle),[FloatLit(5.0),FloatLit(5.0)])),VarDecl(Id(area),FloatType,CallExpr(Id(c),Id(getArea),[]))],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Area of Circle: ),Id(area))])]))])])
---
testcase316:Program([ClassDecl(Id(Animal),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(age),IntType)),MethodDecl(Id(<init>),Instance,[param(Id(name),StringType),param(Id(age),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(age)),Id(age))])),MethodDecl(Id(makeSound),Instance,[],VoidType,Block([],[]))]),ClassDecl(Id(Dog),Id(Animal),[AttributeDecl(Instance,VarDecl(Id(breed),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(name),StringType),param(Id(age),IntType),param(Id(breed),StringType)],Block([],[Call(Self(),Id(Animal),[Id(name),Id(age)]),AssignStmt(FieldAccess(Self(),Id(breed)),Id(breed))])),MethodDecl(Id(makeSound),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Woof! Woof!)])])),MethodDecl(Id(fetch),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Fetching the ball!)])]))]),ClassDecl(Id(Cat),Id(Animal),[AttributeDecl(Instance,VarDecl(Id(furColor),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(name),StringType),param(Id(age),IntType),param(Id(furColor),StringType)],Block([],[Call(Self(),Id(Animal),[Id(name),Id(age)]),AssignStmt(FieldAccess(Self(),Id(furColor)),Id(furColor))])),MethodDecl(Id(makeSound),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Meow!)])])),MethodDecl(Id(climbTree),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Climbing the tree!)])]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(dog),ClassType(Id(Dog)),NewExpr(Id(Dog),[StringLit(Buddy),IntLit(3),StringLit(Labrador)])),VarDecl(Id(cat),ClassType(Id(Cat)),NewExpr(Id(Cat),[StringLit(Whiskers),IntLit(2),StringLit(Gray)])),VarDecl(Id(animal1),ClassType(Id(Animal)),Id(dog)),VarDecl(Id(animal2),ClassType(Id(Animal)),Id(cat))],[Call(Id(dog),Id(makeSound),[]),Call(Id(cat),Id(makeSound),[]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Dog's breed: ),FieldAccess(Id(dog),Id(breed)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Cat's fur color: ),FieldAccess(Id(cat),Id(furColor)))]),Call(Id(animal1),Id(makeSound),[]),Call(Id(animal2),Id(makeSound),[]),Call(Id(animal1),Id(fetch),[]),Call(Id(animal2),Id(climbTree),[])]))])])
---
testcase317:Program([ClassDecl(Id(Point),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),MethodDecl(Id(<init>),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(x)),Id(x)),AssignStmt(FieldAccess(Self(),Id(y)),Id(y))])),MethodDecl(Id(display),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(x: ),FieldAccess(Self(),Id(x))),StringLit(, y: )),FieldAccess(Self(),Id(y)))])])),MethodDecl(Id(add),Static,[param(Id(p1),ClassType(Id(Point))),param(Id(p2),ClassType(Id(Point)))],ClassType(Id(Point)),Block([],[Return(NewExpr(Id(Point),[BinaryOp(+,FieldAccess(Id(p1),Id(x)),FieldAccess(Id(p2),Id(x))),BinaryOp(+,FieldAccess(Id(p1),Id(y)),FieldAccess(Id(p2),Id(y)))]))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(p1),ClassType(Id(Point)),NewExpr(Id(Point),[IntLit(3),IntLit(5)])),VarDecl(Id(p2),ClassType(Id(Point)),NewExpr(Id(Point),[UnaryOp(-,IntLit(2)),IntLit(7)])),VarDecl(Id(sum),ClassType(Id(Point)),CallExpr(Id(Point),Id(add),[Id(p1),Id(p2)]))],[Call(Id(p1),Id(display),[]),Call(Id(p2),Id(display),[]),Call(Id(sum),Id(display),[])]))])])
---
testcase318:Program([ClassDecl(Id(Student),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(age),IntType)),AttributeDecl(Instance,VarDecl(Id(gpa),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(name),StringType),param(Id(age),IntType),param(Id(gpa),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(age)),Id(age)),AssignStmt(FieldAccess(Self(),Id(gpa)),Id(gpa))])),MethodDecl(Id(display),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Name:),FieldAccess(Self(),Id(name)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Age:),FieldAccess(Self(),Id(age)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(GPA:),FieldAccess(Self(),Id(gpa)))])])),MethodDecl(Id(getGrade),Instance,[],StringType,Block([],[If(BinaryOp(>=,FieldAccess(Self(),Id(gpa)),FloatLit(3.5)),Return(StringLit(A)),Block([],[If(BinaryOp(>=,FieldAccess(Self(),Id(gpa)),FloatLit(3.0)),Return(StringLit(B)),Block([],[If(BinaryOp(>=,FieldAccess(Self(),Id(gpa)),FloatLit(2.0)),Return(StringLit(C)),Block([],[If(BinaryOp(>=,FieldAccess(Self(),Id(gpa)),FloatLit(1.0)),Return(StringLit(D)),Return(StringLit(F)))]))]))]))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s1),ClassType(Id(Student)),NewExpr(Id(Student),[StringLit(Alice),IntLit(20),FloatLit(3.8)])),VarDecl(Id(s2),ClassType(Id(Student)),NewExpr(Id(Student),[StringLit(Bob),IntLit(19),FloatLit(2.9)]))],[Call(Id(s1),Id(display),[]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Grade:),CallExpr(Id(s1),Id(getGrade),[]))]),Call(Id(s2),Id(display),[]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Grade:),CallExpr(Id(s2),Id(getGrade),[]))])]))])])
---
testcase319:Program([ClassDecl(Id(Math),[MethodDecl(Id(factorial),Static,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(==,Id(n),IntLit(0)),Block([],[Return(IntLit(1))]),Block([],[Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))])))]))])),MethodDecl(Id(fibonacci),Static,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(<=,Id(n),IntLit(1)),Block([],[Return(Id(n))]),Block([],[Return(BinaryOp(+,CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(n),IntLit(1))]),CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(n),IntLit(2))])))]))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(num1),IntType,IntLit(5)),VarDecl(Id(num2),IntType,IntLit(6)),VarDecl(Id(factNum1),IntType,CallExpr(Id(Math),Id(factorial),[Id(num1)])),VarDecl(Id(factNum2),IntType,CallExpr(Id(Math),Id(factorial),[Id(num2)])),VarDecl(Id(fibNum1),IntType,CallExpr(Id(Math),Id(fibonacci),[Id(num1)])),VarDecl(Id(fibNum2),IntType,CallExpr(Id(Math),Id(fibonacci),[Id(num2)]))],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Factorial_of),Id(num1)),StringLit(:)),Id(factNum1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Factorial_of),Id(num2)),StringLit(:)),Id(factNum2))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Fibonacci_of),Id(num1)),StringLit(:)),Id(fibNum1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Fibonacci_of),Id(num2)),StringLit(:)),Id(fibNum2))])]))])])
---
testcase320:Program([ClassDecl(Id(Bank),[AttributeDecl(Instance,VarDecl(Id(interestRate),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(rate),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(interestRate)),Id(rate))])),MethodDecl(Id(calculateInterest),Instance,[param(Id(principal),FloatType)],FloatType,Block([],[Return(BinaryOp(*,Id(principal),FieldAccess(Self(),Id(interestRate))))]))]),ClassDecl(Id(SavingsAccount),Id(Bank),[MethodDecl(Id(<init>),Instance,[param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Bank),[Id(rate)])])),MethodDecl(Id(calculateInterestReal),Instance,[param(Id(principal),FloatType)],FloatType,Block([],[Return(BinaryOp(+,CallExpr(Self(),Id(calculateInterest),[Id(principal)]),IntLit(100)))]))]),ClassDecl(Id(FixedDeposit),Id(Bank),[MethodDecl(Id(<init>),Instance,[param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Bank),[Id(rate)])])),MethodDecl(Id(calculateInterestReal),Instance,[param(Id(principal),FloatType),param(Id(years),IntType)],FloatType,Block([],[Return(BinaryOp(*,CallExpr(Self(),Id(calculateInterest),[Id(principal)]),Id(years)))]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(bank1),ClassType(Id(Bank))),VarDecl(Id(bank2),ClassType(Id(Bank))),VarDecl(Id(principal),FloatType,FloatLit(1000.0)),VarDecl(Id(interest1),FloatType),VarDecl(Id(interest2),FloatType)],[AssignStmt(Id(bank1),NewExpr(Id(SavingsAccount),[FloatLit(0.05)])),AssignStmt(Id(bank2),NewExpr(Id(FixedDeposit),[FloatLit(0.08)])),AssignStmt(Id(interest1),CallExpr(Id(bank1),Id(calculateInterest),[Id(principal)])),AssignStmt(Id(interest2),CallExpr(Id(bank2),Id(calculateInterest),[Id(principal),IntLit(5)])),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Interest_from_Savings_Account:),Id(interest1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Interest_from_Fixed Deposit:),Id(interest2))])]))])])
---
testcase321:Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(a),IntType,IntLit(5)),VarDecl(Id(b),IntType,IntLit(10)),VarDecl(Id(c),IntType,IntLit(15)),VarDecl(Id(result),BoolType,BinaryOp(>=,BinaryOp(+,Id(a),BinaryOp(*,Id(b),Id(c))),BinaryOp(&&,BinaryOp(-,Id(c),BinaryOp(/,Id(b),Id(a))),UnaryOp(!,BinaryOp(>,Id(a),Id(b))))))],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result: ),Id(result))])]))])])
---
testcase322:Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(p),BoolType,BooleanLit(True)),VarDecl(Id(q),BoolType,BooleanLit(False)),VarDecl(Id(result),BoolType,BinaryOp(||,BinaryOp(&&,Id(p),Id(q)),UnaryOp(!,Id(p))))],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result:),Id(result))])]))])])
---
testcase323:Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(a),IntType,IntLit(5)),VarDecl(Id(b),IntType,IntLit(10)),VarDecl(Id(c),IntType,IntLit(15)),VarDecl(Id(result1),BoolType,BinaryOp(>,BinaryOp(*,BinaryOp(+,Id(a),Id(b)),Id(c)),BinaryOp(+,Id(a),BinaryOp(*,Id(b),Id(c))))),VarDecl(Id(result2),BoolType,BinaryOp(||,BinaryOp(&&,BinaryOp(>=,Id(a),Id(b)),BinaryOp(<,Id(c),Id(a))),BinaryOp(<=,Id(b),Id(c)))),VarDecl(Id(result3),BoolType,BinaryOp(&&,UnaryOp(!,BinaryOp(!=,BinaryOp(||,BinaryOp(==,Id(a),Id(b)),Id(c)),Id(b))),UnaryOp(!,BinaryOp(>,Id(c),BinaryOp(&&,Id(a),BinaryOp(<,Id(b),Id(c)))))))],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result 1: ),Id(result1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result 2: ),Id(result2))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result 3: ),Id(result3))])]))])])
---
testcase324:Program([ClassDecl(Id(Person),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(age),IntType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(a),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(name)),Id(n)),AssignStmt(FieldAccess(Self(),Id(age)),Id(a))])),MethodDecl(Id(display),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Name:),FieldAccess(Self(),Id(name)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Age:),FieldAccess(Self(),Id(age)))])]))])])
---
testcase325:Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(persons),ArrayType(3,ClassType(Id(Person)))),VarDecl(Id(totalAge),IntType,IntLit(0))],[AssignStmt(ArrayCell(Id(persons),IntLit(0)),NewExpr(Id(Person),[StringLit(Alice),IntLit(25)])),AssignStmt(ArrayCell(Id(persons),IntLit(1)),NewExpr(Id(Person),[StringLit(Bob),IntLit(30)])),AssignStmt(ArrayCell(Id(persons),IntLit(2)),NewExpr(Id(Person),[StringLit(Charlie),IntLit(22)])),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Total Age:),Id(totalAge))])]))])])
---
testcase326:Program([ClassDecl(Id(Library),[AttributeDecl(Instance,VarDecl(Id(books),ArrayType(5,ClassType(Id(Book))))),MethodDecl(Id(<init>),Instance,[param(Id(b),ArrayType(5,ClassType(Id(Book))))],Block([],[AssignStmt(Id(books),Id(b))])),MethodDecl(Id(displayBooks),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Library_Catalog:)]),For(Id(i),IntLit(0),FieldAccess(Id(books),Id(length)),True,Block([],[Call(ArrayCell(Id(books),Id(i)),Id(displayInfo),[])])])]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(bookList),ArrayType(3,ClassType(Id(Book)))),VarDecl(Id(myLibrary),ClassType(Id(Library)),NewExpr(Id(Library),[Id(bookList)]))],[AssignStmt(ArrayCell(Id(bookList),IntLit(0)),NewExpr(Id(Book),[StringLit(HarryPotter),StringLit(J.K.Rowling)])),AssignStmt(ArrayCell(Id(bookList),IntLit(1)),NewExpr(Id(Book),[StringLit(TheHobbit),StringLit(J.R.R.Tolkien)]))]))])])
---
testcase327:Program([ClassDecl(Id(array),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),IntLit(2)),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3)))]))])])
---
testcase328:Program([ClassDecl(Id(array),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])
---
testcase329:Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))])])
---
testcase330:Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)))],[AssignStmt(Id(s),NewExpr(Id(Rectangle),[IntLit(3),IntLit(4)])),AssignStmt(Id(s),NewExpr(Id(Triangle),[IntLit(3),IntLit(4)]))]))])])
---
testcase331:Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(5),IntLit(10)]))],[]))])])
---
testcase332:Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(FieldAccess(Self(),Id(aPI)),FloatLit(3.14)),AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5)])),AssignStmt(ArrayCell(Id(l),IntLit(3)),BinaryOp(*,Id(value),IntLit(2)))]))])])
---
testcase333:Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(r),FloatType),VarDecl(Id(s),FloatType),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType))],[AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),IntLit(0)),Id(s))]))])])
---
testcase334:Program([ClassDecl(Id(testForLoop),[MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(i),IntLit(1),IntLit(100),True,Block([],[Call(Id(io),Id(writeIntLn),[Id(i)]),AssignStmt(ArrayCell(Id(Intarray),Id(i)),BinaryOp(+,Id(i),IntLit(1)))])]),For(Id(x),IntLit(5),IntLit(2),False,Call(Id(io),Id(writeIntLn),[Id(x)])])]))])])
---
testcase335:Program([ClassDecl(Id(testBrS),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Break]))])])
---
testcase336:Program([ClassDecl(Id(testConS),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Continue]))])])
---
testcase337:Program([ClassDecl(Id(fac),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(==,Id(n),IntLit(0)),Return(IntLit(1)),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]))))])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(x),IntType)],[AssignStmt(Id(x),CallExpr(Id(io),Id(readInt),[])),Call(Id(io),Id(writeIntLn),[CallExpr(Self(),Id(factorial),[Id(x)])])]))])])
---
testcase338:Program([ClassDecl(Id(decl),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),AttributeDecl(Instance,VarDecl(Id(y),FloatType)),AttributeDecl(Instance,VarDecl(Id(z),StringType,StringLit(abc))),AttributeDecl(Static,VarDecl(Id(d),BoolType,BooleanLit(True)))])])
---
testcase339:Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(z),StringType)),MethodDecl(Id(nml),Instance,[],FloatType,Block([],[For(Id(i),Id(a),Id(b),True,Call(Self(),Id(hahaha),[])]),For(Id(i),IntLit(4),UnaryOp(-,IntLit(5)),False,AssignStmt(Id(h),IntLit(6))]),Return(IntLit(1))]))])])
---
testcase340:Program([ClassDecl(Id(testPrecedence),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(&&,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),IntLit(5))),IntLit(6)),UnaryOp(-,IntLit(7))),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),BinaryOp(&&,BinaryOp(+,IntLit(4),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),Id(abc))),IntLit(123)))),ArrayCell(Id(a),UnaryOp(-,IntLit(5))))]))])])
---
testcase341:Program([ClassDecl(Id(testPrecedence),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(||,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),IntLit(5))),IntLit(6)),IntLit(7)),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),BinaryOp(&&,BinaryOp(+,IntLit(4),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),Id(abc))),UnaryOp(!,IntLit(123))))),ArrayCell(Id(a),UnaryOp(-,IntLit(5))))]))])])
---
testcase342:Program([ClassDecl(Id(testFor),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),IntLit(1),BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(10),IntLit(5)),BinaryOp(*,IntLit(4),Id(e))),Id(x)),True,Break])]))])])
---
testcase343:Program([ClassDecl(Id(String1),[AttributeDecl(Instance,VarDecl(Id(a),StringType,StringLit(chacachien))),MethodDecl(Id(getString),Instance,[],StringType,Block([],[Return(FieldAccess(Self(),Id(a)))]))]),ClassDecl(Id(String2),[AttributeDecl(Instance,VarDecl(Id(b),StringType,StringLit(NguyenPhat))),MethodDecl(Id(getString),Instance,[],StringType,Block([],[Return(FieldAccess(Self(),Id(b)))]))]),ClassDecl(Id(Example),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(str1),ClassType(Id(String1))),VarDecl(Id(str2),ClassType(Id(String2))),VarDecl(Id(result),StringType)],[AssignStmt(Id(result),BinaryOp(^,FieldAccess(Id(str1),Id(getString)),FieldAccess(Id(str2),Id(getString))))]))])])
---
testcase344:Program([ClassDecl(Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[])),MethodDecl(Id(eat),Instance,[],VoidType,Block([],[])),MethodDecl(Id(label),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Animal's data:)])]))]),ClassDecl(Id(Bird),Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Moves by flying.)])])),MethodDecl(Id(eat),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Eats birdfood.)])]))]),ClassDecl(Id(Fish),Id(Animal),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Moves by swimming.)])])),MethodDecl(Id(eat),Instance,[],VoidType,Block([],[Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Eats seafood.)])]))]),ClassDecl(Id(TestBird),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(myBird),ClassType(Id(Animal)))],[AssignStmt(Id(myBird),NewExpr(Id(Bird),[])),Call(Id(myBird),Id(label),[]),Call(Id(myBird),Id(move),[]),Call(Id(myBird),Id(eat),[])]))]),ClassDecl(Id(TestFish),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(myFish),ClassType(Id(Animal)))],[AssignStmt(Id(myFish),NewExpr(Id(Fish),[])),Call(Id(myFish),Id(label),[]),Call(Id(myFish),Id(move),[]),Call(Id(myFish),Id(eat),[])]))])])
---
testcase345:Program([ClassDecl(Id(testArray),[MethodDecl(Id(foo),Instance,[],IntType,Block([VarDecl(Id(a),ArrayType(3,IntType),[FloatLit(5.1),FloatLit(6.2),BooleanLit(True)])],[]))])])
---
testcase346:Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(\,BinaryOp(/,FieldAccess(FieldAccess(FieldAccess(CallExpr(FieldAccess(CallExpr(Self(),Id(ok),[]),Id(not_ok)),Id(very_ok),[]),Id(pho)),Id(rose)),Id(uu)),IntLit(2)),IntLit(5))))])])
---
testcase347:Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))])])
---
testcase348:Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(!=,Id(da),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(cactus),IntType)),MethodDecl(Id(kori),Instance,[],VoidType,Block([VarDecl(Id(x),IntType),ConstDecl(Id(x),FloatType,FloatLit(1.224))],[AssignStmt(Id(b),CallExpr(Self(),Id(call),[Id(leftRecursive),Id(rightRecursive)]))])),MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(x),IntLit(1),UnaryOp(-,IntLit(1)),False,Block([],[AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5)))])])]))])])
---
testcase349:Program([ClassDecl(Id(Understandable),Id(GoodBoy),[MethodDecl(Id(Void),Instance,[],VoidType,Block([],[]))])])
---
testcase350:Program([ClassDecl(Id(Point),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),MethodDecl(Id(length),Static,[param(Id(a),ClassType(Id(Point))),param(Id(b),ClassType(Id(Point)))],FloatType,Block([],[Return(CallExpr(Id(Math),Id(sqrt),[BinaryOp(-,CallExpr(Id(Math),Id(sqr),[BinaryOp(-,FieldAccess(Id(a),Id(x)),FieldAccess(Id(b),Id(x)))]),BinaryOp(-,FieldAccess(Id(a),Id(y)),FieldAccess(Id(b),Id(y))))]))]))]),ClassDecl(Id(Triangle),[AttributeDecl(Instance,VarDecl(Id(point1),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point2),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point3),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(edge1),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge2),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge3),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(p1),ClassType(Id(Point))),param(Id(p2),ClassType(Id(Point))),param(Id(p3),ClassType(Id(Point)))],Block([],[AssignStmt(FieldAccess(Self(),Id(point1)),Id(p1)),AssignStmt(FieldAccess(Self(),Id(point2)),Id(p2)),AssignStmt(FieldAccess(Self(),Id(point3)),Id(p3)),AssignStmt(FieldAccess(Self(),Id(edge1)),CallExpr(Id(Point),Id(length),[Id(p1),Id(p2)])),AssignStmt(FieldAccess(Self(),Id(edge2)),CallExpr(Id(Point),Id(length),[Id(p2),Id(p3)])),AssignStmt(FieldAccess(Self(),Id(edge3)),CallExpr(Id(Point),Id(length),[Id(p3),Id(p1)]))])),MethodDecl(Id(circumference),Instance,[],FloatType,Block([],[Return(BinaryOp(/,BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(edge1)),FieldAccess(Self(),Id(edge2))),FieldAccess(Self(),Id(edge3))),IntLit(2)))])),MethodDecl(Id(area),Instance,[],FloatType,Block([VarDecl(Id(p),FloatType)],[AssignStmt(Id(p),CallExpr(Self(),Id(circumference),[])),Return(CallExpr(Id(Math),Id(sqrt),[BinaryOp(*,BinaryOp(*,BinaryOp(*,Id(p),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge1)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge2)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge3))))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(p1),ClassType(Id(Point))),VarDecl(Id(p2),ClassType(Id(Point))),VarDecl(Id(p3),ClassType(Id(Point))),VarDecl(Id(abc),ClassType(Id(Triangle))),VarDecl(Id(area),FloatType)],[AssignStmt(Id(p1),NewExpr(Id(Point),[IntLit(0),IntLit(0)])),AssignStmt(Id(p2),NewExpr(Id(Point),[IntLit(0),IntLit(1)])),AssignStmt(Id(p3),NewExpr(Id(Point),[IntLit(1),IntLit(0)])),AssignStmt(Id(abc),NewExpr(Id(Triangle),[Id(p1),Id(p2),Id(p3)])),AssignStmt(Id(area),CallExpr(Id(abc),Id(area),[])),Call(Id(io),Id(writeLn),[StringLit(Area of triangle: ),Id(area)])]))])])
---
testcase351:Program([ClassDecl(Id(scope),[MethodDecl(Id(x),Instance,[],IntType,Block([VarDecl(Id(x),IntType)],[Block([VarDecl(Id(x),IntType,IntLit(10))],[Block([ConstDecl(Id(x),IntType,IntLit(10))],[Block([ConstDecl(Id(x),FloatType,FloatLit(0.0))],[])])])]))])])
---
testcase352:Program([ClassDecl(Id(a),Id(b),[MethodDecl(Id(<init>),Instance,[],Block([],[])),MethodDecl(Id(count),Instance,[param(Id(a),IntType),param(Id(b),ClassType(Id(Shape))),param(Id(c),StringType),param(Id(d),StringType),param(Id(e),StringType)],IntType,Block([],[])),MethodDecl(Id(getFloatArray),Instance,[],ArrayType(5,FloatType),Block([],[])),MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(Id(a),IntLit(2)),AssignStmt(FieldAccess(Id(a),Id(b)),IntLit(5)),For(Id(x),IntLit(5),IntLit(10),True,AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5)))])])),MethodDecl(Id(okay),Instance,[],IntType,Block([],[AssignStmt(Id(a),IntLit(2)),AssignStmt(FieldAccess(Id(a),Id(b)),IntLit(5)),For(Id(x),IntLit(5),IntLit(10),True,Block([],[Break,Continue,Return(BinaryOp(==,Id(x),Id(y)))])])]))])])
---
testcase353:Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[If(BinaryOp(==,BinaryOp(+,Id(a),Id(b)),IntLit(5)),AssignStmt(Id(a),Id(b))),Continue]))])])
---
testcase354:Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(!=,Id(daaaaaa),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(cactus),IntType)),MethodDecl(Id(kori),Instance,[],VoidType,Block([VarDecl(Id(x),IntType),ConstDecl(Id(x),FloatType,FloatLit(1.224))],[AssignStmt(Id(b),CallExpr(Self(),Id(call),[Id(leftRecursive),Id(rightRecursive)]))])),MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(x),IntLit(1),UnaryOp(-,IntLit(1)),False,Block([],[AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5)))])])]))])])
---
testcase355:Program([ClassDecl(Id(Point),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),MethodDecl(Id(length),Static,[param(Id(a),ClassType(Id(Point))),param(Id(b),ClassType(Id(Point)))],FloatType,Block([],[Return(CallExpr(Id(Math),Id(sqrt),[BinaryOp(-,CallExpr(Id(Math),Id(sqr),[BinaryOp(-,FieldAccess(Id(a),Id(x)),FieldAccess(Id(b),Id(x)))]),BinaryOp(-,FieldAccess(Id(a),Id(y)),FieldAccess(Id(b),Id(y))))]))]))])])
---
testcase356:Program([ClassDecl(Id(Triangle),[AttributeDecl(Instance,VarDecl(Id(point1),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point2),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(point3),ClassType(Id(Point)))),AttributeDecl(Instance,VarDecl(Id(edge1),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge2),FloatType)),AttributeDecl(Instance,VarDecl(Id(edge3),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(p1),ClassType(Id(Point))),param(Id(p2),ClassType(Id(Point))),param(Id(p3),ClassType(Id(Point)))],Block([],[AssignStmt(FieldAccess(Self(),Id(point1)),Id(p1)),AssignStmt(FieldAccess(Self(),Id(point2)),Id(p2)),AssignStmt(FieldAccess(Self(),Id(point3)),Id(p3)),AssignStmt(FieldAccess(Self(),Id(edge1)),CallExpr(Id(Point),Id(length),[Id(p1),Id(p2)])),AssignStmt(FieldAccess(Self(),Id(edge2)),CallExpr(Id(Point),Id(length),[Id(p2),Id(p3)])),AssignStmt(FieldAccess(Self(),Id(edge3)),CallExpr(Id(Point),Id(length),[Id(p3),Id(p1)]))])),MethodDecl(Id(circumference),Instance,[],FloatType,Block([],[Return(BinaryOp(/,BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(edge1)),FieldAccess(Self(),Id(edge2))),FieldAccess(Self(),Id(edge3))),IntLit(2)))])),MethodDecl(Id(area),Instance,[],FloatType,Block([VarDecl(Id(p),FloatType)],[AssignStmt(Id(p),CallExpr(Self(),Id(circumference),[])),Return(CallExpr(Id(Math),Id(sqrt),[BinaryOp(*,BinaryOp(*,BinaryOp(*,Id(p),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge1)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge2)))),BinaryOp(-,Id(p),FieldAccess(Self(),Id(edge3))))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(p1),ClassType(Id(Point))),VarDecl(Id(p2),ClassType(Id(Point))),VarDecl(Id(p3),ClassType(Id(Point))),VarDecl(Id(abc),ClassType(Id(Triangle))),VarDecl(Id(area),FloatType)],[AssignStmt(Id(p1),NewExpr(Id(Point),[IntLit(0),IntLit(0)])),AssignStmt(Id(p2),NewExpr(Id(Point),[IntLit(0),IntLit(1)])),AssignStmt(Id(p3),NewExpr(Id(Point),[IntLit(1),IntLit(0)])),AssignStmt(Id(abc),NewExpr(Id(Triangle),[Id(p1),Id(p2),Id(p3)])),AssignStmt(Id(area),CallExpr(Id(abc),Id(area),[])),Call(Id(io),Id(writeLn),[StringLit(Area of triangle: ),Id(area)])]))])])
---
testcase357:Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(Id(a),BinaryOp(||,BinaryOp(&&,BinaryOp(/,BinaryOp(*,BinaryOp(/,Id(b),IntLit(2)),Id(n)),IntLit(4)),BinaryOp(%,IntLit(5),Id(g))),BinaryOp(%,BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(9)),IntLit(4)),IntLit(2))))]))])])
---
testcase358:Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(Kori),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])],[AssignStmt(ArrayCell(Id(Kori),IntLit(5)),IntLit(7)),Call(Self(),Id(print),[Id(Kori),IntLit(0),IntLit(4)])]))])])
---
testcase359:Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Static,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Static,VarDecl(Id(c),IntType,IntLit(66))),AttributeDecl(Static,VarDecl(Id(d),IntType)),AttributeDecl(Static,VarDecl(Id(e),IntType)),AttributeDecl(Static,VarDecl(Id(f),IntType,IntLit(77))),AttributeDecl(Static,VarDecl(Id(g),IntType,IntLit(8))),AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id(c),IntType,IntLit(3)))])])
---
testcase360:Program([ClassDecl(Id(Employee),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(age),IntType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(a),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(name)),Id(n)),AssignStmt(FieldAccess(Self(),Id(age)),Id(a))])),MethodDecl(Id(display),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Employee Name: ),FieldAccess(Self(),Id(name)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Employee Age: ),FieldAccess(Self(),Id(age)))])]))])])
---
testcase361:Program([ClassDecl(Id(Manager),Id(Employee),[AttributeDecl(Instance,VarDecl(Id(department),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(a),IntType),param(Id(dept),StringType)],Block([],[Call(Self(),Id(Employee),[Id(n),Id(a)]),AssignStmt(FieldAccess(Self(),Id(department)),Id(dept))])),MethodDecl(Id(display),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Manager Name: ),FieldAccess(Self(),Id(name)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Manager Age: ),FieldAccess(Self(),Id(age)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Manager Department: ),FieldAccess(Self(),Id(department)))])]))])])
---
testcase362:Program([ClassDecl(Id(Developer),Id(Employee),[AttributeDecl(Instance,VarDecl(Id(programmingLanguage),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(a),IntType),param(Id(lang),StringType)],Block([],[Call(Self(),Id(Employee),[Id(n),Id(a)]),AssignStmt(FieldAccess(Self(),Id(programmingLanguage)),Id(lang))])),MethodDecl(Id(display),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Developer Name: ),FieldAccess(Self(),Id(name)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Developer Age: ),FieldAccess(Self(),Id(age)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Programming Language: ),FieldAccess(Self(),Id(programmingLanguage)))])]))])])
---
testcase363:Program([ClassDecl(Id(Test),[])])
---
testcase364:Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],VoidType,Block([VarDecl(Id(_str_),StringType),VarDecl(Id(o),StringType),VarDecl(Id(c),StringType)],[]))])])
---
testcase365:Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(Id(a),UnaryOp(+,Id(a)))]))])])
---
testcase366:Program([ClassDecl(Id(ABC),[])])
---
testcase367:Program([ClassDecl(Id(PPL),[AttributeDecl(Instance,VarDecl(Id(PPL),StringType,StringLit(Principles of Programming Languages))),AttributeDecl(Instance,VarDecl(Id(lecturer),StringType,StringLit(Dr. Nguyen Hua Phung))),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(con),StringType)],[AssignStmt(Id(con),BinaryOp(^,Id(lecturer),StringLit( - )))]))])])
---
testcase368:Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(||,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),IntLit(5))),IntLit(6)),IntLit(7)),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),BinaryOp(&&,BinaryOp(+,IntLit(4),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),Id(abc))),UnaryOp(!,IntLit(123))))),ArrayCell(Id(a),UnaryOp(-,IntLit(5))))]))])])
---
testcase369:Program([ClassDecl(Id(main),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3))),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])
---
testcase370:Program([ClassDecl(Id(main),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),IntLit(2)),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3))),Block([VarDecl(Id(r),FloatType),VarDecl(Id(s),FloatType),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType))],[AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),IntLit(0)),Id(s))]),Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])
---
testcase371:Program([ClassDecl(Id(a),[]),ClassDecl(Id(b),[MethodDecl(Id(bb),Instance,[],ClassType(Id(a)),Block([],[Continue,AssignStmt(ArrayCell(FieldAccess(Id(xxx),Id(xxx)),IntLit(2)),ArrayCell(CallExpr(Id(aaa),Id(aaa),[Id(a)]),Id(aaa)))]))])])
---
testcase372:Program([ClassDecl(Id(Vehicle),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Vehicle is moving.)])]))])])
---
testcase373:Program([ClassDecl(Id(Car),Id(Vehicle),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Car is driving on the road.)])]))])])
---
testcase374:Program([ClassDecl(Id(Bicycle),Id(Vehicle),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Bicycle is pedaling on the path.)])]))])])
---
testcase375:Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(vehicles),ArrayType(5,ClassType(Id(Vehicle))))],[AssignStmt(ArrayCell(Id(vehicles),IntLit(0)),NewExpr(Id(Vehicle),[])),AssignStmt(ArrayCell(Id(vehicles),IntLit(1)),NewExpr(Id(Car),[])),AssignStmt(ArrayCell(Id(vehicles),IntLit(2)),NewExpr(Id(Bicycle),[])),For(Id(v),IntLit(0),Id(vehicles),True,Block([],[Call(Id(v),Id(move),[])])])]))])])
---
testcase376:Program([ClassDecl(Id(Vehicle),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Vehicle is moving.)])]))]),ClassDecl(Id(Car),Id(Vehicle),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Car is driving on the road.)])]))]),ClassDecl(Id(Bicycle),Id(Vehicle),[MethodDecl(Id(move),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Bicycle is pedaling on the path.)])]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(vehicles),ArrayType(5,ClassType(Id(Vehicle))))],[AssignStmt(ArrayCell(Id(vehicles),IntLit(0)),NewExpr(Id(Vehicle),[])),AssignStmt(ArrayCell(Id(vehicles),IntLit(1)),NewExpr(Id(Car),[])),AssignStmt(ArrayCell(Id(vehicles),IntLit(2)),NewExpr(Id(Bicycle),[])),For(Id(v),IntLit(0),Id(vehicles),True,Block([],[Call(Id(v),Id(move),[])])])]))])])
---
testcase377:Program([ClassDecl(Id(Character),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(level),IntType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(l),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(name)),Id(n)),AssignStmt(FieldAccess(Self(),Id(level)),Id(l))])),MethodDecl(Id(displayInfo),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Name: ),FieldAccess(Self(),Id(name)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Level: ),FieldAccess(Self(),Id(level)))])]))])])
---
testcase378:Program([ClassDecl(Id(Warrior),Id(Character),[AttributeDecl(Instance,VarDecl(Id(weapon),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(l),IntType),param(Id(w),IntType)],Block([],[Call(Self(),Id(Character),[Id(n),Id(l)]),AssignStmt(FieldAccess(Self(),Id(weapon)),Id(w))])),MethodDecl(Id(displayInfo),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Warrior:)]),Call(FieldAccess(Self(),Id(Character)),Id(displayInfo),[]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Weapon: ),FieldAccess(Self(),Id(weapon)))])]))])])
---
testcase379:Program([ClassDecl(Id(Mage),Id(Character),[AttributeDecl(Instance,VarDecl(Id(spell),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(l),IntType),param(Id(s),IntType)],Block([],[Call(Self(),Id(Character),[Id(n),Id(l)]),AssignStmt(FieldAccess(Self(),Id(spell)),Id(s))])),MethodDecl(Id(displayInfo),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Mage:)]),Call(FieldAccess(Self(),Id(Character)),Id(displayInfo),[]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Spell: ),FieldAccess(Self(),Id(spell)))])]))])])
---
testcase380:Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(warrior),ClassType(Id(Warrior)),NewExpr(Id(Warrior),[StringLit(Conan),IntLit(25),StringLit(Greatsword)])),VarDecl(Id(mage),ClassType(Id(Mage)),NewExpr(Id(Mage),[StringLit(Gandalf),IntLit(30),StringLit(Fireball)])),VarDecl(Id(characters),ArrayType(2,ClassType(Id(Character))))],[AssignStmt(ArrayCell(Id(characters),IntLit(0)),Id(warrior)),AssignStmt(ArrayCell(Id(characters),IntLit(1)),Id(mage)),For(Id(c),Id(lemgth),Id(characters),False,Block([],[Call(Id(c),Id(displayInfo),[]),Call(Id(io),Id(writeStrLn),[])])])]))])])
---
testcase381:Program([ClassDecl(Id(Character),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(level),IntType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(l),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(name)),Id(n)),AssignStmt(FieldAccess(Self(),Id(level)),Id(l))])),MethodDecl(Id(displayInfo),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Name: ),FieldAccess(Self(),Id(name)))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Level: ),FieldAccess(Self(),Id(level)))])]))]),ClassDecl(Id(Warrior),Id(Character),[AttributeDecl(Instance,VarDecl(Id(weapon),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(l),IntType),param(Id(w),IntType)],Block([],[Call(Self(),Id(Character),[Id(n),Id(l)]),AssignStmt(FieldAccess(Self(),Id(weapon)),Id(w))])),MethodDecl(Id(displayInfo),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Warrior:)]),Call(FieldAccess(Self(),Id(Character)),Id(displayInfo),[]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Weapon: ),FieldAccess(Self(),Id(weapon)))])]))]),ClassDecl(Id(Mage),Id(Character),[AttributeDecl(Instance,VarDecl(Id(spell),StringType)),MethodDecl(Id(<init>),Instance,[param(Id(n),StringType),param(Id(l),IntType),param(Id(s),IntType)],Block([],[Call(Self(),Id(Character),[Id(n),Id(l)]),AssignStmt(FieldAccess(Self(),Id(spell)),Id(s))])),MethodDecl(Id(displayInfo),Instance,[],VoidType,Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Mage:)]),Call(FieldAccess(Self(),Id(Character)),Id(displayInfo),[]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Spell: ),FieldAccess(Self(),Id(spell)))])]))]),ClassDecl(Id(Test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(warrior),ClassType(Id(Warrior)),NewExpr(Id(Warrior),[StringLit(Conan),IntLit(25),StringLit(Greatsword)])),VarDecl(Id(mage),ClassType(Id(Mage)),NewExpr(Id(Mage),[StringLit(Gandalf),IntLit(30),StringLit(Fireball)])),VarDecl(Id(characters),ArrayType(2,ClassType(Id(Character))))],[AssignStmt(ArrayCell(Id(characters),IntLit(0)),Id(warrior)),AssignStmt(ArrayCell(Id(characters),IntLit(1)),Id(mage)),For(Id(c),IntLit(0),Id(characters),True,Block([],[Call(Id(c),Id(displayInfo),[]),Call(Id(io),Id(writeStrLn),[])])])]))])])
---
testcase382:Program([ClassDecl(Id(MergeSort),[MethodDecl(Id(merge),Instance,[param(Id(left),IntType),param(Id(middle),IntType),param(Id(right),IntType)],VoidType,Block([VarDecl(Id(n1),IntType,BinaryOp(+,BinaryOp(-,Id(middle),Id(left)),IntLit(1))),VarDecl(Id(n2),IntType,BinaryOp(-,Id(right),Id(middle))),VarDecl(Id(leftArray),ArrayType(0,IntType)),VarDecl(Id(rightArray),ArrayType(0,IntType))],[For(Id(i),IntLit(0),BinaryOp(-,Id(n1),IntLit(1)),True,AssignStmt(ArrayCell(Id(leftArray),Id(i)),ArrayCell(Id(arr),BinaryOp(+,Id(left),Id(i))))]),For(Id(j),IntLit(0),BinaryOp(-,Id(n2),IntLit(1)),True,AssignStmt(ArrayCell(Id(rightArray),Id(j)),ArrayCell(Id(arr),BinaryOp(+,BinaryOp(+,Id(middle),IntLit(1)),Id(j))))]),AssignStmt(Id(i),IntLit(0)),AssignStmt(Id(j),IntLit(0)),AssignStmt(Id(k),Id(left)),For(Id(k),Id(left),Id(right),True,Block([],[If(BinaryOp(<,Id(i),BinaryOp(&&,Id(n1),BinaryOp(||,BinaryOp(>=,Id(j),Id(n2)),BinaryOp(<=,ArrayCell(Id(leftArray),Id(i)),ArrayCell(Id(rightArray),Id(j)))))),Block([],[AssignStmt(ArrayCell(Id(arr),Id(k)),ArrayCell(Id(leftArray),Id(i))),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]),Block([],[AssignStmt(ArrayCell(Id(arr),Id(k)),ArrayCell(Id(rightArray),Id(j))),AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))]))])])])),MethodDecl(Id(mergeSort),Instance,[param(Id(left),IntType),param(Id(right),IntType)],VoidType,Block([],[If(BinaryOp(<,Id(left),Id(right)),Block([VarDecl(Id(middle),IntType,BinaryOp(+,Id(left),BinaryOp(/,BinaryOp(-,Id(right),Id(left)),IntLit(2))))],[Call(Self(),Id(mergeSort),[Id(arr),Id(left),Id(middle)]),Call(Self(),Id(mergeSort),[Id(arr),BinaryOp(+,Id(middle),IntLit(1)),Id(right)]),Call(Self(),Id(merge),[Id(arr),Id(left),Id(middle),Id(right)])]))]))])])
---
testcase383:Program([ClassDecl(Id(TestMergeSort),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(numbers),ArrayType(10,IntType),[IntLit(5),IntLit(2),IntLit(8),IntLit(1),IntLit(9),IntLit(3),IntLit(7),IntLit(4),IntLit(6),IntLit(0)]),VarDecl(Id(sorter),ClassType(Id(MergeSort)),NewExpr(Id(MergeSort),[]))],[Call(Id(sorter),Id(mergeSort),[Id(numbers),IntLit(0),BinaryOp(-,FieldAccess(Id(numbers),Id(length)),IntLit(1))]),Call(Id(io),Id(writeStrLn),[StringLit(Sorted Array:)]),For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(Id(numbers),Id(length)),IntLit(1)),True,Block([],[Call(Id(io),Id(writeInt),[ArrayCell(Id(numbers),Id(i))]),Call(Id(io),Id(writeChar),[StringLit( )])])])]))])])
---
testcase384:Program([ClassDecl(Id(BubbleSort),[MethodDecl(Id(sort),Instance,[param(Id(arr),ArrayType(10,IntType))],VoidType,Block([VarDecl(Id(temp),IntType)],[For(Id(i),IntLit(0),BinaryOp(-,Id(length),IntLit(2)),True,Block([],[For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,Id(length),IntLit(2)),Id(i)),True,Block([],[If(BinaryOp(>,ArrayCell(Id(arr),Id(j)),ArrayCell(Id(arr),BinaryOp(+,Id(j),IntLit(1)))),Block([],[AssignStmt(Id(temp),ArrayCell(Id(arr),Id(j))),AssignStmt(ArrayCell(Id(arr),Id(j)),ArrayCell(Id(arr),BinaryOp(+,Id(j),IntLit(1)))),AssignStmt(ArrayCell(Id(arr),BinaryOp(+,Id(j),IntLit(1))),Id(temp))]))])])])])])),MethodDecl(Id(printArray),Instance,[param(Id(arr),ArrayType(10,IntType))],VoidType,Block([],[For(Id(i),IntLit(0),BinaryOp(-,Id(length),IntLit(1)),True,Block([],[Call(Id(io),Id(writeInt),[ArrayCell(Id(arr),Id(i))]),Call(Id(io),Id(writeChar),[StringLit( )])])])]))])])
---
testcase385:Program([ClassDecl(Id(TestBubbleSort),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(array),ArrayType(7,IntType),[IntLit(64),IntLit(34),IntLit(25),IntLit(12),IntLit(22),IntLit(11),IntLit(90)]),VarDecl(Id(sorter),ClassType(Id(BubbleSort)),NewExpr(Id(BubbleSort),[]))],[Call(Id(io),Id(writeStrLn),[StringLit(Original array:)]),Call(Id(sorter),Id(printArray),[Id(array)]),Call(Id(io),Id(writeStrLn),[StringLit(\\nSorted array:)]),Call(Id(sorter),Id(sort),[Id(array)]),Call(Id(sorter),Id(printArray),[Id(array)])]))])])
---
testcase386:Program([ClassDecl(Id(MergeSort),[MethodDecl(Id(merge),Instance,[param(Id(left),IntType),param(Id(middle),IntType),param(Id(right),IntType)],VoidType,Block([VarDecl(Id(n1),IntType,BinaryOp(+,BinaryOp(-,Id(middle),Id(left)),IntLit(1))),VarDecl(Id(n2),IntType,BinaryOp(-,Id(right),Id(middle))),VarDecl(Id(leftArray),ArrayType(0,IntType)),VarDecl(Id(rightArray),ArrayType(0,IntType))],[For(Id(i),IntLit(0),BinaryOp(-,Id(n1),IntLit(1)),True,AssignStmt(ArrayCell(Id(leftArray),Id(i)),ArrayCell(Id(arr),BinaryOp(+,Id(left),Id(i))))]),For(Id(j),IntLit(0),BinaryOp(-,Id(n2),IntLit(1)),True,AssignStmt(ArrayCell(Id(rightArray),Id(j)),ArrayCell(Id(arr),BinaryOp(+,BinaryOp(+,Id(middle),IntLit(1)),Id(j))))]),AssignStmt(Id(i),IntLit(0)),AssignStmt(Id(j),IntLit(0)),AssignStmt(Id(k),Id(left)),For(Id(k),Id(left),Id(right),True,Block([],[If(BinaryOp(<,Id(i),BinaryOp(&&,Id(n1),BinaryOp(||,BinaryOp(>=,Id(j),Id(n2)),BinaryOp(<=,ArrayCell(Id(leftArray),Id(i)),ArrayCell(Id(rightArray),Id(j)))))),Block([],[AssignStmt(ArrayCell(Id(arr),Id(k)),ArrayCell(Id(leftArray),Id(i))),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]),Block([],[AssignStmt(ArrayCell(Id(arr),Id(k)),ArrayCell(Id(rightArray),Id(j))),AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))]))])])])),MethodDecl(Id(mergeSort),Instance,[param(Id(left),IntType),param(Id(right),IntType)],VoidType,Block([],[If(BinaryOp(<,Id(left),Id(right)),Block([VarDecl(Id(middle),IntType,BinaryOp(+,Id(left),BinaryOp(/,BinaryOp(-,Id(right),Id(left)),IntLit(2))))],[Call(Self(),Id(mergeSort),[Id(arr),Id(left),Id(middle)]),Call(Self(),Id(mergeSort),[Id(arr),BinaryOp(+,Id(middle),IntLit(1)),Id(right)]),Call(Self(),Id(merge),[Id(arr),Id(left),Id(middle),Id(right)])]))]))]),ClassDecl(Id(TestMergeSort),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(numbers),ArrayType(10,IntType),[IntLit(5),IntLit(2),IntLit(8),IntLit(1),IntLit(9),IntLit(3),IntLit(7),IntLit(4),IntLit(6),IntLit(0)]),VarDecl(Id(sorter),ClassType(Id(MergeSort)),NewExpr(Id(MergeSort),[]))],[Call(Id(sorter),Id(mergeSort),[Id(numbers),IntLit(0),BinaryOp(-,FieldAccess(Id(numbers),Id(length)),IntLit(1))]),Call(Id(io),Id(writeStrLn),[StringLit(Sorted Array:)]),For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(Id(numbers),Id(length)),IntLit(1)),True,Block([],[Call(Id(io),Id(writeInt),[ArrayCell(Id(numbers),Id(i))]),Call(Id(io),Id(writeChar),[StringLit( )])])])]))])])
---
testcase387:Program([ClassDecl(Id(BubbleSort),[MethodDecl(Id(sort),Instance,[param(Id(arr),ArrayType(10,IntType))],VoidType,Block([VarDecl(Id(temp),IntType)],[For(Id(i),IntLit(0),BinaryOp(-,Id(length),IntLit(2)),True,Block([],[For(Id(j),IntLit(0),BinaryOp(-,BinaryOp(-,Id(length),IntLit(2)),Id(i)),True,Block([],[If(BinaryOp(>,ArrayCell(Id(arr),Id(j)),ArrayCell(Id(arr),BinaryOp(+,Id(j),IntLit(1)))),Block([],[AssignStmt(Id(temp),ArrayCell(Id(arr),Id(j))),AssignStmt(ArrayCell(Id(arr),Id(j)),ArrayCell(Id(arr),BinaryOp(+,Id(j),IntLit(1)))),AssignStmt(ArrayCell(Id(arr),BinaryOp(+,Id(j),IntLit(1))),Id(temp))]))])])])])])),MethodDecl(Id(printArray),Instance,[param(Id(arr),ArrayType(10,IntType))],VoidType,Block([],[For(Id(i),IntLit(0),BinaryOp(-,Id(length),IntLit(1)),True,Block([],[Call(Id(io),Id(writeInt),[ArrayCell(Id(arr),Id(i))]),Call(Id(io),Id(writeChar),[StringLit( )])])])]))]),ClassDecl(Id(TestBubbleSort),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(array),ArrayType(7,IntType),[IntLit(64),IntLit(34),IntLit(25),IntLit(12),IntLit(22),IntLit(11),IntLit(90)]),VarDecl(Id(sorter),ClassType(Id(BubbleSort)),NewExpr(Id(BubbleSort),[]))],[Call(Id(io),Id(writeStrLn),[StringLit(Original array:)]),Call(Id(sorter),Id(printArray),[Id(array)]),Call(Id(io),Id(writeStrLn),[StringLit(\\nSorted array:)]),Call(Id(sorter),Id(sort),[Id(array)]),Call(Id(sorter),Id(printArray),[Id(array)])]))])])
---
testcase388:Program([ClassDecl(Id(BinarySearch),[MethodDecl(Id(search),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(target),IntType),param(Id(low),IntType),param(Id(high),IntType)],IntType,Block([VarDecl(Id(mid),IntType)],[If(BinaryOp(>,Id(low),Id(high)),Return(UnaryOp(-,IntLit(1)))),AssignStmt(Id(mid),BinaryOp(/,BinaryOp(+,Id(low),Id(high)),IntLit(2))),If(BinaryOp(==,ArrayCell(Id(arr),Id(mid)),Id(target)),Return(Id(mid)),If(BinaryOp(>,ArrayCell(Id(arr),Id(mid)),Id(target)),Return(CallExpr(Self(),Id(search),[Id(arr),Id(target),Id(low),BinaryOp(-,Id(mid),IntLit(1))])),Return(CallExpr(Self(),Id(search),[Id(arr),Id(target),BinaryOp(+,Id(mid),IntLit(1)),Id(high)]))))]))])])
---
testcase389:Program([ClassDecl(Id(TestBinarySearch),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(sortedArray),ArrayType(10,IntType),[IntLit(2),IntLit(5),IntLit(8),IntLit(12),IntLit(16),IntLit(23),IntLit(38),IntLit(56),IntLit(72),IntLit(91)]),VarDecl(Id(target),IntType,IntLit(23)),VarDecl(Id(searchAlgorithm),ClassType(Id(BinarySearch)),NewExpr(Id(BinarySearch),[])),VarDecl(Id(result),IntType,CallExpr(Id(searchAlgorithm),Id(search),[Id(sortedArray),Id(target),IntLit(0),BinaryOp(-,FieldAccess(Id(sortedArray),Id(length)),IntLit(1))]))],[If(BinaryOp(!=,Id(result),UnaryOp(-,IntLit(1))),Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Element ),Id(target)),StringLit( found at index )),Id(result))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,StringLit(Element ),Id(target)),StringLit( not found in the array))]))]))])])
---
testcase390:Program([ClassDecl(Id(BinarySearch),[MethodDecl(Id(search),Instance,[param(Id(arr),ArrayType(10,IntType)),param(Id(target),IntType),param(Id(low),IntType),param(Id(high),IntType)],IntType,Block([VarDecl(Id(mid),IntType)],[If(BinaryOp(>,Id(low),Id(high)),Return(UnaryOp(-,IntLit(1)))),AssignStmt(Id(mid),BinaryOp(/,BinaryOp(+,Id(low),Id(high)),IntLit(2))),If(BinaryOp(==,ArrayCell(Id(arr),Id(mid)),Id(target)),Return(Id(mid)),If(BinaryOp(>,ArrayCell(Id(arr),Id(mid)),Id(target)),Return(CallExpr(Self(),Id(search),[Id(arr),Id(target),Id(low),BinaryOp(-,Id(mid),IntLit(1))])),Return(CallExpr(Self(),Id(search),[Id(arr),Id(target),BinaryOp(+,Id(mid),IntLit(1)),Id(high)]))))]))]),ClassDecl(Id(TestBinarySearch),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(sortedArray),ArrayType(10,IntType),[IntLit(2),IntLit(5),IntLit(8),IntLit(12),IntLit(16),IntLit(23),IntLit(38),IntLit(56),IntLit(72),IntLit(91)]),VarDecl(Id(target),IntType,IntLit(23)),VarDecl(Id(searchAlgorithm),ClassType(Id(BinarySearch)),NewExpr(Id(BinarySearch),[])),VarDecl(Id(result),IntType,CallExpr(Id(searchAlgorithm),Id(search),[Id(sortedArray),Id(target),IntLit(0),BinaryOp(-,FieldAccess(Id(sortedArray),Id(length)),IntLit(1))]))],[If(BinaryOp(!=,Id(result),UnaryOp(-,IntLit(1))),Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Element ),Id(target)),StringLit( found at index )),Id(result))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,StringLit(Element ),Id(target)),StringLit( not found in the array))]))]))])])
---
testcase391:Program([ClassDecl(Id(Account),[AttributeDecl(Instance,VarDecl(Id(accountNumber),IntType)),AttributeDecl(Instance,VarDecl(Id(balance),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(number),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(accountNumber)),Id(number)),AssignStmt(FieldAccess(Self(),Id(balance)),FloatLit(0.0))])),MethodDecl(Id(deposit),Instance,[param(Id(amount),FloatType)],VoidType,Block([],[AssignStmt(FieldAccess(Self(),Id(balance)),BinaryOp(+,FieldAccess(Self(),Id(balance)),Id(amount)))])),MethodDecl(Id(withdraw),Instance,[param(Id(amount),FloatType)],VoidType,Block([],[If(BinaryOp(<=,Id(amount),FieldAccess(Self(),Id(balance))),AssignStmt(FieldAccess(Self(),Id(balance)),BinaryOp(-,FieldAccess(Self(),Id(balance)),Id(amount))))])),MethodDecl(Id(getBalance),Instance,[],FloatType,Block([],[Return(FieldAccess(Self(),Id(balance)))]))])])
---
testcase392:Program([ClassDecl(Id(SavingsAccount),Id(Account),[AttributeDecl(Instance,VarDecl(Id(interestRate),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(number),IntType),param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Account),[Id(number)]),AssignStmt(FieldAccess(Self(),Id(interestRate)),Id(rate))])),MethodDecl(Id(applyInterest),Instance,[],VoidType,Block([VarDecl(Id(interest),FloatType,BinaryOp(*,FieldAccess(Self(),Id(balance)),FieldAccess(Self(),Id(interestRate))))],[Call(Self(),Id(deposit),[Id(interest)])]))])])
---
testcase393:Program([ClassDecl(Id(CheckingAccount),Id(Account),[AttributeDecl(Instance,VarDecl(Id(overdraftLimit),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(number),IntType),param(Id(limit),FloatType)],Block([],[Call(Self(),Id(Account),[Id(number)]),AssignStmt(FieldAccess(Self(),Id(overdraftLimit)),Id(limit))])),MethodDecl(Id(withdraw),Instance,[param(Id(amount),FloatType)],VoidType,Block([],[If(BinaryOp(<=,Id(amount),BinaryOp(+,FieldAccess(Self(),Id(balance)),FieldAccess(Self(),Id(overdraftLimit)))),AssignStmt(FieldAccess(Self(),Id(balance)),BinaryOp(-,FieldAccess(Self(),Id(balance)),Id(amount))))]))])])
---
testcase394:Program([ClassDecl(Id(Bank),[AttributeDecl(Instance,VarDecl(Id(accounts),ArrayType(10,ClassType(Id(Account))))),MethodDecl(Id(<init>),Instance,[param(Id(numAccounts),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(accounts)),NewExpr(Id(Account),[])),For(Id(i),IntLit(0),BinaryOp(-,Id(numAccounts),IntLit(1)),True,If(BinaryOp(==,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),NewExpr(Id(SavingsAccount),[Id(i),FloatLit(0.05)])),AssignStmt(ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),NewExpr(Id(CheckingAccount),[Id(i),FloatLit(500.0)])))])])),MethodDecl(Id(simulateTransactions),Instance,[],VoidType,Block([],[For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(FieldAccess(Self(),Id(accounts)),Id(length)),IntLit(1)),True,If(BinaryOp(==,ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),Id(SavingsAccount)),Block([VarDecl(Id(sa),ClassType(Id(SavingsAccount)),ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)))],[Call(Id(sa),Id(deposit),[FloatLit(100.0)]),Call(Id(sa),Id(applyInterest),[])]),Block([VarDecl(Id(ca),ClassType(Id(CheckingAccount)),ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)))],[Call(Id(ca),Id(deposit),[FloatLit(200.0)]),Call(Id(ca),Id(withdraw),[FloatLit(300.0)])]))])])),MethodDecl(Id(printAccountBalances),Instance,[],VoidType,Block([],[For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(FieldAccess(Self(),Id(accounts)),Id(length)),IntLit(1)),True,Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Account ),Id(i)),StringLit( Balance: )),CallExpr(ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),Id(getBalance),[]))])])]))])])
---
testcase395:Program([ClassDecl(Id(TestBank),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(bank),ClassType(Id(Bank)),NewExpr(Id(Bank),[IntLit(10)]))],[Call(Id(bank),Id(simulateTransactions),[]),Call(Id(bank),Id(printAccountBalances),[])]))])])
---
testcase396:Program([ClassDecl(Id(Account),[AttributeDecl(Instance,VarDecl(Id(accountNumber),IntType)),AttributeDecl(Instance,VarDecl(Id(balance),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(number),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(accountNumber)),Id(number)),AssignStmt(FieldAccess(Self(),Id(balance)),FloatLit(0.0))])),MethodDecl(Id(deposit),Instance,[param(Id(amount),FloatType)],VoidType,Block([],[AssignStmt(FieldAccess(Self(),Id(balance)),BinaryOp(+,FieldAccess(Self(),Id(balance)),Id(amount)))])),MethodDecl(Id(withdraw),Instance,[param(Id(amount),FloatType)],VoidType,Block([],[If(BinaryOp(<=,Id(amount),FieldAccess(Self(),Id(balance))),AssignStmt(FieldAccess(Self(),Id(balance)),BinaryOp(-,FieldAccess(Self(),Id(balance)),Id(amount))))])),MethodDecl(Id(getBalance),Instance,[],FloatType,Block([],[Return(FieldAccess(Self(),Id(balance)))]))]),ClassDecl(Id(SavingsAccount),Id(Account),[AttributeDecl(Instance,VarDecl(Id(interestRate),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(number),IntType),param(Id(rate),FloatType)],Block([],[Call(Self(),Id(Account),[Id(number)]),AssignStmt(FieldAccess(Self(),Id(interestRate)),Id(rate))])),MethodDecl(Id(applyInterest),Instance,[],VoidType,Block([VarDecl(Id(interest),FloatType,BinaryOp(*,FieldAccess(Self(),Id(balance)),FieldAccess(Self(),Id(interestRate))))],[Call(Self(),Id(deposit),[Id(interest)])]))]),ClassDecl(Id(CheckingAccount),Id(Account),[AttributeDecl(Instance,VarDecl(Id(overdraftLimit),FloatType)),MethodDecl(Id(<init>),Instance,[param(Id(number),IntType),param(Id(limit),FloatType)],Block([],[Call(Self(),Id(Account),[Id(number)]),AssignStmt(FieldAccess(Self(),Id(overdraftLimit)),Id(limit))])),MethodDecl(Id(withdraw),Instance,[param(Id(amount),FloatType)],VoidType,Block([],[If(BinaryOp(<=,Id(amount),BinaryOp(+,FieldAccess(Self(),Id(balance)),FieldAccess(Self(),Id(overdraftLimit)))),AssignStmt(FieldAccess(Self(),Id(balance)),BinaryOp(-,FieldAccess(Self(),Id(balance)),Id(amount))))]))]),ClassDecl(Id(Bank),[AttributeDecl(Instance,VarDecl(Id(accounts),ArrayType(10,ClassType(Id(Account))))),MethodDecl(Id(<init>),Instance,[param(Id(numAccounts),IntType)],Block([],[AssignStmt(FieldAccess(Self(),Id(accounts)),NewExpr(Id(Account),[])),For(Id(i),IntLit(0),BinaryOp(-,Id(numAccounts),IntLit(1)),True,If(BinaryOp(==,BinaryOp(%,Id(i),IntLit(2)),IntLit(0)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),NewExpr(Id(SavingsAccount),[Id(i),FloatLit(0.05)])),AssignStmt(ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),NewExpr(Id(CheckingAccount),[Id(i),FloatLit(500.0)])))])])),MethodDecl(Id(simulateTransactions),Instance,[],VoidType,Block([],[For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(FieldAccess(Self(),Id(accounts)),Id(length)),IntLit(1)),True,If(BinaryOp(==,ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),Id(SavingsAccount)),Block([VarDecl(Id(sa),ClassType(Id(SavingsAccount)),ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)))],[Call(Id(sa),Id(deposit),[FloatLit(100.0)]),Call(Id(sa),Id(applyInterest),[])]),Block([VarDecl(Id(ca),ClassType(Id(CheckingAccount)),ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)))],[Call(Id(ca),Id(deposit),[FloatLit(200.0)]),Call(Id(ca),Id(withdraw),[FloatLit(300.0)])]))])])),MethodDecl(Id(printAccountBalances),Instance,[],VoidType,Block([],[For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(FieldAccess(Self(),Id(accounts)),Id(length)),IntLit(1)),True,Call(Id(io),Id(writeStrLn),[BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(Account ),Id(i)),StringLit( Balance: )),CallExpr(ArrayCell(FieldAccess(Self(),Id(accounts)),Id(i)),Id(getBalance),[]))])])]))]),ClassDecl(Id(TestBank),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(bank),ClassType(Id(Bank)),NewExpr(Id(Bank),[IntLit(10)]))],[Call(Id(bank),Id(simulateTransactions),[]),Call(Id(bank),Id(printAccountBalances),[])]))])])
---
testcase397:Program([ClassDecl(Id(OperatorTest),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Block([VarDecl(Id(a),IntType,IntLit(10)),VarDecl(Id(b),IntType,IntLit(20)),VarDecl(Id(x),FloatType,FloatLit(15.5)),VarDecl(Id(condition),BoolType,BooleanLit(True)),VarDecl(Id(result1),IntType,BinaryOp(/,BinaryOp(*,BinaryOp(+,Id(a),Id(b)),BinaryOp(-,Id(b),Id(a))),IntLit(2))),VarDecl(Id(result2),FloatType,BinaryOp(/,BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(x)),BinaryOp(-,Id(x),Id(b)))),VarDecl(Id(result3),BoolType,BinaryOp(||,BinaryOp(&&,BinaryOp(<,Id(a),Id(b)),BinaryOp(>=,Id(x),Id(a))),Id(condition)))],[Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result 1: ),Id(result1))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result 2: ),Id(result2))]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Result 3: ),Id(result3))])]),Block([VarDecl(Id(numbers),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]),VarDecl(Id(sum),IntType,IntLit(0))],[For(Id(i),IntLit(0),BinaryOp(-,FieldAccess(Id(numbers),Id(length)),IntLit(1)),True,Block([],[AssignStmt(Id(sum),BinaryOp(+,Id(sum),ArrayCell(Id(numbers),Id(i))))])]),If(BinaryOp(==,BinaryOp(%,Id(sum),IntLit(2)),IntLit(0)),Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Sum of numbers is even.)])]),Block([],[Call(Id(io),Id(writeStrLn),[StringLit(Sum of numbers is odd.)])]))])]))])])
---
testcase398:Program([ClassDecl(Id(SuperComplexTest),[MethodDecl(Id(customPower),Static,[param(Id(base),FloatType),param(Id(exponent),IntType)],FloatType,Block([],[If(BinaryOp(==,Id(exponent),IntLit(0)),Block([],[Return(IntLit(1))]),If(BinaryOp(==,BinaryOp(%,Id(exponent),IntLit(2)),IntLit(0)),Block([VarDecl(Id(temp),FloatType,CallExpr(Self(),Id(customPower),[Id(base),BinaryOp(/,Id(exponent),IntLit(2))]))],[Return(BinaryOp(*,Id(temp),Id(temp)))]),Block([VarDecl(Id(temp),FloatType,CallExpr(Self(),Id(customPower),[Id(base),BinaryOp(/,BinaryOp(-,Id(exponent),IntLit(1)),IntLit(2))]))],[Return(BinaryOp(*,BinaryOp(*,Id(base),Id(temp)),Id(temp)))])))])),MethodDecl(Id(fibonacci),Static,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(<=,Id(n),IntLit(1)),Block([],[Return(Id(n))]),Block([],[Return(BinaryOp(+,CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(n),IntLit(1))]),CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(n),IntLit(2))])))]))])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(sum),FloatType,IntLit(0)),VarDecl(Id(finalValue),IntType,IntLit(0))],[For(Id(i),IntLit(1),IntLit(10),True,Block([VarDecl(Id(factorial),IntType,IntLit(1)),VarDecl(Id(fibonacciSum),IntType,IntLit(0))],[For(Id(j),IntLit(1),Id(i),True,Block([],[AssignStmt(Id(factorial),BinaryOp(*,Id(factorial),Id(j))),AssignStmt(Id(fibonacciSum),BinaryOp(+,Id(fibonacciSum),CallExpr(Self(),Id(fibonacci),[Id(j)])))])]),Block([VarDecl(Id(customPowerResult),FloatType,CallExpr(Self(),Id(customPower),[Id(factorial),Id(i)]))],[AssignStmt(Id(sum),BinaryOp(+,Id(sum),BinaryOp(*,Id(customPowerResult),Id(fibonacciSum))))])])]),For(Id(k),IntLit(1),IntLit(5),True,Block([],[If(BinaryOp(==,BinaryOp(%,Id(k),IntLit(2)),IntLit(0)),Block([],[AssignStmt(Id(finalValue),BinaryOp(+,BinaryOp(+,Id(finalValue),CallExpr(Self(),Id(customPower),[Id(sum),Id(k)])),Id(k)))]),Block([],[AssignStmt(Id(finalValue),BinaryOp(-,BinaryOp(-,Id(finalValue),CallExpr(Self(),Id(customPower),[Id(sum),Id(k)])),Id(k)))]))])]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Final Value: ),Id(finalValue))])]))])])
---
testcase399:Program([ClassDecl(Id(UltraComplexTest),[MethodDecl(Id(factorial),Static,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(<=,Id(n),IntLit(1)),Block([],[Return(IntLit(1))]),Block([],[Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))])))]))])),MethodDecl(Id(gcd),Static,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[If(BinaryOp(==,Id(b),IntLit(0)),Block([],[Return(Id(a))]),Block([],[Return(CallExpr(Self(),Id(gcd),[Id(b),BinaryOp(%,Id(a),Id(b))]))]))])),MethodDecl(Id(computeSeries),Static,[param(Id(x),IntType)],FloatType,Block([VarDecl(Id(result),FloatType,IntLit(0))],[For(Id(i),IntLit(1),IntLit(10),True,Block([],[AssignStmt(Id(result),BinaryOp(+,Id(result),BinaryOp(/,CallExpr(Self(),Id(customPower),[Id(x),Id(i)]),CallExpr(Self(),Id(factorial),[Id(i)]))))])]),Return(Id(result))])),MethodDecl(Id(customPower),Static,[param(Id(base),FloatType),param(Id(exponent),IntType)],FloatType,Block([],[If(BinaryOp(==,Id(exponent),IntLit(0)),Block([],[Return(IntLit(1))]),If(BinaryOp(==,BinaryOp(%,Id(exponent),IntLit(2)),IntLit(0)),Block([VarDecl(Id(temp),FloatType,CallExpr(Self(),Id(customPower),[Id(base),BinaryOp(/,Id(exponent),IntLit(2))]))],[Return(BinaryOp(*,Id(temp),Id(temp)))]),Block([VarDecl(Id(temp),FloatType,CallExpr(Self(),Id(customPower),[Id(base),BinaryOp(/,BinaryOp(-,Id(exponent),IntLit(1)),IntLit(2))]))],[Return(BinaryOp(*,BinaryOp(*,Id(base),Id(temp)),Id(temp)))])))])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(finalResult),IntType,IntLit(0))],[For(Id(a),IntLit(1),IntLit(5),True,Block([],[For(Id(b),IntLit(1),IntLit(5),True,Block([],[If(BinaryOp(!=,Id(a),Id(b)),Block([],[For(Id(c),IntLit(1),IntLit(5),True,Block([],[For(Id(d),IntLit(1),IntLit(5),True,Block([],[If(BinaryOp(!=,Id(c),Id(d)),Block([VarDecl(Id(gcdValue),IntType,CallExpr(Self(),Id(gcd),[BinaryOp(*,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d))])),VarDecl(Id(sum),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),Id(d))),VarDecl(Id(seriesResult),FloatType,CallExpr(Self(),Id(computeSeries),[Id(sum)]))],[If(BinaryOp(==,BinaryOp(%,Id(gcdValue),IntLit(2)),IntLit(0)),Block([],[AssignStmt(Id(finalResult),BinaryOp(+,Id(finalResult),BinaryOp(*,Id(seriesResult),Id(gcdValue))))]),Block([],[AssignStmt(Id(finalResult),BinaryOp(-,Id(finalResult),BinaryOp(/,Id(seriesResult),Id(gcdValue))))]))]))])])])])]))])])])]),Call(Id(io),Id(writeStrLn),[BinaryOp(^,StringLit(Final Result: ),Id(finalResult))])]))])])
---
"""









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