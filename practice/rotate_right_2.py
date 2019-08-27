"""
1,2,3,4
1,1,
"""


a = [1,2,3,4]

last_el = a[len(a)-1]
temp = a[0]
for i in range(1,len(a)):
	temp_1 = a[i]
	a[i] = temp
	temp = temp_1
a[0] = last_el
print a

