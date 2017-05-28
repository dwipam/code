def merge(x,y):
    i=j=z=0;
    t = []
    while i <= len(x)-1 and j <=len(y)-1:
        if x[i] < y[j]:
            t.append(x[i])
            i+=1
        else:
            t.append(y[j])
            j+=1
    
    return t+(x[i-2:]or y[j-1:])

print(merge([1],[2,3]))
    
