def quicksort(a,li,hi):
    if li<hi:
        q = partition(a,li,hi)
        quicksort(a,q+1,hi)
        quicksort(a,li,q-1)
def partition(a,li,hi):
    j=li-1
    for i in range(len(a))[li:len(a)-1]:
        if a[i] <= a[hi]:
            j+=1
            t = a[j]
            a[j] = a[i]
            a[i] = t
    t = a[j+1]
    a[j+1] = a[hi]
    a[hi] = t
    return j+1
a = [4,2,1,3]
quicksort(a,0,3)
print a
    
        
