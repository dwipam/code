def quicksort(a,li,hi):
    if li<hi:
        q = partition(a,li,hi)
        quicksort(a,q+1,hi)
        quicksort(a,li,q-1)
def partition(a,li,hi):
    j=li-1
    for i in range(len(a))[li:hi]:
        if a[i] <= a[hi]:
            j+=1
            t = a[j]
            a[j] = a[i]
            a[i] = t
    t = a[j+1]
    a[j+1] = a[hi]
    a[hi] = t
    return j+1

a = [10, 80, 30, 90, 40, 70, 50]
quicksort(a,0,len(a)-1)
print a