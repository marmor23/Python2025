from doublelist import DoubleList, Node
import pytest

dl = DoubleList()
dl.insert_head(Node(5))
dl.insert_head(Node(6))
dl.insert_tail(Node(1))
dl.insert_head(Node(7))
dl.insert_head(Node(8))
dl.insert_tail(Node(1))
dl.insert_tail(Node(3))
dl.insert_tail(Node(9))
dl.insert_tail(Node(-10))
dl.insert_tail(Node(4))
dl.insert_tail(Node(1))
dl.insert_head(Node(1))

dl2 = DoubleList()
dl2.insert_head(Node(-1.768))
dl2.insert_head(Node(-3.34))
dl2.insert_head(Node(54.232))
dl2.insert_head(Node(-2.14))
dl2.insert_head(Node(-7.331))
dl2.insert_head(Node(0.01))
dl2.insert_tail(Node(7.123))
dl2.insert_tail(Node(8.0))
dl2.insert_tail(Node(6.123))
dl2.insert_tail(Node(9.789))
dl2.insert_tail(Node(1.15))

def test_findmax():
	assert dl.find_max() == Node(9)
	assert dl2.find_max() == Node(54.232)

def test_findmin():
	assert dl.find_min() == Node(-10)
	assert dl2.find_min() == Node(-7.331)
	
def test_remove():
	dl.remove(Node(1))
	assert dl.count() == 8
	assert dl.remove_head() == Node(8)
	assert dl.remove_tail() == Node(4)
	dl2.remove(Node(0.01))
	dl2.remove(Node(54.232))
	assert dl2.count() == 9
	assert dl2.find_max() == Node(9.789)
	assert dl2.remove_head() == Node(-7.331)
	assert dl2.remove_tail() == Node(1.15)

def test_clear():
	dl2.clear()
	assert dl2.count() == 0
	assert dl2.head == None
	assert dl2.tail == None
    
if __name__ == "__main__":
	pytest.main()