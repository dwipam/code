def minDist(a,x,y):
    prev = 0
    for i in a:
        if i == x or i == y:
            break
        prev+=1
    dist = 99999
    for i in range(prev,len(a)):
        if a[i]!=a[prev] and (a[i] == x or a[i] == y) and i-prev < dist:
            dist = i-prev
            prev = i
        else:
            prev = i

    print dist
minDist([3, 4, 5],3,5)
