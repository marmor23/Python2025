import os

# 2.9
def copyfile(name, dest):
	f = open(name, "rb")
	data = f.read().split(os.linesep.encode())
	f.close()
	out = os.linesep.encode().join([i for i in data if len(i) and not i.startswith(b"#")])
	f = open(dest, "wb")
	f.write(out)
	f.close()
	
# 2.10
wcount = lambda line: len([i for i in line.split() if len(i)])

# 2.11
dispunderscore = lambda word: "_".join([i for i in word])

# 2.12
getwords = lambda word: [i for i in word.split() if len(i)]
getfirst = lambda word: "".join([i[0] for i in getwords(word)])
getlast = lambda word: "".join([i[-1] for i in getwords(word)])

# 2.13
getwordsum = lambda line: sum([len(i) for i in getwords(line)])

# 2.14
def getmaxwordandsize(line):
	mx = max(getwords(line), key=len)
	return mx, len(mx)
	
# 2.15
getnumstr = lambda l: "".join([str(i) for i in l])

# 2.16
repgvr = lambda line: line.replace("GvR", "Guido van Rossum")

# 2.17
def spsort(line):
	words = getwords(line)
	return sorted(words), sorted(words, key=len)
	
# 2.18
getzerocount = lambda num: str(num).count("0")

# 2.19
getthreedigitstr = lambda l: "".join([str(i).zfill(3) for i in l])



# test 2.10
multstr = """
aa bb\tccc

ddd"""
assert wcount(multstr) == 4

# test 2.11
word = "testpython123"
assert dispunderscore(word) == "t_e_s_t_p_y_t_h_o_n_1_2_3"

# test 2.12
line = """Litwo Ojczyzno moja ty jestes jak zdrowie
Ile cie trzeba cenic ten tylko sie dowie
Kto cie stracil Dzis pieknosc twa w calej ozdobie
Widze i opisuje bo tesknie po tobie"""

assert getfirst(line) == "LOmtjjzIctcttsdKcsDptwcoWiobtpt"
assert getlast(line) == "ooayskeeeacnoeeoelscawjeeieoeoe"

# test 2.13
assert getwordsum(line) == 138

# test 2.14
mxword, siz = getmaxwordandsize(line)
assert mxword == "Ojczyzno"
assert siz == 8

# test 2.15
l = [1, 10, 345, 78, 99, 203]
assert getnumstr(l) == "1103457899203"

# test 2.16
txt = "aaaGvRbbb"
assert repgvr(txt) == "aaaGuido van Rossumbbb"

# test 2.17
srtalph, srtsiz = spsort(line)
# sortowanie alfabetyczne - wyrazy zaczynajace sie z duzej litery maja priorytet bo maja mniejszy kod ascii
assert srtalph == ['Dzis', 'Ile', 'Kto', 'Litwo', 'Ojczyzno', 'Widze', 'bo', 'calej', 'cenic', 'cie', 'cie', 'dowie', 'i', 'jak', 'jestes', 'moja', 'opisuje', 'ozdobie', 'pieknosc', 'po', 'sie', 'stracil', 'ten', 'tesknie', 'tobie', 'trzeba', 'twa', 'ty', 'tylko', 'w', 'zdrowie']
assert srtsiz == ['w', 'i', 'ty', 'bo', 'po', 'jak', 'Ile', 'cie', 'ten', 'sie', 'Kto', 'cie', 'twa', 'moja', 'Dzis', 'Litwo', 'cenic', 'tylko', 'dowie', 'calej', 'Widze', 'tobie', 'jestes', 'trzeba', 'zdrowie', 'stracil', 'ozdobie', 'opisuje', 'tesknie', 'Ojczyzno', 'pieknosc']

# test 2.18
num = 154890327873203280111
assert getzerocount(num) == 3

# test 2.19
l = [1, 45, 56, 102, 849, 43, 2]
assert getthreedigitstr(l) == "001045056102849043002"

print("Wszystkie testy zakonczyly sie pomyslnie")
