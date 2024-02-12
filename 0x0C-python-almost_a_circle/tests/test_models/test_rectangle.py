#!/usr/bin/python3
""" defines a rectangle tests """


import unittest
from io import StringIO
from models.rectangle import Rectangle
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """ this defines tests for rectangle """
    @classmethod
    def setUpClass(cls):
        """ initializes new object """
        cls.r1 = Rectangle(2, 10)
        cls.r2 = Rectangle(5, 3, 1, 1, 6)
        cls.r3 = Rectangle(11, 15, 1, 1, 15)
        cls.r4 = Rectangle(10, 5, 3, 2, 5)
        cls.r5 = Rectangle(10, 5, 3, 2, 7)

    @classmethod
    def tearDownClass(cls):
        """ del initialized instance attr for TestRectangle """
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4
        del cls.r5

    def test_obj_type(self):
        """ test if object created is type Rectangle """

        self.assertTrue(isinstance(self.r1, Rectangle))
        self.assertTrue(isinstance(self.r3, Rectangle))

    def test_attr_val(self):
        """ compare the attributes and the setters and getters """

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r3.id, 15)
        rect_attr = [self.r1.width, self.r1.height, self.r1.x, self.r1.y]
        rect_attr2 = [self.r3.width, self.r3.height, self.r3.x, self.r3.y]
        self.assertEqual(rect_attr, [2, 10, 0, 0])
        self.assertEqual(rect_attr2, [11, 15, 1, 1])
        self.r1.x = 4
        self.r1.y = 3
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 3)

    def test_TypeError_validateattr(self):
        """ this function test the validator code """

        with self.assertRaises(TypeError, msg="width must be an integer"):
            self.r1.width = "5"
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Obj1 = Rectangle("5", 14)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            self.r1.height = [3, 4]
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Obj2 = Rectangle(5, "14")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.r3.x = 4.553
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Obj3 = Rectangle(5, 14, "4")

        with self.assertRaises(TypeError, msg="y must be an integer"):
            self.r1.y = "5"

    def test_ValueError_validateAttr(self):
        """this function test value errore"""

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.r1.width = 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            obj1 = Rectangle(-12, 6)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            self.r1.height = -3

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            self.r1.x = -3
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            obj2 = Rectangle(12, 6, -2)

        with self.assertRaises(ValueError, msg="y must be > 0"):
            self.r1.y = -2

    def test_area(self):
        """this test the area method"""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r3.area(), 165)

    @unittest.skip("the cordinate not considered in display, so will fail")
    def test_display0(self):
        """this function tests the display method"""
        str_obj_file = StringIO()
        with redirect_stdout(str_obj_file):
            self.r2.display()
        self.assertEqual(str_obj_file.getvalue(), "#####\n#####\n#####\n")

    def test__str__(self):
        """this function test the output of str() on object"""
        self.assertEqual(str(self.r2), "[Rectangle] (6) 1/1 - 5/3")
        str_obj_file = StringIO()
        with redirect_stdout(str_obj_file):
            print(self.r2)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (6) 1/1 - 5/3\n")

    def test_display1(self):
        """ test the display function with coordinate in place"""
        str_obj_file = StringIO()
        with redirect_stdout(str_obj_file):
            self.r2.display()
        self.assertEqual(str_obj_file.getvalue(), "\n #####\n #####\n #####\n")
        r2 = Rectangle(4, 4, id=3) 
        str_obj_file1 = StringIO()
        with redirect_stdout(str_obj_file1):
            r2.display()
        self.assertEqual(str_obj_file1.getvalue(), "####\n####\n####\n####\n")

    def test_update0(self):
        """this function assigns an argument to each attribute"""
        str_obj_file = StringIO()
        self.r4.update(89)
        with redirect_stdout(str_obj_file):
            print(self.r4)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (89) 3/2 - 10/5\n")

        str_obj_file1 = StringIO()
        self.r4.update(89, 2)
        with redirect_stdout(str_obj_file1):
            print(self.r4)
        self.assertEqual(str_obj_file1.getvalue(), "[Rectangle] (89) 3/2 - 2/5\n")

        str_obj_file = StringIO()
        self.r4.update(89, 2, 3)
        with redirect_stdout(str_obj_file):
            print(self.r4)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (89) 3/2 - 2/3\n")
        
        str_obj_file = StringIO()
        self.r4.update(89, 2, 3, 4)
        with redirect_stdout(str_obj_file):
            print(self.r4)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (89) 4/2 - 2/3\n")

        str_obj_file = StringIO()
        self.r4.update(89, 2, 3, 4, 5)
        with redirect_stdout(str_obj_file):
            print(self.r4)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

    def test_update1(self):
        """ Update the class Rectangle """
        str_obj_file = StringIO()
        self.r5.update(height=10)
        with redirect_stdout(str_obj_file):
            print(self.r5)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (7) 3/2 - 10/10\n")

        str_obj_file1 = StringIO()
        self.r5.update(width=9, x=8)
        with redirect_stdout(str_obj_file1):
            print(self.r5)
        self.assertEqual(str_obj_file1.getvalue(), "[Rectangle] (7) 8/2 - 9/10\n")

        str_obj_file = StringIO()
        self.r5.update(y=7, width=6, x=5, id =80)
        with redirect_stdout(str_obj_file):
            print(self.r5)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (80) 5/7 - 6/10\n")
        
        str_obj_file = StringIO()
        self.r5.update(x=4, width=3, y=2, height=1)
        with redirect_stdout(str_obj_file):
            print(self.r5)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (80) 4/2 - 3/1\n")
        
        str_obj_file = StringIO()
        self.r5.update(89, 2, 3, 4, 5)
        with redirect_stdout(str_obj_file):
            print(self.r5)
        self.assertEqual(str_obj_file.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")


if __name__ == "__main__":
    unittest.main()
