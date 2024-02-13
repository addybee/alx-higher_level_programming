#!/usr/bin/python3
""" defines a Square tests """


from io import StringIO
import unittest
from models.square import Square
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """ this defines tests for square """
    @classmethod
    def setUpClass(cls):
        """ initializes new object """
        cls.idx = 0
        cls.sq1 = Square(5)
        cls.sq2 = Square(3, 3, 3, 3)
        cls.sq3 = Square(4, 3, 3, 33)
        cls.sq4 = Square(2, 1, 1, 34)

    @classmethod
    def tearDownClass(cls):
        """ del initialized instance attr for TestSquare """
        del cls.sq1
        del cls.sq2
        del cls.sq3
        del cls.sq4

    def test_obj_type(self):
        """ test if object created is type Square """

        self.assertTrue(isinstance(self.sq1, Square))
        self.assertTrue(isinstance(self.sq2, Square))

    def test_attr_val(self):
        """ compare the attributes and the setters and getters of square"""
        self.assertEqual(self.sq2.id, 3)
        self.assertEqual(self.sq1.size, 5)
        self.assertEqual(self.sq2.size, 3)
        sq_attr = [self.sq1.width, self.sq1.height, self.sq1.x, self.sq1.y]
        sq_attr2 = [self.sq2.width, self.sq2.height, self.sq2.x, self.sq2.y]
        self.assertEqual(sq_attr, [5, 5, 0, 0])
        self.assertEqual(sq_attr2, [3, 3, 3, 3])
        self.sq1.x = 4
        self.sq1.y = 3
        self.assertEqual(self.sq1.x, 4)
        self.assertEqual(self.sq1.y, 3)

    def test_TypeError_validateattr(self):
        """ this function test the validation for attributes """

        with self.assertRaises(TypeError, msg="width must be an integer"):
            self.sq1.width = "5"

        self.idx += 1
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Obj1 = Square("5")

        with self.assertRaises(TypeError, msg="height must be an integer"):
            self.sq1.height = [3, 4]

        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.sq2.x = 4.553

        self.idx += 1
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Obj3 = Square(14, "4")

        with self.assertRaises(TypeError, msg="y must be an integer"):
            self.sq1.y = "5"

    def test_ValueError_validateAttr(self):
        """this function test value errore"""

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.sq1.width = 0

        self.idx += 1
        with self.assertRaises(ValueError, msg="width must be > 0"):
            obj1 = Square(-12)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            self.sq1.height = -3

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            self.sq1.x = -3

        self.idx += 1
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            obj2 = Square(12, -2)

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            self.sq1.y = -2

    def test_area(self):
        """this test the area method"""
        self.assertEqual(self.sq1.area(), 25)
        self.assertEqual(self.sq2.area(), 9)

    def test__str__(self):
        """this function test the output of str() on object"""
        self.assertEqual(str(self.sq3), "[Square] (33) 3/3 - 4")

        str_obj_file = StringIO()
        with redirect_stdout(str_obj_file):
            print(self.sq3)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (33) 3/3 - 4\n")

    def test_display1(self):
        """ test the display function with coordinate in place"""
        str_obj_file = StringIO()
        with redirect_stdout(str_obj_file):
            self.sq3.display()
        self.assertEqual(str_obj_file.getvalue(),
                         "\n\n\n   ####\n   ####\n   ####\n   ####\n")

        s2 = Square(4)
        self.idx += 1

        str_obj_file1 = StringIO()
        with redirect_stdout(str_obj_file1):
            s2.display()
        self.assertEqual(str_obj_file1.getvalue(), "####\n####\n####\n####\n")

    def test_square_update0(self):
        """this function assigns an argument to each attribute"""
        str_obj_file = StringIO()
        self.sq4.update(89)
        with redirect_stdout(str_obj_file):
            print(self.sq4)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (89) 1/1 - 2\n")

        str_obj_file1 = StringIO()
        self.sq4.update(89, 2)
        with redirect_stdout(str_obj_file1):
            print(self.sq4)
        self.assertEqual(str_obj_file1.getvalue(), "[Square] (89) 1/1 - 2\n")

        str_obj_file = StringIO()
        self.sq4.update(89, 2, 3)
        with redirect_stdout(str_obj_file):
            print(self.sq4)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (89) 3/1 - 2\n")

        str_obj_file = StringIO()
        self.sq4.update(89, 2, 3, 4)
        with redirect_stdout(str_obj_file):
            print(self.sq4)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (89) 3/4 - 2\n")

    def test_square_update1(self):
        """ Update the class Square """
        sq5 = Square(2, 2, 2, 2)
        str_obj_file = StringIO()
        sq5.update(size=10)
        with redirect_stdout(str_obj_file):
            print(sq5)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (2) 2/2 - 10\n")

        str_obj_file1 = StringIO()
        sq5.update(size=9, x=8)
        with redirect_stdout(str_obj_file1):
            print(sq5)
        self.assertEqual(str_obj_file1.getvalue(), "[Square] (2) 8/2 - 9\n")

        str_obj_file = StringIO()
        sq5.update(y=7, size=6, x=5, id=80)
        with redirect_stdout(str_obj_file):
            print(sq5)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (80) 5/7 - 6\n")

        str_obj_file = StringIO()
        sq5.update(x=4, size=3, y=2)
        with redirect_stdout(str_obj_file):
            print(sq5)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (80) 4/2 - 3\n")

        str_obj_file = StringIO()
        sq5.update(89, 3, 4, y=5)
        with redirect_stdout(str_obj_file):
            print(sq5)
        self.assertEqual(str_obj_file.getvalue(), "[Square] (89) 4/2 - 3\n")
