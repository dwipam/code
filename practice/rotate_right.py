"""
Recursssion to move left
"""

a = [1,2,3,4,5]
times = 2

def reverse(a,low,high):
	while low < high:
		temp = a[low]
		a[low] = a[high]
		a[high] = temp
		low+=1
		high-=1

reverse(a,low=0,high=len(a)-1)
reverse(a,low=0,high=times-1)
reverse(a,low=times,high=len(a)-1)

print a