###################################
# CS B551 Fall 2015, Assignment #5
# D. Crandall
#
# There should be no need to modify this file, although you 
# can if you really want. Edit pos_solver.py instead!
#

from pos_scorer import Score
from pos_solver import Solver
import sys

# Read in training or test data file
#
def read_data(fname):
    exemplars = []
    file = open(fname, 'r');
    for line in file:
        data = tuple([w.lower() for w in line.split()])
        exemplars += [ (data[0::2], data[1::2]), ]

    return exemplars


####################
# Main program
#

if len(sys.argv) != 3:
    print "Usage: python label.py training_file test_file"
    sys.exit()

(train_file, test_file) = sys.argv[1:3]

print "Learning model..."
solver = Solver()
train_data = read_data(train_file)
solver.train(train_data)

print "Loading test data..."
test_data = read_data(test_file)

print "Testing classifiers..."
scorer = Score()
Algorithms = ("Naive", "Sampler", "Max marginal", "MAP", "Best")
for (s, gt) in test_data:
    outputs = {"0. Ground truth" : [[gt,], []]}

    # run all algorithms on the sentence
    for i in range(0, len(Algorithms)):
        outputs[ str(i+1) + ". " + Algorithms[i] ] = solver.solve(Algorithms[i], s)

    # compute posteriors for each solution
    posteriors = { algo: [ solver.posterior(s, output) for output in outputs[algo][0] ] for algo in outputs }

    Score.print_results(s, outputs, posteriors)

    scorer.score(outputs)
    scorer.print_scores()

    print "----"
