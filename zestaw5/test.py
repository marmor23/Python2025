from fracs import *
import unittest

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 5], [1, 8]), [13, 40])
        self.assertEqual(add_frac([1, 5], [1, 20]), [1, 4])
    def test_sub_frac(self):
    	self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
    	self.assertEqual(sub_frac([1, 4], [1, 2]), [-1, 4])
    	self.assertEqual(sub_frac([1, 25], [1, 4]), [-21, 100])
    def test_mul_frac(self):
    	self.assertEqual(mul_frac([1, 3], [1, 4]), [1, 12])
    	self.assertEqual(mul_frac([-1, 2], [2, 3]), [-1, 3])
    	self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
    def test_div_frac(self):
    	self.assertEqual(div_frac([7, 2], [1, 5]), [35, 2])
    	self.assertEqual(div_frac([-3, 5], [2, 15]), [-9, 2])
    	self.assertEqual(div_frac(self.zero, [88, 99]), self.zero)
    def test_is_positive(self):
    	self.assertFalse(is_positive(self.zero))
    	self.assertFalse(is_positive([1, -3]))
    	self.assertTrue(is_positive([2, 5]))
    def test_is_zero(self):
    	self.assertTrue(is_zero(self.zero))
    	self.assertTrue(is_zero([0, 3]))
    	self.assertFalse(is_zero([2, -5]))
    def test_cmp_frac(self):
    	self.assertEqual(cmp_frac([2, 5], [1, 3]), 1)
    	self.assertEqual(cmp_frac([-1, 7], [1, -8]), -1)
    	self.assertEqual(cmp_frac([13, 39], [1, 3]), 0)
    def test_frac2float(self):
    	self.assertEqual(frac2float([2, 4]), 0.5)
    	self.assertAlmostEqual(frac2float([1, 7]), 0.142857, places = 6)
    	self.assertAlmostEqual(frac2float([-2, 17]), -0.11764705, places = 7)

if __name__ == '__main__':
    unittest.main()
