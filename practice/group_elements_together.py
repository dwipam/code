
k = 3
a = [2, 1, 5, 6, 3]


diff_a = []
for i in range(len(a)):
	diff_a.append(a[i] - k)

idx = a
for j in range(len(diff_a)):
	for i in range(len(diff_a)-1):
		if diff_a[i] > diff_a[i+1]:
			temp = diff_a[i+1]
			diff_a[i+1] = diff_a[i]
			diff_a[i] = temp

			temp = idx[i+1]
			idx[i+1] = idx[i]
			idx[i] = temp
print idx
print diff_a

