from points import Point

class Rectangle:
	def __init__(self, x1, y1, x2, y2):
		if x1 >= x2 or y1 >= y2:
			raise ValueError("Podane wspolrzedne nie tworza prostokata!")
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)
	def __str__(self):
		return "[(%s, %s), (%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)
	def __repr__(self):
		return "Rectangle(%s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)
	def __eq__(self, other):
		return self.pt1 == other.pt1 and self.pt2 == other.pt2
	def __ne__(self, other):
		return not self == other
	def center(self):
		return Point((self.pt2.x + self.pt1.x) / 2, (self.pt2.y + self.pt1.y) / 2)
	def area(self):
		return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)
	def move(self, x, y):
		tmp1 = self.pt1 + Point(x, y)
		tmp2 = self.pt2 + Point(x, y)
		return Rectangle(tmp1.x, tmp1.y, tmp2.x, tmp2.y)
	def intersection(self, other):
		xn1 = max(self.pt1.x, other.pt1.x)
		xn2 = min(self.pt2.x, other.pt2.x)
		yn1 = max(self.pt1.y, other.pt1.y)
		yn2 = min(self.pt2.y, other.pt2.y)  
		if xn1 >= xn2 or yn1 >= yn2:
			raise ValueError("Prostokaty sa rozlaczne, ich przeciecie nie istnieje!")
		return Rectangle(xn1, yn1, xn2, yn2)
	def cover(self, other):
		return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
	def make4(self):
		center = self.center()
		return (Rectangle(self.pt1.x, self.pt1.y, center.x, center.y), Rectangle(center.x, self.pt1.y, self.pt2.x, center.y), Rectangle(self.pt1.x, center.y, center.x, self.pt2.y), Rectangle(center.x, center.y, self.pt2.x, self.pt2.y))
	@staticmethod
	def from_points(plist):
		return Rectangle(plist[0].x, plist[0].y, plist[1].x, plist[1].y)
	@property
	def top(self):
		return self.pt2.y
	@property
	def bottom(self):
		return self.pt1.y
	@property
	def left(self):
		return self.pt1.x
	@property
	def right(self):
		return self.pt2.x
	@property
	def width(self):
		return self.pt2.x - self.pt1.x
	@property
	def height(self):
		return self.pt2.y - self.pt1.y
	@property
	def topleft(self):
		return Point(self.pt1.x, self.pt2.y)
	@property
	def bottomleft(self):
		return self.pt1
	@property
	def topright(self):
		return self.pt2
	@property
	def bottomright(self):
		return Point(self.pt2.x, self.pt1.y)
