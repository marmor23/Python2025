# 3.1
"""
Czy podany kod jest poprawny skladniowo w Pythonie? Jesli nie, to dlaczego?

a)
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
    
b)
for i in "axby": if ord(i) < 100: print (i)

c)
for i in "axby": print (ord(i) if ord(i) < 100 else i)
"""

"""
a) Podany kod jest poprawny. W pythonie mozna wykorzystywac nawiasy w if-ach oraz sredniki po wyrazeniach, ale nie jest to konieczne
b) Podany kod jest niepoprawny. Kolejne wyrazenia w pythonie powinny byc oddzielone za pomoca wciec (spacji lub tabulatorow), wyjatkiem jest jedno wyrazenie po dwukropku
c) Podany kod jest poprawny. Po dwukropku moze byc jedno wyrazenie bez wciecia, a wyrazenie if-else mozna zawrzec w jednej linijce
"""

# 3.2
"""
a)
L = [3, 5, 4] ; L = L.sort()

b)
x, y = 1, 2, 3

c)
X = 1, 2, 3 ; X[1] = 4

d)
X = [1, 2, 3] ; X[3] = 4

e)
X = "abc" ; X.append("d")

f)
L = list(map(pow, range(8)))
"""

"""
a) 
Funkcja sort() w zastosowaniu do listy jest typu void. W celu posortowania listy nalezy wywolac L.sort() i nie zapisywac zwracanej wartosci. W tym przypadku po przypisaniu wartosci zmienna L bedzie miec wartosc None

b)
Kod przypisuje 3 wartosci do 2 zmiennych. W pythonie jest tot zabronione, interpreter zwroci blad.

c)
Po zainicjalizowaniu zmiennej X lista danych po przecinkach bez nawiasow kwadratowych, python nada jej typ tuple zamiast list. Typ tuple jest w pythonie tylko do odczytu (niemodyfikowalny), wiec proba przypisania nowego elementu zakonczy sie bledem.

d)
Kod proboje przypisac do listy element o nieistniejacym indeksie. Rozmiar listy to 3, a wiec mozna zmieniac wartosci listy tylko na indeksach 0 - 2

e)
Zmienna X jest stringiem, na stringu nie mozna wywolac funkcji append()

f)
Funkcja pow() przyjmuje 2 lub 3 elementy. Drugim elementem funkcji map() jest lista jednoargumentowa, wiec proba zmapowania zakonczy sie bledem.
"""

# 3.3
def printnotthird():
	for i in range(31):
		if i % 3:
			print(i)
		
# 3.4
def getthirdpower():
	while True:
		tmp = input()
		if tmp == "stop":
			break
		try:
			x = float(tmp)
			print("x =", x, "x^3 =", x ** 3)
		except:
			print("Nalezy podac poprawna liczbe!")
			
# 3.5
printmiarka = lambda x:	"|" + "....|" * x + "\n0" + "".join([str(i).rjust(5, " ") for i in range(1, x + 1)])
	
# 3.6
def printrect(x, y):
	ln = "+" + "---+" * y
	ln2 = "|" + "   |" * y
	out = (ln + "\n" + ln2 + "\n") * x + ln
	return out
	
# 3.8

# a)
getcommon = lambda s1, s2: list(set([i for i in s1 if i in s2]))

# b)
getall = lambda s1, s2: list(set(s1 + s2))


# 3.9
getlistsum = lambda arr: [sum(lst) for lst in arr]
	
# 3.10

# jedna cyfra rzymska -> liczba w systemie dziesietnym
dct1 = {
	"I" : 1,
	"V" : 5,
	"X" : 10,
	"L" : 50,
	"C" : 100,
	"D" : 500,
	"M" : 1000
}

# konstruuje slownik identyczny jak dct1
dct2 = dict(zip("IVXLCDM", [1, 5, 10, 50, 100, 500, 1000]))

# konstruuje identyczny slownik jak dct1 i dct2
dct3 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

assert dct1 == dct2 and dct1 == dct3

# liczba, ktora da sie zapisac jednym znakiem w systemie rzymskim -> cyfra rzymska
revdct = {}
for xx in dct1.keys():
	revdct[dct1[xx]] = xx

# konwersja stringa zawierajacego liczbe rzymska na liczbe (int)	
def roman2int(txt):
	if any([i not in dct1.keys() for i in txt]):
		print("Argument zawiera niedozwolone znaki dla systemu rzymskiego")
		return
	res = 0
	prev = 0
	for x in txt[::-1]:
		v = dct1[x]
		if v < prev:
			v = -v
		res += v
		prev = v
	return res
