k = 2
x = [1,2,3,4,5]
temp = x[:k]
for i in range(k,len(x)):
    _ =999999
    minindex = 0
    for j in range(len(temp)):
        if _ > temp[j]:
            _ = temp[j]
            minindex = j
    if temp[minindex]<x[i]:
        temp[minindex] = x[i]
print temp
        
