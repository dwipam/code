 = [0, -10, 2, 10, -20]
def seag(x):
    j = 0
    for i in range(len(x))[1:]:
        if x[i] < 0:
            t = x[j]
            x[j] = x[i]
            x[i] = t
            j+=1
    return j
def small(x):
    for i in range(len(x)):
        if abs(x[i]) < len(x) and x[i] >= 0:
            x[x[i]] = -x[x[i]]
    import pdb;pdb.set_trace()
    for i in range(len(x)):
        if x[i] > 0:
            print i
j = seag(x)
small(x[j:])
print x
