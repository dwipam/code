a = [1,2,0,3,4,0,5,6,0]


def two_pass():
	count = 0
	for i in range(len(a)-1):
		if a[i]!=0:
			a[count] = a[i]
			count+=1
	while count <len(a):
		a[count] = 0
		count+=1

	print a


a = [1,2,0,3,4,0,5,6,0]

"""
1,2,0,3,4,0,5,6,0
1,2,3,0,4,0,5,6,0
1,2,3,4,0,0,5,6,0
1,2,3,4,
"""
def one_pass():
	for i in range(len(a)):
		if a[i]==0:
			j = i
			while j<len(a):
				if a[j] > 0:
					break
				j+=1
			a[i] = a[j-1]
			a[j-1] = 0
	print a
two_pass()
one_pass()