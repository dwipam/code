def jumps(a,l,h):
    if a[l]==0:
        return 999999
    if h == l:
        return 0
    mn = 99999
    for i in range(len(a))[l+1:]:
        if i <= l+a[l] and i<= h:
            jump = jumps(a,i,h)
            if mn > jump+1 and jump != 9999:
                mn = jump+1
    return mn
print jumps([1, 3, 6, 3, 2, 3, 6, 8, 9, 10],0,len([1, 3, 6, 3, 2, 3, 6, 8, 9, 10])-1)
        
