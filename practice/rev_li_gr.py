class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None


def revere(n1,n):
    hold = cur = n1
    begin = cur;temp = cur
    i = 0
    while cur:
        i+=1
        if i%n==0:
            import pdb;pdb.set_trace()
            temp = reverseK(begin,cur)
            cur = temp;
        cur = cur.next
    return hold

def reverseK(begin,end):
    first = begin
    prev = Node(None)
    next = cur = begin
    while (cur != end):
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    begin = prev
    first.next = cur
    return first

n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(4)
x = revere(n1,2)
while x:
    print x.val
    x = x.next
