def gcd(a, b):
	while b:
		a, b, = b, a % b
	return a
	
def simplify(frac):
	g = gcd(frac.x, frac.y)
	return Frac(frac.x // g, frac.y // g)

class Frac:
	def __init__(self, x = 0, y = 1):
		self.x = x
		self.y = y
	def __str__(self):
		if self.y == 1:
			return str(self.x)
		return "%d/%d" % (self.x, self.y)
	def __repr__(self):
		return "Frac(%d, %d)" % (self.x, self.y)
	def cmp(self, tmp, other):
		"""
		Funkcja zwraca:
		-1 jesli self < other
		0 jesli self = other
		1 jesli self > other
		"""
		g = gcd(self.y, other.y)
		fv1 = self.x * other.y // g
		fv2 = other.x * self.y // g
		if fv1 > fv2:
			return 1
		elif fv2 > fv1:
			return -1
		return 0
	def __eq__(self, other):
		return self.cmp(self, other) == 0
	def __ne__(self, other):
		return self.cmp(self, other) != 0
	def __lt__(self, other):
		return self.cmp(self, other) < 0
	def __le__(self, other):
		return self.cmp(self, other) <= 0
	def __gt__(self, other):
		return self.cmp(self, other) > 0
	def __ge__(self, other):
		return self.cmp(self, other) >= 0
	def __add__(self, other):
		return simplify(Frac(self.x * other.y + self.y * other.x, self.y * other.y))	
	def __sub__(self, other):
		return simplify(Frac(self.x * other.y - self.y * other.x, self.y * other.y))
	def __mul__(self, other):
		return simplify(Frac(self.x * other.x, self.y * other.y))
	def __truediv__(self, other):
		return simplify(Frac(self.x * other.y, self.y * other.x))
	def __floordiv__(self, other):
		return Frac((self.x * other.y) // (self.y * other.x), 1)
	def __mod__(self, other):
		return Frac((self.x * other.y) % (other.x * self.y), self.y * other.y)
	def __pos__(self):
		return self
	def __neg__(self):
		return Frac(-self.x, self.y)
	def __invert__(self):
		return Frac(self.y, self.x)
	def __float__(self):
		return self.x / self.y
	def __hash__(self):
		return hash(float(self))
	def is_positive(self):
		return self.x * self.y > 0
	def is_zero(self):
		return self.x == 0
