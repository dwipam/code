class Node:
	def __init__(self, key):
		self.key = key
		self.next = None
		self.visited = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, key):
		n = Node(key)
		n.next = self.head
		self.head = n

	def traverse(self):
		temp = self.head
		while temp:
			print temp.key
			temp = temp.next

	def counter(self):
		cnt = 0
		temp = self.head
		while temp:
			cnt+=1
			temp = temp.next
		return cnt

li = LinkedList()
li.push(3)
li.push(6)
li.push(9)
li.push(15)
li.push(30)
li.traverse()

print "\n"
l2 = LinkedList()
l2.push(10)
l2.head.next = li.head.next.next
l2.traverse()

def find_intersection():
	c1 = li.counter()
	c2 = l2.counter()
	d = abs(c1 - c2)

	cnt = 0
	if c1 > c2:
		temp = li.head
	else:
		temp = l2.head
	while cnt <= d:
		cnt+=1
		temp = temp.next
	print "Intersection key: ",temp.key

find_intersection()







