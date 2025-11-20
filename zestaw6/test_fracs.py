from fracs import Frac
import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.zero = Frac()
    def test_tostr(self):
    	self.assertEqual(str(Frac(1, 3)), "1/3")
    	self.assertEqual(str(Frac(7, 1)), "7")
    	self.assertEqual(str(Frac(12, 35)), "12/35")
    def test_repr(self):
    	self.assertEqual(repr(Frac(1, 3)), "Frac(1, 3)")
    	self.assertEqual(repr(Frac(7, 1)), "Frac(7, 1)")
    	self.assertEqual(repr(Frac(12, 35)), "Frac(12, 35)")
    def test_eq(self):
    	self.assertEqual(Frac(1, 3), Frac(2, 6))
    	self.assertEqual(Frac(81, 99), Frac(9, 11))
    	self.assertEqual(Frac(0, 7), self.zero)
    def test_neq(self):
    	self.assertNotEqual(Frac(1, 3), Frac(1, 5))
    	self.assertNotEqual(Frac(2, 3), Frac(2, 4))
    	self.assertNotEqual(Frac(11, 12), self.zero)
    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) +  Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 5) +  Frac(1, 8), Frac(13, 40))
        self.assertEqual(Frac(1, 5) +  Frac(1, 20), Frac(1, 4))
    def test_sub_frac(self):
    	self.assertEqual(Frac(1, 2) -  Frac(1, 3), Frac(1, 6))
    	self.assertEqual(Frac(1, 4) -  Frac(1, 2), Frac(-1, 4))
    	self.assertEqual(Frac(1, 25) -  Frac(1, 4), Frac(-21, 100))
    def test_mul_frac(self):
    	self.assertEqual(Frac(1, 3) * Frac(1, 4), Frac(1, 12))
    	self.assertEqual(Frac(-1, 2) * Frac(2, 3), Frac(-1, 3))
    	self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))
    def test_truediv_frac(self):
    	self.assertEqual(Frac(7, 2) / Frac(1, 5), Frac(35, 2))
    	self.assertEqual(Frac(-3, 5) / Frac(2, 15), Frac(-9, 2))
    	self.assertEqual(self.zero / Frac(88, 99), self.zero)
    def test_floordiv_frac(self):
    	self.assertEqual(Frac(7, 2) // Frac(2, 3), Frac(5, 1))
    	self.assertEqual(Frac(15, 4) // Frac(7, 11), Frac(5, 1))
    	self.assertEqual(Frac(33, 2) // Frac(12, 5), Frac(6, 1))
    def test_mod_frac(self):
    	self.assertEqual(Frac(15, 6) % Frac(1, 5), Frac(1, 10))
    	self.assertEqual(Frac(7, 3) % Frac(2, 7), Frac(1, 21))
    	self.assertEqual(Frac(8, 11) % Frac(3, 7), Frac(23, 77))
    def test_pos(self):
    	self.assertEqual(Frac(1, 3), +Frac(1, 3))
    	self.assertEqual(Frac(11, 7), +Frac(11, 7))
    	self.assertEqual(Frac(100, 9), +Frac(100, 9))
    def test_neg(self):
    	self.assertEqual(Frac(-1, 5), -Frac(1, 5))
    	self.assertEqual(Frac(-2, 3), -Frac(2, 3))
    	self.assertEqual(Frac(34, -53), -Frac(34, 53))
    def test_invert(self):
    	self.assertEqual(Frac(2, 9), ~Frac(9, 2))
    	self.assertEqual(Frac(1, 7), ~Frac(7, 1))
    	self.assertEqual(Frac(1, 1), ~Frac(1, 1))
    def test_tofloat(self):
    	self.assertEqual(float(Frac(2, 4)), 0.5)
    	self.assertAlmostEqual(float(Frac(1, 7)), 0.142857, places = 6)
    	self.assertAlmostEqual(float(Frac(-2, 17)), -0.11764705, places = 7)
    def test_is_positive(self):
    	self.assertFalse(self.zero.is_positive())
    	self.assertFalse(Frac(1, -3).is_positive())
    	self.assertTrue(Frac(2, 5).is_positive())
    def test_is_zero(self):
    	self.assertTrue(self.zero.is_zero())
    	self.assertTrue(Frac(0, 3).is_zero())
    	self.assertFalse(Frac(2, -5).is_zero())
	
if __name__ == '__main__':
    unittest.main()
