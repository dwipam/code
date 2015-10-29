"""
Analysis of implementation:

There are essentially two implementations:
    1)  In this implementation, we try to calculate the edges of the tree. Once we have the edges, we follow the
        below algorithm of **Gradient Descent**.
            -   Start with a random state. (In the first run, the tree is laid out in a way that the BFS iteration
                yields the numbers 1 to N sequentially.
            -   Populate the edges, and calculate the weight of the edges as the absolute difference between the
                nodes it is connecting.
            -   Add all the edges to an array. Remove the largest edge from the array.
            -   Iterate over the remainder edges:
                -   For every edge, check if any of the node-values fall within the range represented by the maximum edge:
                    -   Since there is an overlap (on the number line) of the 4 numbers represented by current edge and 
                        maximum edge, swap the values so that they no longer overlap. This leads to minimisation of overall
                        edge values.
                    -   Calculate the new value of the tree. This is the value given by the successor function.
            -   Through course of all iterations, check for the edge that leads to a minimum overall tree value.
            -   Swap the edges so that the overall value of the tree is equal to the new minimum
            -   If there is no new minimum overall value, we have entered a local minima. In this case, shuffle the
                values in the tree and restart.
            -   Store the minimum value through all these iterations and print it out.
    2)  This is fairly straightforward implementation meant only for smaller depths. This essentially generates all
        possible combinations and try to search the one with minimum possible value.

Results:
    1) For k=3
        Minimised Maximum Value: 3
        Arrangement: 4 1 5 7 2 3 6 8 9 10
        Time Taken: 146 seconds
    
"""


from itertools import takewhile, permutations
import random
import sys
from Queue import PriorityQueue

DEPTH = 0
MAX_MINIMAS = 2

class Node(object):
    def __init__(self, value, parent=None, depth=1):
        self.value = value
        self.left = None
        self.right = None
        self.middle = None
        self.parent = parent
        self.depth = depth

    def __repr__(self):
        children = [x for x in [self.left, self.middle, self.right] if x]
        return "\t"*(self.depth-1) + "%d"%self.value + "\n" + "\n".join(map(repr, children))

    @staticmethod
    def swap(node1, node2):
        node1.value, node2.value = node2.value, node1.value

class Edge(object):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.sorted_node1 = min(node1, node2, key=lambda x: x.value)
        self.sorted_node2 = max(node1, node2, key=lambda x: x.value)
    
    def value(self):
        return abs(self.node1.value - self.node2.value)
    
    def __repr__(self):
        return "Edge: %d => %d"%(self.node1.value, self.node2.value)

def gen_tree_depth(node, max_depth):
    if node.depth > max_depth-1:
        return None
    if node.depth == 1:
        node.left = Node(0, parent=node, depth=node.depth+1)
        node.middle = Node(0, parent=node, depth=node.depth+1)
        node.right = Node(0, parent=node, depth=node.depth+1)
        gen_tree_depth(node.left, max_depth)
        gen_tree_depth(node.middle, max_depth)
        gen_tree_depth(node.right, max_depth)
    else:
        node.left = Node(0, parent=node, depth=node.depth+1)
        node.right = Node(0, parent=node, depth=node.depth+1)
        gen_tree_depth(node.left, max_depth)
        gen_tree_depth(node.right, max_depth)
 
def bfs_iter(node):
    queue = [node]
    while queue:
        curNode = queue.pop(0)
        queue += filter(lambda x: x is not None, [curNode.left, curNode.middle, curNode.right])
        yield curNode

def fill_tree(root, arr):
    for node, value in zip(bfs_iter(root), arr):
        node.value = value
 

def get_all_edges(node):
    res = []
    for node in bfs_iter(node):
        if node.left:
            res.append(Edge(node, node.left))
        if node.middle:
            res.append(Edge(node, node.middle))
        if node.right:
            res.append(Edge(node, node.right))
    return res

def eval_tree(root):
    return max(get_all_edges(root), key=lambda x: x.value())

def apply_aggr_fn(node, fn=max):
    m = lambda x: abs(x[0].value - x[1].value)
    children = [x for x in (node.left, node.middle, node.right) if x is not None]
    if not children:
        return None
    maxEdge = fn(zip(children, [node]*3), key=m)
    for child in children:
        childMax = apply_aggr_fn(child, fn)
        if childMax:
            maxEdge = fn(maxEdge, childMax, key=m)
    nodes = sorted([maxEdge[0], maxEdge[1]], key=lambda x: x.value)
    return nodes[0], nodes[1]

def get_tree(d):
    root = Node(0)
    gen_tree_depth(root, d)
    return root

def search(root):
    overlap = lambda e1, e2:    e2.sorted_node1.value < e1.sorted_node1.value < e2.sorted_node2.value or \
                                e2.sorted_node1.value < e1.sorted_node2.value < e2.sorted_node2.value or \
                                e1.sorted_node1.value < e2.sorted_node1.value < e1.sorted_node2.value or \
                                e1.sorted_node1.value < e2.sorted_node2.value < e1.sorted_node2.value
    max_val = 10**8

    seen_minimas = PriorityQueue()

    while True:
        if len(seen_minimas.queue) == MAX_MINIMAS:
            break
        #import pdb; pdb.set_trace()
        print root
        edges = get_all_edges(root)
        max_edge = max(edges, key=lambda x: x.value())
        max_edge_val = max_edge.value()
        edges.remove(max_edge)
        
        candidate_edges = PriorityQueue()

        for edge in edges:
            if overlap(max_edge, edge):
                Node.swap(max_edge.sorted_node1, edge.sorted_node2)

                largest_edge = eval_tree(root)

                print "Tree Value: ", largest_edge.value()
                if max_edge_val > largest_edge.value():
                    print "Adding to the queue."
                    candidate_edges.put((largest_edge.value(), largest_edge))
                
                Node.swap(max_edge.sorted_node1, edge.sorted_node2)
        
        if not len(candidate_edges.queue):
            seen_minimas.put((eval_tree(root).value(), root))
            new_root = get_tree(DEPTH)
            nodes_value = [x.value for x in bfs_iter(root)]
            random.shuffle(nodes_value)
            fill_tree(new_root, nodes_value)
            root = new_root
            print "Generated a new configuration."
            #import pdb; pdb.set_trace()
        else:
            min_value, edge = candidate_edges.queue[0]
            min_value_edges = list(takewhile(lambda x: x[0] == min_value, candidate_edges.queue))
           
            edge = random.choice(min_value_edges)[1]

            print "Swapping: ", max_edge, edge
            Node.swap(max_edge.sorted_node1, edge.sorted_node2)

            print "\n\nLatest Tree Evaluation:", eval_tree(root)
        
    return seen_minimas.get()[1]


def searchAll(root):
    values = [x.value for x in bfs_iter(root)]

    min_value = (100, None)
    for value_arr in permutations(values):
        root = get_tree(DEPTH)
        fill_tree(root, value_arr)

        tree_value = eval_tree(root)

        if tree_value.value() < min_value[0]:
            min_value = (tree_value.value(), [x.value for x in bfs_iter(root)])
            print min_value[0]
            print " ".join(map(str, min_value[1]))
    return min_value[1]


def main():
    global DEPTH
    DEPTH = int(sys.argv[1])
    root = get_tree(DEPTH)
    fill_tree(root, range(1, 3*(2**(DEPTH-1)) + 1))
    print root
    if DEPTH > 4:
        search(root)
    else:
        print searchAll(root)



if __name__ == '__main__':
    main()

