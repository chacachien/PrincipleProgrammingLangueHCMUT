import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """class Math{
    static int max(int a; int b) {
        if (a > b) then return a;
        else return b;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """class Circle extends Shape {
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
    static void main() {
        Shape c = new Circle();
        Shape s = new Square();
        float area1 = c.getArea();
        float area2 = s.getArea();
        io.writeStrLn("Area of Circle: " ^ area1);
        io.writeStrLn("Area of Square: " ^ area2);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """class Shape {
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
    static void main() {
        Circle c = new Circle(5.0, 5.0);
        float area = c.getArea();
        io.writeStrLn("Area of Circle: " ^ area);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test313(self):
        """Miss ) int main( {}"""
        input = """class Test{
    int factorial(int n) {
        if (n <= 1) then
            return 1;
        else
            return n * factorial(n - 1);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))