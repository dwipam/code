a = [54, 546, 548, 60]

for j in range(len(a)):
	for i in range(len(a)-1):
		if str(a[i])+str(a[i+1]) < str(a[i+1]) + str(a[i]):
			temp = a[i]
			a[i] = a[i+1]
			a[i+1] = temp
print ''.join(map(lambda x : str(x),a))