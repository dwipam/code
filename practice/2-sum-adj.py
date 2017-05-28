arr=[5, 5, 10, 100, 10, 5]
incl = 0
excl = 0
for i in arr:
    new_excl = excl if excl>incl else incl
    incl = excl + i
    excl = new_excl

for i in range(len(arr))[2:]:
    arr[i] = max(arr[i],arr[i-2]+arr[i])
print max(arr[len(arr)-2],arr[len(arr)-1])
