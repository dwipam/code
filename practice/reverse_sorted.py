"""
Find the Rotation Count in Rotated Sorted array
Consider an array of distinct numbers sorted in increasing order. 
The array has been rotated (clockwise) k number of times. 
Given such an array, find the value of k.
"""
a = [3,4,5,1,2]
search_a = 3

prev = a[0]
for idx in range(1,len(a)):
	if a[idx] < prev:
		pivot = idx
	prev = a[idx]

print pivot


if search_a  <= a[-1] and search_a >= a[pivot]:
	low = pivot
	high = len(a) - 1
else:
	high  = pivot
	low = 0

def binary_search(arr, low, high):
	if low>high:
		return -1
	mid = (low + high)/2
	if arr[mid] == search_a:
		return mid
	if search_a > arr[mid]:
		return binary_search(arr, mid+1, high)
	else:
		return binary_search(arr, low, mid-1)
print low, high
print binary_search(a, low, high)