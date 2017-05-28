x = [1,1,0,0,1,1,1,0]
j = 0
for i in range(len(x)):
    if x[i] == 0:
        t = x[j]
        x[j] = x[i]
        x[i] = t
        j+=1
print x
