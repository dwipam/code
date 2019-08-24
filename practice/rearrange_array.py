"""
Rearrange at index
"""

def rearrange(a):
	for i in range(len(a)):
		if a[i]!= -1 and a[i] != i:
			temp = a[a[i]]
			a[a[i]] = a[i]
			a[i] = temp
			if a[i] != i:
				for j in range(len(a)):
					if a[j] == i:
						swap = a[j]
						a[j] = a[i]
						a[i] = swap
	print a
rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1])
rearrange([19, 7, 0, 3, 18, 15, 12, 6, 1, 8,11, 10, 9, 5, 13, 16, 2, 14, 17, 4])