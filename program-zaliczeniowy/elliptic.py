from utils import bisprime, hasmodularsqrt, modularsqrt
import hashlib
import random

class point:
	"""
	Klasa reprezentujaca punkt na krzywej eliptycznej
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __eq__(self, other):
		if isinstance(other, tuple):
			return self.x == other[0] and self.y == other[1]
		return self.x == other.x and self.y == other.y
	def __ne__(self, other):
		return not self == other
	def __str__(self):
		return "(%d, %d)" % (self.x, self.y)
	def __repr__(self):
		return "point(%d, %d)" % (self.x, self.y)
		
class ellipticcurve:
	def __init__(self, a, b, p, basepoint = None, order = None):
		"""
		Klasa reprezentujaca krzywa eliptyczna
		Krzywa przedstawiona jest w postaci Weierstrassa: y^2 == x^3 + ax + b (mod p)
		Parametr 'p' musi byc liczba pierwsza
		Krzywa nie moze byc osobliwa. Ten warunek jest spelniony wtedy, gdy wyroznik D = 4*a^3 + 27*b^2 != 0 (mod p)
		"""
		if not bisprime(p):
			raise ValueError("Liczba p musi byc pierwsza!")
		if (4 * a **3 + 27 * b ** 2) % p == 0:
			raise ValueError("Krzywa jest osobliwa")
		self.a = a
		self.b = b
		self.p = p
		if basepoint and not self.bisoncurve(basepoint):
			raise ValueError("Punkt bazowy musi lezec na krzywej!")
		self.order = order
		self.basepoint = basepoint
		# Punkt w nieskonczonosci jest elementem neutralnym wzgledem dodawania punktow
		self.inf = point(0, 0)
	
	def setbasepoint(self, basepoint):
		self.basepoint = basepoint
		
	def setorder(self, order):
		self.order = order
	
	def bisoncurve(self, pt):
		""" Sprawdza, czy punkt lezy na krzywej """
		return pt.y ** 2 % self.p == (pt.x ** 3 + self.a * pt.x + self.b) % self.p
		
	def pneg(self, pt):
		""" Zwraca punkt przeciwny do wejsciowego """
		# Punkt w nieskonczonosci nie posiada punktu przeciwnego
		if pt == self.inf:
			return self.inf
		return point(pt.x, self.p - pt.y)
		
	def pdbl(self, pt):
		"""
		Podwaja dany punkt, zwraca punkt P = 2 * pt
		"""
		if pt == self.inf:
			return self.inf
		if not self.bisoncurve(pt):
			raise Exception("Punkt wejsciowy nie znajduje sie na krzywej")
		if pt.y == 0:
			return self.inf
		tmp = (3 * pt.x ** 2 + self.a) * pow(2 * pt.y, -1, self.p) % self.p
		x2 = (tmp ** 2 - 2 * pt.x) % self.p
		y2 = (tmp * (pt.x - x2) - pt.y) % self.p
		return point(x2, y2)
		
	def pointadd(self, pt1, pt2):
		"""
		Dodaje dwa punkty na krzywej, zwraca punkt P = pt1 + pt2
		"""
		if pt1 == self.inf:
			return pt2
		elif pt2 == self.inf:
			return pt1
		if not self.bisoncurve(pt1) or not self.bisoncurve(pt2):
			raise Exception("Punkty wejsciowe nie znajduja sie na krzywej")
		# Jesli punkty sa identyczne mozna zastosowac algorytm podwojenia punktu
		if pt1 == pt2:
			return self.pdbl(pt1)
		# Dodawanie przeciwnych punktow zwraca punkt w nieskonczonosci
		if pt2 == self.pneg(pt1):
			return self.inf
		tmp = (pt1.y - pt2.y) * pow(pt1.x - pt2.x, -1, self.p) % self.p
		x2 = (tmp ** 2 - pt1.x - pt2.x) % self.p
		y2 = (tmp * (pt1.x - x2) - pt1.y) % self.p
		return point(x2, y2)
		
	def pointsub(self, pt1, pt2):
		"""
		Odejmuje dwa punkty na krzywej, zwraca punkt P = pt1 - pt2
		"""
		return self.pointadd(pt1, self.pneg(pt2))
		
	def pointmul(self, pt, num):
		"""
		Mnozy punkt przez skalar (liczbe) zwraca punkt P = num * pt
		Algorytm jest szybki, gdyz dziala w czasie log(2, num) co jest bardzo wazne w praktyce (parametr num moze przyjmowac duze wartosci)
		"""
		if pt == self.inf:
			return self.inf
		if not self.bisoncurve(pt):
			raise ValueError("Punkt wejsciowy nie znajduje sie na krzywej")
		if num < 1:
			raise ValueError("Parametr num musi byc dodatni")
		elif num == 1:
			return pt
		if num & 1:
			return self.pointadd(self.pointmul(self.pdbl(pt), num >> 1), pt)
		return self.pointmul(self.pdbl(pt), num >> 1)
	
	def getkeypair(self):
		"""
		Generuje pare (klucz prywatny, klucz publiczny) ktore sa wykorzystane do podpisu cyfrowego wiadomosci
		"""
		if not self.basepoint:
			raise ValueError("Pare kluczy mozna wygenerowac jesli na krzywej ustalony jest punkt bazowy!")
		priv = random.randint(1, self.p)
		pub = self.pointmul(self.basepoint, priv)
		return (priv, pub)
	
	def sign(self, privatekey, msg, hashfunc = hashlib.sha256):
		""" Zwraca podpis cyfrowy wiadomosci za pomoca klucza prywatnego na krzywej """
		if not self.basepoint or not self.order:
			raise ValueError("Podpis cyfrowy moze byc uzywany jesli na krzywej ustalony jest punkt bazowy!")
		r = random.randint(1, self.order - 1)
		rpt = self.pointmul(self.basepoint, r)
		rx = rpt.x % self.order
		if isinstance(msg, str):
			msg = msg.encode()
		hnum = int(hashfunc(msg).hexdigest(), 16) % self.order
		s = pow(r, -1, self.order) * (hnum + rx * privatekey) % self.order
		return (rx, s)
		
	def verify(self, publickey, msg, sig, hashfunc = hashlib.sha256):
		""" Sprawdza poprawnosc podpisu cyfrowego """
		if not self.basepoint or not self.order:
			raise ValueError("Podpis cyfrowy moze byc uzywany jesli na krzywej ustalony jest punkt bazowy!")
		r, s = sig
		c = pow(s, -1, self.order)
		if isinstance(msg, str):
			msg = msg.encode()
		hnum = int(hashfunc(msg).hexdigest(), 16) % self.order
		u1 = hnum * c % self.order
		u2 = r * c % self.order
		pt = self.pointadd(self.pointmul(self.basepoint, u1), self.pointmul(publickey, u2))
		if pt == self.inf:
			return False
		return r == pt.x % self.order
	
	def recovery(self, x):
		"""
		Na podstawie wartosci x koordynaty punktu zwraca odpowiadajaca jej wartosc y taka, ze punkt (x, y) lezy na krzywej
		Nie dla kazdej wartosci x istnieje odpowiadajacy mu y
		Jesli punkt o wartosci x istnieje na krzywej, funkcja zwraca dwa punkty: (x, y) oraz (x, -y)
		"""
		val = (x ** 3 + self.a * x + self.b) % self.p
		if not hasmodularsqrt(val, self.p):
			raise ValueError("Na krzywej nie istnieje punkt o podanej koordynacie x")
		vv = modularsqrt(val, self.p)
		return [point(x, vv[0]), point(x, vv[1])]	
		
	def randpoint(self):
		""" Zwraca losowy punkt lezacy na krzywej """
		while True:
			try:
				x = random.randint(1, self.p)
				res = self.recovery(x)
				return res[random.randint(0, 1)]
			except:
				pass
	
	def recoverpub(self, msg, sig, hashfunc = hashlib.sha256):
		"""
		Na podstawie wiadomosci oraz jej podpisu cyfrowego odzyskuje klucz publiczny odpowiadajacy kluczowi prywatnemu, ktorym zostala podpisana dana wiadomosc
		Zwracane sa dwa potencjalne klucze, oba poprawnie weryfikuja dana wiadomosc
		"""
        if not self.basepoint or not self.order:
			raise ValueError("Algorytm odzyskiwania klucza publicznego z podpisu moze byc zasotosowany jesli na krzywej ustalony jest punkt bazowy!")
		r, s = sig
		if isinstance(msg, str):
			msg = msg.encode()
		hnum = int(hashfunc(msg).hexdigest(), 16) % self.order
		val = (r ** 3 + self.a * r + self.b) % self.p
		vv = modularsqrt(val, self.p)
		pt1 = point(r, vv[0])
		pt2 = point(r, vv[1])
		rm = pow(r, -1, self.order)
		pub1 = self.pointmul(self.pointsub(self.pointmul(pt1, s), self.pointmul(self.basepoint, hnum)), rm)
		pub2 = self.pointmul(self.pointsub(self.pointmul(pt2, s), self.pointmul(self.basepoint, hnum)), rm)
		return [pub1, pub2]