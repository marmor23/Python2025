import random

# a)
def iterbin():
	x = 0
	while True:
		yield x
		x ^= 1

# b)
def iterdir():
	while True:
		yield random.choice(["N", "E", "S", "W"])
		
# c)
def iterdayweek():
	x = 0
	while True:
		yield x % 7
		x += 1
		

it1 = iterbin()
for i in range(20):
	print(next(it1), end = " ")
	
print()

it2 = iterdir()
for i in range(20):
	print(next(it2), end = " ")
	
print()

it3 = iterdayweek()
for i in range(20):
	print(next(it3), end = " ")
	
print()
