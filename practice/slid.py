k = 3
x = [1, 2, 3, 1, 4, 5, 2, 3, 6]
for i in range(len(x)-k+1):
    print max(x[i:i+k])

