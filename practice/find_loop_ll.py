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

	def find_loop(self):
		temp1 = self.head
		temp2 = self.head
		while temp2:
			print temp2.key
			temp1 = temp1.next
			temp2 = temp2.next.next
			if temp1 == temp2:
				print "Loop found at: ",temp1.key
				return
	def traverse(self):
		print "Traversing"
		temp = self.head
		while temp:
			print temp.key
			temp = temp.next

list_ = LinkedList()
list_.push(1)
list_.push(2)
list_.push(3)
list_.push(4)
list_.push(5)
list_.traverse()
list_.head.next.next.next = list_.head

list_.find_loop()

