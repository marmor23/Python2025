def gcd(a, b):
	while b:
		a, b, = b, a % b
	return a
	
class Frac:
	def __init__(self, x = 0, y = 1):
		# Konstrukcja ulamka z liczby calkowitej podobnie jak we wbudowanej klasie Fraction
		if isinstance(x, float):
			self.x, self.y = float.as_integer_ratio(x)
		else:
			self.x = x
			self.y = y
		self.check()
		g = gcd(self.x, self.y)
		self.x = self.x // g
		self.y = self.y // g
	def check(self):
		if not isinstance(self.x, int):
			raise ValueError("Licznk powinien byc liczba calkowita!")
		if not isinstance(self.y, int):
			raise ValueError("Mianownik powinien byc liczba calkowita!")
		if self.y == 0:
			raise ValueError("Mianownik musi byc rozny od zera!")
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
		if isinstance(other, float):
			return self.cmp("", Frac(other))
		elif isinstance(other, int):
			return self.cmp("", Frac(other, 1))
		elif not isinstance(other, Frac):
			raise ValueError("Niedozwolony typ zmiennej other!")
		other.check()
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
		if isinstance(other, float):
			return self + Frac(other)
		elif isinstance(other, int):
			return self + Frac(other, 1)
		elif not isinstance(other, Frac):
			raise ValueError("Niedozwolony typ zmiennej other!")
		other.check()
		return Frac(self.x * other.y + self.y * other.x, self.y * other.y)
	__radd__ = __add__
	def __sub__(self, other):
		if isinstance(other, float):
			return self - Frac(other)
		elif isinstance(other, int):
			return self - Frac(other, 1)
		elif not isinstance(other, Frac):
			raise ValueError("Niedozwolony typ zmiennej other!")
		other.check()
		return Frac(self.x * other.y - self.y * other.x, self.y * other.y)
	def __rsub__(self, other):
		return Frac(self.y * other - self.x, self.y)
	def __mul__(self, other):
		if isinstance(other, float):
			return self * Frac(other)
		elif isinstance(other, int):
			return self * Frac(other, 1)
		elif not isinstance(other, Frac):
			raise ValueError("Niedozwolony typ zmiennej other!")
		other.check()
		return Frac(self.x * other.x, self.y * other.y)
	__rmul__ = __mul__
	def __truediv__(self, other):
		if isinstance(other, float):
			return self / Frac(other)
		elif isinstance(other, int):
			return self / Frac(other, 1)
		elif not isinstance(other, Frac):
			raise ValueError("Niedozwolony typ zmiennej other!")
		other.check()
		if other.x == 0:
			raise ValueError("Nie mozna podzielic przez ulamek, ktory ma wartosc 0!")
		return Frac(self.x * other.y, self.y * other.x)
	def __rtruediv__(self, other):
		if isinstance(other, float):
			return Frac(other) / self
		elif isinstance(other, int):
			return Frac(other, 1) / self
		elif not isinstance(other, Frac):
			raise ValueError("Niedozwolony typ zmiennej other!")
		return other / self
	def __pos__(self):
		return self
	def __neg__(self):
		return Frac(-self.x, self.y)
	def __invert__(self):
		if self.x == 0:
			raise ValueError("Nie mozna odwrocic ulamka o wartosci 0!")
		return Frac(self.y, self.x)
	def __float__(self):
		return self.x / self.y
	def __hash__(self):
		return hash(float(self))
	def is_positive(self):
		return self.x * self.y > 0
	def is_zero(self):
		return self.x == 0
