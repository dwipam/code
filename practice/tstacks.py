class tStacks(object):
    def __init__(self):
        self.t1 = -1
        self.t2 = 10
        self.a = [None]*self.t2
    def push1(self,n):
        if self.t1 < self.t2 -1:
            self.t1+=1
            self.a[self.t1] = n
        else: print "Overflow"
    def push2(self,n):
        if self.t1 < self.t2-1:
            self.t2-=1
            self.a[self.t2] = n
        else: print "Overflow"
    def pop1(self):
        if self.t1>= 0:
            print self.a[self.t1]
            self.t1-=1
        else: print "Underflow"
    def pop2(self):
        if self.t2<10:
            print self.a[self.t2]
            self.t2+=1
        else: print "Underflow"


t = tStacks()
t.push1(10)
t.push2(20)
t.pop1()
t.pop2()
t.pop1()
t.pop2()
        
    
