class Node:
	def __init__(self, key):
		self.key = key
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, key):
		node = Node(key)
		node.next = self.head
		self.head = node

	def pop(self):
		if self.head.next != None:
			temp = self.head
			self.head = self.head.next
			temp = None

	def search(self, search_key):
		temp = self.head
		while temp != None:
			if temp.key == search_key:
				return "Found"
			temp = temp.next
		return "Not Found"

	def traverse(self):
		temp = self.head
		while temp != None:
			print temp.key
			temp = temp.next

list_ = LinkedList()
list_.push(2)
list_.push(5)
list_.push(8)
list_.push(9)
list_.push(1)
list_.push(3)
list_.push(6)
list_.push(4)
list_.push(7)
print list_.search(10)
print list_.search(2)
list_.traverse()
list_.pop()
print "\n"
list_.traverse()


