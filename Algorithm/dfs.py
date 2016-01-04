"""
Author: Dwipam Katariya
Email: ddkatari@iu.edu
"""
class node(object):
	def __init__(self,value,neighbours):
		self.value=value
		self.neighbours=neighbours

class DFSSearch(object):
	def __init__(self):
		self.fringe=[]
		self.traversal=[]
	def push(self,value,neighbours):
		node_obj = node(value,neighbours)
		self.fringe.append(node_obj)
	def search(self):
		#import pdb;pdb.set_trace()
		while self.fringe:
			curNode = self.fringe.pop(0)
			print "Current Node:",curNode.value,"Neighbours:",curNode.neighbours
			while curNode.neighbours:
				cur_neighbours = curNode.neighbours.pop(0)
				for node_recur in self.fringe:
					if node_recur.value==cur_neighbours:
						while node_recur.neighbours: 
							self.fringe.insert(0,node(node_recur.neighbours.pop(0),))
	def search2(self,curNode):
	#	import pdb;pdb.set_trace()
		for temp_obj in self.fringe:
			if temp_obj.value == curNode:
				obj = self.fringe.pop(self.fringe.index(temp_obj))
				self.traversal.append(obj.value)
		print "Node explored",curNode,"Neighbours:",obj.neighbours
		if len(self.fringe)==0:	
			return self.traversal
		for neighbour in obj.neighbours:
			if neighbour not in self.traversal:
				self.search2(neighbour)
def main():
	dfs = DFSSearch()
	dfs.push('A',['B','E','D','G'])
	dfs.push('B',['A','E','F'])
	dfs.push('F',['B','C','D'])
	dfs.push('E',['B','G'])
	dfs.push('G',['E','A'])
	dfs.push('C',['F','H'])
	dfs.push('D',['A','F'])
	dfs.push('H',['C'])
	dfs.search2('A')
	print "Explored Nodes",dfs.traversal
if __name__=='__main__':
	main()
