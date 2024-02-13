""" defines unit tests for base.py """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ defines unit test """
    @classmethod
    def setUpClass(cls):
        """ create 3 obj of Base & assign id attr of new obj to attr of
        TestBase"""

        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(22)
        cls.b4 = Base()
        cls.idx = 0

    @classmethod
    def tearDownClass(cls):
        """ deletete attribute (attr) of TestBase """
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        cls.idx = 0

    def test_Base_id_equal(self):
        self.idx += 1
        self.assertEqual(self.b1.id, self.idx)
        self.idx += 1
        self.assertEqual(self.b2.id, self.idx)
        self.assertEqual(self.b3.id, 22)
        self.idx += 1
        self.assertEqual(self.b4.id, self.idx)

    def test_object(self):
        self.assertTrue(isinstance(self.b1, Base))
        self.assertTrue(isinstance(self.b3, Base))


if __name__ == "__main__":
    unittest.main()
