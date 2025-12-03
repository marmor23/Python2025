from rectangles import Rectangle
from points import Point
import pytest

class TestRectangle:
	
	@pytest.fixture
	def rectlist(self):
		return [
			Rectangle(2, 2, 6, 6),
			Rectangle(0, 1, 7, 8),
			Rectangle(-5, -5, 10, 10),
			Rectangle(-7, 3, 4, 5),
			Rectangle(-13, -17, 14, 21)
		]
	
	def test_eq_neq(self, rectlist):
		assert rectlist[0] == Rectangle(2, 2, 6, 6)
		assert rectlist[4] == Rectangle(-13, -17, 14, 21)
		assert rectlist[2] != rectlist[3]
		assert rectlist[3] != Rectangle(2, 3, 4, 5)
		
	def test_center(self, rectlist):
		assert rectlist[0].center() == Point(4, 4)
		assert rectlist[2].center() == Point(2.5, 2.5)
		assert Rectangle(-2, -4, 3, 5).center() == Point(0.5, 0.5)

	def test_area(self, rectlist):
		assert rectlist[1].area() == 49
		assert rectlist[4].area() == 1026
		assert Rectangle(8, 8, 10, 10).area() == 4
	
	def test_move(self, rectlist):
		assert rectlist[1].move(2, 3) == Rectangle(2, 4, 9, 11)
		assert rectlist[2].move(-7, 9) == Rectangle(-12, 4, 3, 19)
		assert rectlist[3].move(-8, -3) == Rectangle(-15, 0, -4, 2)
	
	def test_intersection(self, rectlist):
		assert rectlist[0].intersection(rectlist[1]) == rectlist[0]
		assert rectlist[2].intersection(rectlist[3]) == Rectangle(-5, 3, 4, 5)
		assert rectlist[3].intersection(rectlist[1]) == Rectangle(0, 3, 4, 5)
		assert Rectangle(2, -3, 70, 13).intersection(Rectangle(2, 4, 8, 26)) == Rectangle(2, 4, 8, 13)
	
	def test_cover(self, rectlist):
		assert rectlist[0].cover(rectlist[1]) == Rectangle(0, 1, 7, 8)
		assert rectlist[2].cover(rectlist[3]) == Rectangle(-7, -5, 10, 10)
		assert rectlist[4].cover(Rectangle(33, 44, 55, 66)) == Rectangle(-13, -17, 55, 66)
		assert rectlist[3].cover(Rectangle(-100, -123, 2, 1)) == Rectangle(-100, -123, 4, 5)
	
	def test_make4(self, rectlist):
		assert rectlist[0].make4() == (Rectangle(2, 2, 4, 4), Rectangle(4, 2, 6, 4), Rectangle(2, 4, 4, 6), Rectangle(4, 4, 6, 6))
		assert rectlist[2].make4() == (Rectangle(-5, -5, 2.5, 2.5), Rectangle(2.5, -5, 10, 2.5), Rectangle(-5, 2.5, 2.5, 10), Rectangle(2.5, 2.5, 10, 10))
		assert rectlist[3].make4() == (Rectangle(-7, 3, -1.5, 4.0), Rectangle(-1.5, 3, 4, 4.0), Rectangle(-7, 4.0, -1.5, 5), Rectangle(-1.5, 4.0, 4, 5))
		assert Rectangle(-9, 1.2, 3.1, 3.45).make4() == (Rectangle(-9, 1.2, -2.95, 2.325), Rectangle(-2.95, 1.2, 3.1, 2.325), Rectangle(-9, 2.325, -2.95, 3.45), Rectangle(-2.95, 2.325, 3.1, 3.45))
		
	def test_frompoints(self, rectlist):
		assert Rectangle.from_points([Point(2, 2), Point(6, 6)]) == rectlist[0]	
		assert Rectangle.from_points([Point(-7, 3), Point(4, 5)]) == rectlist[3]
		assert Rectangle.from_points([Point(1, 7), Point(2, 11)]) == Rectangle(1, 7, 2, 11)
	
	def test_top(self, rectlist):
		assert rectlist[0].top == 6
		assert rectlist[1].top == 8
		assert rectlist[2].top == 10

	def test_bottom(self, rectlist):
		assert rectlist[2].bottom == -5
		assert rectlist[3].bottom == 3
		assert rectlist[4].bottom == -17

	def test_left(self, rectlist):
		assert rectlist[1].left == 0
		assert rectlist[3].left == -7
		assert rectlist[4].left == -13

	def test_right(self, rectlist):
		assert rectlist[0].right == 6
		assert rectlist[2].right == 10
		assert rectlist[4].right == 14
	
	def test_width(self, rectlist):
		assert rectlist[0].width == 4
		assert rectlist[3].width == 11
		assert rectlist[4].width == 27
	
	def test_heigth(self, rectlist):
		assert rectlist[1].height == 7
		assert rectlist[2].height == 15
		assert rectlist[3].height == 2
		
	def test_topleft(self, rectlist):
		assert rectlist[0].topleft == Point(2, 6)
		assert rectlist[1].topleft == Point(0, 8)
		assert rectlist[3].topleft == Point(-7, 5)
	
	def test_topright(self, rectlist):
		assert rectlist[1].topright == Point(7, 8)
		assert rectlist[2].topright == Point(10, 10)
		assert Rectangle(1, 1, 11, 13).topright == Point(11, 13)
	
	def test_bottomleft(self, rectlist):
		assert rectlist[2].bottomleft == Point(-5, -5)
		assert rectlist[3].bottomleft == Point(-7, 3)
		assert Rectangle(-5.2, -6.33, 12.456, 112.9898).bottomleft == Point(-5.2, -6.33)
	
	def test_bottomright(self, rectlist):
		assert rectlist[0].bottomright == Point(6, 2)
		assert rectlist[4].bottomright == Point(14, -17)
		assert Rectangle(-1.23, -4.671, 8.898, 9.6332).bottomright == Point(8.898, -4.671)
		
if __name__ == "__main__":
	pytest.main()
