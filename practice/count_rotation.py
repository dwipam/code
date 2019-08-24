"""
Find the Rotation Count in Rotated Sorted array
Consider an array of distinct numbers sorted in increasing order. 
The array has been rotated (clockwise) k number of times. 
Given such an array, find the value of k.
"""

a = [15, 18, 19, 1, 6, 12]

min_ = a[0]
min_index = 0
for i in range(1,len(a)):
	if a[i] < min_:
		min_ = a[i]
		min_index = i
print min_index


def count_rotation(arr, low, high):
	if low > high :
		return -1
	mid =(low + high)/2
	if a[mid] < a[mid-1]:
		return mid
	elif a[mid-1] < a[mid] and a[mid+1] > a[mid]:
		return count_rotation(arr, low, mid-1)
	else:
		return count_rotation(arr, mid+1, high)
low = 0
high = len(a)
print count_rotation(a, low, high)