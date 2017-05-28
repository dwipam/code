def tri():
    x = [1, 4, 45, 6, 10, 8]
    y = 22
    x = sorted(x)
    for i in range(len(x)):
        q = i+1; r = len(x)-1
        while q<r :
            if x[q]+x[r] < y-x[i]:
                q+=1 
            elif x[q]+x[r] > y-x[i]:
                r-=1
            else:
                return (x[i],x[q],x[r])
    return "Nothing Found"
print tri()
        
