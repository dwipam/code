a = "ABCDGH"
b = "AEDFHR"


arr = [[0]*(len(a)+1)]*(len(b)+1)
for i in range(len(b)+1):
	for j in range(len(a)+1):
		if i == 0 or j == 0:
			arr[i][j] = 0
		if b[i-1] == a[j-1]:
			arr[i][j] = arr[i][j-1]+1
		else:
			arr[i][j] = max(arr[i][j-1], arr[i-1][j])
print arr[len(b)][len(a)]


