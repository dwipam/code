from random import random
def weightGet(px,py,pz,n):
    for i in range(n):
        num = random()
        if num <= px:
            print "1"
        elif num <= px+py:
            print "2"
        else: print "3"
weightGet(0.25,0.25,0.5,20)
    
