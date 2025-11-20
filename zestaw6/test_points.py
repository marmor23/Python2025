from points import Point
import unittest

class TestPoint(unittest.TestCase):
	def test_tostr(self):
		self.assertEqual(str(Point(3, 7)), "(3, 7)")
		self.assertEqual(str(Point(10, 52)), "(10, 52)")
	def test_repr(self):
		self.assertEqual(repr(Point(3, 7)), "Point(3, 7)")
		self.assertEqual(repr(Point(10, 52)), "Point(10, 52)")
	def test_eq(self):
		self.assertEqual(Point(2, 8), Point(2, 8))
		self.assertEqual(Point(-33, 77), Point(-33, 77))
	def test_neq(self):
		self.assertNotEqual(Point(1, 2), Point(3, 4))
		self.assertNotEqual(Point(-35, 89), Point(35, 89))
	def test_add(self):
		self.assertEqual(Point(2, 2) + Point(6, 6), Point(8, 8))
		self.assertEqual(Point(3, 4) + Point(5, 6), Point(8, 10))
		self.assertEqual(Point(-12, 4) + Point(12, -4), Point(0, 0))
	def test_sub(self):
		self.assertEqual(Point(1, 7) - Point(6, 2), Point(-5, 5))
		self.assertEqual(Point(5, 4) - Point(3, 9), Point(2, -5))
		self.assertEqual(Point(22, 13) - Point(4, -4), Point(18, 17))
	def test_mul(self):
		self.assertEqual(Point(2, 3) * Point(2, 3), Point(4, 9))
		self.assertEqual(Point(7, 8) * Point(-3, 5), Point(-21, 40))
		self.assertEqual(Point(6, 2) * Point(7, 1), Point(42, 2))
	def test_cross(self):
		self.assertEqual(Point(6, 3).cross(Point(2, 4)), 18)
		self.assertEqual(Point(-1, -5).cross(Point(3, -8)), 23)
		self.assertEqual(Point(11, 0).cross(Point(345, 22)), 242)
	def test_length(self):
		self.assertEqual(Point(4, 3).length(), 5)
		self.assertEqual(Point(-60, -11).length(), 61)
		self.assertAlmostEqual(Point(1, -2).length(), 2.236068, places = 6)
		
if __name__ == "__main__":
	unittest.main()
