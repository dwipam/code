def fib(N):
	if N == 0:
	    return 0
	if N == 1:
	    return 1
	prev_sum = 0
	cur_sum = 1
	total_sum = 1
	for i in range(2,N+1):
	    total_sum = cur_sum + prev_sum
	    prev_sum = cur_sum
	    cur_sum = total_sum
	return total_sum
print fib(5)