x = [1,2,2,3,4,5]
for i in range(len(x)):
    if x[abs(x[i])]>=0:
        x[abs(x[i])] = x[abs(x[i])]*-1
    else:
        print abs(x[i])

