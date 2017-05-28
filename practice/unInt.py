x = [1,2,3,4]
y = [3,4]
temp = []
i =j = 0
while i<len(x) and j < len(y):
    if x[i] < y[j]:
        temp.append(x[i])
        i+=1
    elif x[i] == y[j]: 
        temp.append(y[j])
        i+=1
        j+=1
    else:
        temp.append(y[j])
        j+=1
temp+=x[i:]
temp+=y[j:]
print temp
