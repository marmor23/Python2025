def gcd(a, b):
	while b:
		a, b, = b, a % b
	return a

def checkvalid(frac):
	if frac[1] == 0:
		raise ValueError("Mianownik nie moze byc zerem!")

def simplify(frac):
	g = gcd(frac[0], frac[1])
	return [frac[0] // g, frac[1] // g]
	
def add_frac(frac1, frac2):
	checkvalid(frac1)
	checkvalid(frac2)
	return simplify([frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]])
	
def sub_frac(frac1, frac2):
	checkvalid(frac1)
	checkvalid(frac2)
	return simplify([frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1]])
	
def mul_frac(frac1, frac2):
	checkvalid(frac1)
	checkvalid(frac2)
	return simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])
	
def div_frac(frac1, frac2):
	checkvalid(frac1)
	checkvalid(frac2)
	return simplify([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):
	checkvalid(frac)
	return frac[0] * frac[1] > 0
	
def is_zero(frac):
	checkvalid(frac)
	return frac[0] == 0
	
def cmp_frac(frac1, frac2):
	"""
	Funkcja zwraca:
	-1 jesli frac1 < frac2
	0 jesli frac1 = frac2
	1 jesli frac1 > frac2
	"""
	checkvalid(frac1)
	checkvalid(frac2)
	g = gcd(frac1[1], frac2[1])
	fv1 = frac1[0] * frac2[1] // g
	fv2 = frac2[0] * frac1[1] // g
	if fv1 > fv2:
		return 1
	elif fv2 > fv1:
		return -1
	return 0

def frac2float(frac):
	checkvalid(frac)
	return float(frac[0]) / frac[1]
