def overLoop(a):
    x = [1]*len(a)
    for i in range(len(a)):
        x[i] = innerLoop(a,x,i)
    return x

def innerLoop(a,x,i):
   # import pdb;pdb.set_trace()
    for j in range(len(a))[:i]:
        if a[j] < a[i]:
            x[i]  = max(x[i],x[j]+1)
    return x[i]


print overLoop([3,4,-1,0,6,2,3])
