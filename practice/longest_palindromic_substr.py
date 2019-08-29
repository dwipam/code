str1 = "abababa"

max_length = 1
for i in range(1,len(str1)-1):
	k = i
	l = i
	while k>=0 and l<=len(str1)-1 and str1[l] == str1[k]:
		k-=1
		l+=1
	max_length = max(l-1-k, max_length)
print max_length
