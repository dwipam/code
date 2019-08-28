str1 = "Sunday"
str2 = "Monday"

def edit_distance(str1, str2):
	m = len(str1)
	n = len(str2)
	dist = [[0 for i in range(m+1)] for i in range(n+1)]
	for i in range(n+1):
		for j in range(m+1):
			if i==0:
				dist[i][j] == j
			if j==0:
				dist[i][j] == i
			elif str1[i-1] == str2[j-1]:
				dist[i][j] = dist[i-1][j-1]
			else:
				dist[i][j] = 1 + min(dist[i-1][j],dist[j-1][i],dist[i-1][j-1])
	return dist[n][m]
print edit_distance(str1, str2)
