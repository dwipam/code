a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

"""
-4,1,2,3,-1,4
-4,1,-1,2,3,4

-5, -2, 5, 2, 4, 7, 1, 8, 0, -8
-5, 5, -2, 2, -8, 4, 7, 1, 8, 0
"""

for i in range(len(a)):
	if (i+1)%2==1 and a[i]>0:
		print "Element : ",a[i]
		j = i
		idx = 0
		while j<len(a):
			if a[j] < 0:
				idx = j
				break
			j+=1
		if j < len(a):
			print "To Be swapped With: ",a[j]
			print "Idx odd: ",idx
			z = i
			k = j
			while z<k:
				temp = a[k]
				a[k] = a[z]
				a[z] = temp
				z+=1
				k-=1

			z=i+1
			while z<j:
				temp = a[j]
				a[j] = a[z]
				a[z] = temp
				z+=1
				j-=1

	print a
	if (i+1)%2==0 and a[i] < 0:
		j = i
		idx = 0
		while j<len(a):
			if a[j] > 0:
				idx = j
				break
			j+=1
		print "Idx: ",idx
		if j < len(a):
			z = i
			k = j
			while z<k:
				temp = a[k]
				a[k] = a[z]
				a[z] = temp
				z+=1
				k-=1

			z=i+1
			while z<j:
				temp = a[j]
				a[j] = a[z]
				a[z] = temp
				z+=1
				j-=1
print a
