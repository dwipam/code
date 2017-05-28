def _(a):
    for i in a:
        if a[i-1]>0:
            a[i-1] = -a[i-1]
        else:
            print abs(i)
_([1,3,3,3,1])
