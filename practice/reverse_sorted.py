a = [3,4,5,1,2]
search_a = 3

prev = a[0]
for idx in range(1,len(a)):
	if a[idx] < prev:
		pivot = idx
	prev = a[idx]



if search_a <= a[pivot]:
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