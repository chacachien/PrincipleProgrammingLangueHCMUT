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
        input = """
class Book {
    string title;
    string author;
    
    Book(string t; string a) {
        title := t;
        author := a;
    }
    
    void displayInfo() {
        io.writeStrLn("Title:" ^ title);
        io.writeStrLn("Author:" ^ author);
    }
}

class Library {
    Book[5] books;
    
    Library(Book[5] b) {
        books := b;
    }
    
    void displayBooks() {
        io.writeStrLn("Library Catalog:");
        for i := 0 to books.length do {
           (books[i]).displayInfo(a);
        }
    }
}

class Test {
    static void main() {
        Book[3] bookList;
        Library myLibrary = new Library(bookList);
        bookList[0] := new Book("Harry Potter", "J.K. Rowling");
        bookList[1] := new Book("The Hobbit", "J.R.R. Tolkien");
        bookList[2] := new Book("1984", "George Orwell");
        
        myLibrary.displayBooks();
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))