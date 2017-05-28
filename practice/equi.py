x = [-7,6,1,-7,6]
tot = sum(x)
lef = 0
for i in x:
    tot = tot-i
    if lef == tot:
        print i
    lef = lef+i

