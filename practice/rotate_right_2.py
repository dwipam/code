"""
1,2,3,4
1,1,
"""


a = [1,2,3,4]

last_el = a[len(a)-1]
for i in range(len(a)-1,0,-1):
	a[i] = a[i-1]
a[0] = last_el
print a

