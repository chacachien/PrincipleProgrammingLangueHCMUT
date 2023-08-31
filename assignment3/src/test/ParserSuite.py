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
    
    def test_wrong_miss_close83(self):
        """Miss ) int main( {}"""
        input = """class SuperComplexTest {
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
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test313(self):
        """Miss ) int main( {}"""
        input = """
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
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))