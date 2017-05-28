a = [12, 4, 78, 90, 45, 23]
inc = [1]*len(a)
dec = [1]*len(a)
for i in range(1,len(a)):
    if a[i] > a[i-1]:
        inc[i] = inc[i-1]+1
    else:
        inc[i] = 1
for i in range(len(a)-1)[::-1]:
    if a[i] > a[i+1]:
        dec[i] = dec[i+1]+1
print max([inc[i]+dec[i] for i in range(len(a))])-1
