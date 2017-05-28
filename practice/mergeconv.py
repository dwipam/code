def merge_sort(x):
    return merge(x,0,len(x)-1)
def merge(x,left,right):
    cnt = 0
    if left < right :
        mid = (left + right)/2
        cnt = merge(x,left,mid)
        cnt+=merge(x,mid+1,right)
        cnt+=mergeFull(x,left,mid,right)
    return cnt
def mergeFull(x,left,mid,right):
        l = x[left:mid+1]
        r = x[mid+1:right+1]
        temp = []
        i = 0;j = 0
        cnt = 0
        while i<len(l) and j<len(r):
            if l[i] < r[j]:
                temp.append(l[i])
                i+=1
            else:
                cnt+=(mid-i)
                temp.append(r[j])
                j+=1
        while i<len(l):
            temp.append(l[i])
            i+=1
        while j<len(r):
            temp.append(r[j])
            j+=1
        for i in range(len(temp)):
            x[i] = temp[i]
        return cnt

print(merge_sort([1,2,3,4]))
    
