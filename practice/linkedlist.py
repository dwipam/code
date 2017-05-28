class Node(object):
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node
class operations(object):
    def traverse(self,node):
        
        while node.next_node != None:
            print node.data
            node = node.next_node

if __name__=='__main__':
    N1 = Node(1)
    N2 = Node(2)
    N3 = Node(3)
    N1.next_node = N1
    N2.next_node = N2
    N2.next_node = N3
    operations.traverse(N1)

