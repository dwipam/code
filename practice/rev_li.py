class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse(N1):
    temp = N1
    prev = Node(None)
    cur  = N1
    while cur:
        next = cur.next
        cur.next= prev
        prev = cur
        cur = next        
    return prev
n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
x = reverse(n1)
while x:
    print x.val
    x = x.next


