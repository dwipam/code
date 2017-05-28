max = -9999999
second = -9999999
for i in [4,10,100,99]:
    if i>max:
        second = max
        max = i
    elif i>second and i!=max:
        second =i 
print (max,second)
        
