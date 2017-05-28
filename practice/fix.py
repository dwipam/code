def binary(a,li,hi):
    if hi>=li:
        mid = (li+hi)/2
        if a[mid]==mid:
            return mid
        elif a[mid] > mid:
            return binary(a,li,mid-1)
        else:
            return binary(a,mid+1,hi)
    return -1

print(binary([0,2,3,4],0,3))
