
"""
Sort in Even Odd
"""
def sort_(a):
	low = 0
	high = len(a)-1
	while low<high:
		while a[low]%2==0 and low < high:
			low+=1
		while a[high]%2==1 and low < high:
			high-=1
		temp = a[low]
		a[low] = a[high]
		a[high] = temp
	print a

sort_([1,2,3,4,5,6])


