class Celeb(object):
    def __init__(self, relation):
        self.relation = relation
    def knows(self,A,B):
        return self.relation[A][B]
    def getHost(self):
        people = [ i for i in range(len(self.relation))]
        A = people.pop(0)
        B = people.pop(0)
        while len(people) > 1:
            if self.knows(A,B):
                A = people.pop(0)
            else:
                B = people.pop(0)
        C = people.pop(0)
        if self.knows(C,A):
            C = A
        if self.knows(C,B):
            C = B
        return C

relation = [[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,0]]
c = Celeb(relation)
print c.getHost()
                
