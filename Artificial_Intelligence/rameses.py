from collections import Counter
from itertools import chain
import math
import sys
from copy import deepcopy

INFINITY = 10**12
LOST_VALUE = 500

class State(object):
	def __init__(self,arr, maxMove=True, depth=0):
		self.array = arr
		self.depth = depth
		self.maxMove = maxMove

	def __repr__(self):
		return "\n" .join("".join(cell for cell in row) for row in self.array) 
	
	def get_children(self):
		res = []
		for rowNum, row in enumerate(self.array):
			for colNum, cell in enumerate(row):
				if cell == '.':
					temp = deepcopy(self.array)
					temp[rowNum][colNum] = 'x'
					res.append(State(temp, depth=self.depth+1))
		return res

	def stateEvalFunction1(self):
		"""
		We are not using this function. Refer to the other function.

		"""

		dimen = len(self.array[0])
		cost = [[0 for x in range(len(self.array))] for x in range(len(self.array))]
		for rowNum, row in enumerate(self.array):
			for colNum, cell in enumerate(row):
				if cell == 'x':
					continue	
				costRow = sum((-2 if cell == 'x' else 1) for cell in self.array[rowNum])
				costCol = sum((-2 if cell == 'x' else 1) for cell in [row[colNum] for row in self.array])
				costMainDiag = 0
				costOppDiag = 0
				if rowNum == colNum:
					costMainDiag = sum((-2 if cell == 'x' else 1) \
										for cell in 
										[self.array[x][y] for x in range(dimen) for y in range(dimen) if x == y])
				if rowNum + colNum == dimen - 1:
					costOppDiag = sum((-2 if cell == 'x' else 1) \
										for cell in \
										[self.array[x][y] for x in range(dimen) for y in range(dimen) \
										if x + y == dimen-1])
				cost[rowNum][colNum] = costRow + costCol+ costMainDiag + costOppDiag
		return max(chain(*cost))


	def getMoveMultiplier(self):
		return 1 if self.maxMove else -1

	def stateEvalFunction(self):
        """
        This evaluation function is simply:
            (No of rows that can be completed in odd number of moves) +
            (No of columns that can be completed in odd number of moves) +
            1 if main diagonal can be completed in odd number of moves +
            1 if opposite diagonal can be completed in odd number of moves +
            
        If any of the rows/columns/diagonals are complete, return LOST_VALUE
        """
		dimen = len(self.array)
		if any(set(row) == set('x') for row in self.array):
			return self.getMoveMultiplier() * -LOST_VALUE
		if any(set(col) == set('x') for col in zip(*self.array)):
			return self.getMoveMultiplier() * -LOST_VALUE
		if set(self.array[pos][pos] for pos in range(dimen)) == set('x'):
			return self.getMoveMultiplier() * -LOST_VALUE
		if set(self.array[pos][dimen-pos-1] for pos in range(dimen)) == set('x'):
			return self.getMoveMultiplier() * -LOST_VALUE

		rowEmptyElems = [row.count('.') for row in self.array]
		colEmptyElems = [col.count('.') for col in zip(*self.array)]
		diagEmptyCount = [self.array[pos][pos] for pos in range(dimen)].count('.')
		oppDiagEmptyCount = [self.array[pos][dimen-pos-1] for pos in range(dimen)].count('.')
		return self.getMoveMultiplier() * \
				sum(x%2 for x in rowEmptyElems + colEmptyElems + [diagEmptyCount, oppDiagEmptyCount])


def alpha_beta_pruning(node, depth, alpha, beta, maxPlayer):
	"""
	Algorithm used from https://www.wikiwand.com/en/Alpha%E2%80%93beta_pruning
	"""
	if depth == 0 or node.stateEvalFunction() in (LOST_VALUE, -LOST_VALUE):
		return node.stateEvalFunction()
	if maxPlayer:
		v = -INFINITY
		for child in node.get_children():
			v = max(v, alpha_beta_pruning(child, depth-1, alpha, beta, False))
			alpha = max(v, alpha)
			if beta <= alpha:
				break
		return v
	else:
		v = INFINITY
		for child in node.get_children():
			v = min(v, alpha_beta_pruning(child, depth-1, alpha, beta, True))
			beta = min(beta, v)
			if beta <= alpha:
				break
		return v

def get_move(state, max_depth):
	#import pdb; pdb.set_trace()
	max_state = None
	max_value = -INFINITY
	children = state.get_children()
	for child in children:
		value = alpha_beta_pruning(child, max_depth, -INFINITY, INFINITY, False)
		#print "Value for child:"
		#print child
		#print " is: ", value
		if value > max_value:
			max_value = value
			max_state = child
	if max_state is None:
		max_state = children[0]
	return max_state

def main():
	print "This program will search in an iterative deepening way. It will conduct its searches in an" + \
			" increasing order of depth. It will terminate when it has fully searched all dimension*dimension" + \
			" or when the evaluation script kills it. Kill this program any time, the last line of output" + \
			" is the best solution so far."
	
	dimen = int(sys.argv[1])
	array = sys.argv[2]
	time = sys.argv[3] #ignored!

	iterator = iter(array)
	arr = [[next(iterator) for x in range(dimen)] for x in range(dimen)]
	s = State(arr)
	for depth in range(dimen*dimen):
		move = get_move(s, depth)
		print "".join("".join(x for x in row) for row in move.array)
	#print "Move to make:"
	#print move

if __name__ == '__main__':
	main()


