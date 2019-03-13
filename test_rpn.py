import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)

    def test_percentage(self):
        result = rpn.calculate("100 5 %")
        self.assertEqual(105, result)
    def test_exponent(self):
        result = rpn.calculate("3 2 ^")
        self.assertEqual(9, result)
    def test_floordivide(self):
        result = rpn.calculate("7 3 //")
        self.assertEqual(2, result)
    def test_factorial(self):
        result = rpn.calculate("5 0 !")
        self.assertEqual(120, result)
    def test_bitAnd(self):
        result = rpn.calculate("3 2 &")
        self.assertEqual(0, result)
    def test_bitOr(self):
        result = rpn.calculate("4 2 |")
        self.assertEqual(4, result)
    def test_bitNot(self):
        result = rpn.calculate("5 0 ~")
        self.assertEqual(-5, result)

if __name__ == '__main__':
    unittest.main()
