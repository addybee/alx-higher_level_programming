#!/usr/bin/python3
"""Unittest for the function max_integer([])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, max_integer, 50)
        self.assertRaises(TypeError, max_integer, {10, 20, 30})
        self.assertRaises(TypeError, max_integer,  ["10", 20, [40, 30], 50])

    def test_max_end_list(self):
        self.assertEqual(max_integer([50, 40, 30, 80]), 80)

    def test_unorded_list(self):
        self.assertEqual(max_integer([30, 40, 21, 12]), 40)

    def test_max_beginning_list(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_list(self):
        self.assertEqual(max_integer([11]), 11)

    def test_single_negative_list(self):
        self.assertEqual(max_integer([11, 24, 35, -46]), 35)

    def test_all_negative_list(self):
        self.assertEqual(max_integer([-4, -31, -22, -13]), -4)

    def test_float_list(self):
        self.assertEqual(max_integer([3.1, 4.8, 5.4, 10.3]), 10.3)
