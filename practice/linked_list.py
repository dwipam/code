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

	def pop_key(self, key):
		temp = self.head.next
		prev = self.head
		if prev.key == key:
			self.pop()
		while temp!=None:
			if temp.key == key:
				print "\n Deleted: ",key
				prev.next = temp.next
				temp = None
				return
			prev = temp
			temp = temp.next

	def delete_linked_list(self):
		print "\n Deleting Linked List"
		while self.head:
			temp = self.head
			self.head = self.head.next
			temp = None

	def len(self):
		cnt = 0
		temp = self.head
		while temp:
			cnt+=1
			temp = temp.next
		print "Length: ", cnt

	def middle(self):
		print "Middle"
		temp1 = self.head
		temp2 = self.head
		while temp2.next:
			temp2 = temp2.next.next
			temp1 =	temp1.next
		print temp1.key

	def count_key(self, key, temp, freq=0):
		if not temp:
			return freq
		if temp.key == key:
			freq+=1
		return self.count_key(key, temp.next, freq)

list_ = LinkedList()
list_.push(2)
list_.push(5)
list_.push(8)
list_.push(9)
list_.push(1)
list_.push(4)
list_.push(6)
list_.push(4)
list_.push(7)
print list_.search(10)
print list_.search(2)
list_.traverse()
list_.pop()
print "\n"
list_.traverse()
list_.pop_key(6)
print "\n"
list_.traverse()
list_.len()
list_.middle()
print "Number of Times Key occur: ",list_.count_key(4, list_.head)
list_.delete_linked_list()
list_.traverse()
list_.len()




