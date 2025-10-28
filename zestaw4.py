# 4.2

# W poprzednim zestawie rowniez napisalem te zadania jako funkcje ktore zwracaja pelny string

def make_ruler(n):
	return "|" + "....|" * n + "\n0" + "".join([str(i).rjust(5, " ") for i in range(1, n + 1)])
	
def make_grid(rows, cols):
	ln = "+" + "---+" * cols
	ln2 = "|" + "   |" * cols
	out = (ln + "\n" + ln2 + "\n") * rows + ln
	return out
	
# 4.3

def factorial(n):
	if n < 0:
		raise ValueError("Argument silni musi byc nieujemny")
	res = 1
	for i in range(2, n + 1):
		res = res * i
	return res
	
# 4.4

def fibonacci(n):
	if n < 1:
		raise ValueError("Numery wyrazow ciagu zaczynaja sie od 1")
	if n < 3:
		return n - 1
	x = [0, 1]
	for i in range(n - 1):
		x[0], x[1] = x[1], x[0] + x[1]
	return x[0]

# 4.5

def odwracanieiter(L, left, right):
	x = left
	y = right
	while x < y:
		L[x], L[y] = L[y], L[x]
		x += 1
		y -= 1
	return L

def odwracanierek(L, left, right):
	if left >= right:
		return L
	L[left], L[right] = L[right], L[left]
	return odwracanierek(L, left + 1, right - 1)
	
# 4.6

def sum_seq(sequence):
	res = 0.0
	for item in sequence:
		if isinstance(item, (list, tuple)):
			res += sum_seq(item)
		elif isinstance(item, (int, float)):
			res += item
		else:
			raise ValueError("Sekwencja zawiera niedozwolony typ")
	return res
	
# 4.7

def flatten(sequence):
	res = []
	for item in sequence:
		if isinstance(item, (list, tuple)):
			res += flatten(item)
		elif isinstance(item, (int, float)):
			res.append(item)
		else:
			raise ValueError("Sekwencja zawiera niedozwolony typ")
	return res
