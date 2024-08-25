import unittest
from lw_AT01_3 import *


class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)
        self.assertRaises(TypeError, divide, 6, 0)


if __name__ == '__main__':
    unittest.main()
