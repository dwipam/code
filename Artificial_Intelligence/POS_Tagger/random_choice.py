from random import random
from bisect import bisect 
class weight(object):
	def weightedChoice(self,choices):
		import pdb;pdb.set_trace()
		values, weights = zip(*choices)
    		total = 0
    		cum_weights = []
    		for w in weights:
        		total += w
        		cum_weights.append(total)
    		x = random()*total
    		i = bisect(cum_weights, x)
    		return values[i]		
def main():
	ch=weight()
	print ch.weightedChoice([('a',0.1),('b',0.9)])
if __name__=='__main__':
	main()
