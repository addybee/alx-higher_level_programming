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

    @classmethod
    def tearDownClass(self):
        """ deletete attribute (attr) of TestBase """
        del self.b1
        del self.b2
        del self.b3
        del self.b4

    def test_Base_id_equal(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 22)
        self.assertEqual(self.b4.id, 3)

    def test_object(self):
        self.assertTrue(isinstance(self.b1, Base))
        self.assertTrue(isinstance(self.b3, Base))


if __name__ == "__main__":
    unittest.main()
