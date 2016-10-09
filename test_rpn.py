import unittest
import rpn
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_sub(self):
    	result = rpn.calculate("1 1 -")
    	self.assertEqual(0, result)
    def test_mult(self):
    	result = rpn.calculate("2 3 *")
    	self.assertEqual(6, result)
    def test_div(self):
    	result = rpn.calculate("6 3 /")
    	self.assertEqual(2, result)
    def test_exp(self):
        result = rpn.calculate("2 4 ^")
        self.assertEqual(16, result)