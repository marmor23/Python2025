import random

def bisprime(num, ntrial = 10):
	# Sprawdzanie, czy liczba jest pierwsza (algorytm dziala na bazie malego twierdzenia Fermata)
	if num in [2, 3]: return True
	if num < 5: return False
	for i in range(ntrial):
		r = random.randrange(2, num - 2)
		if pow(r, num - 1, num) != 1:
			return False
	return True

def tonelli(x, p):
	# Oblicza pierwiastek modularny algorytmem Tonelliego-Shanksa
	q = p - 1
	s = 0
	while q & 1 == 0:
		q = q >> 1
		s += 1
	z = 2
	while legendre(z, p) == 1:
		z += 1
	m = s
	c = pow(z, q, p)
	t = pow(x, q, p)
	r = pow(x, (q + 1) >> 1, p)
	while t != 1:
		for i in range(1, m):
			if pow(t, 2**i, p) == 1:
				break
		b = pow(c, 2 ** (m - i - 1), p)
		m = i
		c = b * b % p
		t = (t * c) % p
		r = (r * b) % p
	return [r, p - r]
	
def legendre(x, p):
	# Zwraca symbol Legendre'a dla x i liczby pierwszej p
	return pow(x, p >> 1, p)
	
def hasmodularsqrt(x, p):
	# Sprawdza czy istnieje liczba a, taka ze a jest calkowite oraz a^2 (mod p) = x
	return legendre(x, p) == 1
	
def modularsqrt(x, p):
	# Zwraca liste liczb a takich ze a^2 (mod p) = x
    if not bisprime(p):
        raise ValueError("Liczba p musi byc pierwsza!")
	if not hasmodularsqrt(x, p):
		raise ValueError("Nie istnieje zadna liczba spelniajaca rownanie")
	if p & 3 == 3:
		# W takim przypadku mozna szybko obliczyc pierwiastek modularny
		sol = pow(x, (p + 1) >> 2, p)
		return [sol, p - sol]
	if p & 7 == 5:
		# W takim przypadku mozna szybko obliczyc pierwiastek modularny
		aa = pow(x << 1, (p - 5) >> 3, p)
		bb = 2 * x * aa * aa % p
		sol = x * aa * (bb - 1) % p
		return [sol, p - sol]
	# W przeciwnym razie nalezy wykorzystac algorytm Tonelliego-Shanksa
	return tonelli(x, p)