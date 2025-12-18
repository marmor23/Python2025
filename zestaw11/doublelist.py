class Node:
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

	def __str__(self):
		return str(self.data)

	def __eq__(self, other):
		return self.data == other.data

	def __ne__(self, other):
		return not self == other
		
class DoubleList:
	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None

	def is_empty(self):
		#return self.length == 0
		return self.head is None

	def count(self):
		return self.length

	def insert_head(self, node):
		if self.head:
			node.next = self.head
			self.head.prev = node
			self.head = node
		else:
			self.head = node
			self.tail = node
		self.length += 1

	def insert_tail(self, node):
		if self.tail:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
		else:
			self.head = node
			self.tail = node
		self.length += 1

	def remove_head(self):
		if self.is_empty():
			raise ValueError("pusta lista")
		elif self.head is self.tail:
			node = self.head
			self.head = None
			self.tail = None
			self.length = 0
			return node
		else:
			node = self.head
			self.head = self.head.next
			self.head.prev = None
			node.next = None
			self.length -= 1
			return node

	def remove_tail(self):
		if self.is_empty():
			raise ValueError("pusta lista")
		elif self.head is self.tail:
			node = self.tail
			self.head = None
			self.tail = None
			self.length = 0
			return node
		else:
			node = self.tail
			self.tail = self.tail.prev
			self.tail.next = None
			node.prev = None
			self.length -= 1
			return node
			
	def find_max(self):
		if self.is_empty():
			return None
		tmp = self.head
		res = tmp
		while tmp:
			if tmp.data > res.data:
				res = tmp
			tmp = tmp.next
		return res
	
	def find_min(self):
		if self.is_empty():
			return None
		tmp = self.head
		res = tmp
		while tmp:
			if tmp.data < res.data:
				res = tmp
			tmp = tmp.next
		return res
	
	def remove(self, node):
		# Usuwa wszystkie wystapienia node w liscie
		if node == self.head:
			self.remove_head()
			self.remove(node)
		elif node == self.tail:
			self.remove_tail()
			self.remove(node)
		tmp = self.head
		while tmp:
			if tmp == node:
				tmp.prev.next = tmp.next
				tmp.next.prev = tmp.prev
				self.length -= 1
			tmp = tmp.next
	
	def clear(self):
		self.length = 0
		self.head = None
		self.tail = None