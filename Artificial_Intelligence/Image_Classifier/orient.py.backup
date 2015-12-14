import sys
import random
import math
import json
import numpy
import matplotlib.pyplot as pyplot
import time
from heapq import nlargest
from itertools import izip, imap

sigmoid = lambda u: 1.0 / (1 + math.exp(-u))
sigmoid_ = lambda u: sigmoid(u) * (1 - sigmoid(u))
tanh = lambda u: math.tanh(u)
tanh_ = lambda u: 1-tanh(u)**2
new = lambda u: 1.7159*math.tanh(2.0 * u / 3.0) 
new_ = lambda u: 1.14393 * tanh_(2.0 * u / 3.0)
average_error_iter = []

def dot(x,y):
    if len(x) != len(y):
        raise "Unmatched dimensions."
    return sum(map(lambda (a,b): a*b, zip(x,y)))


class TestData(object):
    def __init__(self, id_str, orientation, data):
        self.id_str = id_str
        self.orientation = orientation
        self.data = data

    def __repr__(self):
        return "<%s> => %d\n%s"%(self.id_str, self.orientation, " ".join(map(str, self.data)))

def knn(train_data, test_data, k):
    k = int(k)
    euclidean_dist = lambda t1, t2: sum(map(lambda (x,y): (x-y)**2, zip(t1.data, t2.data)))
    for data in test_data:
        largest = nlargest(k, map(lambda x: (-euclidean_dist(x, data),x), train_data))
        orientations = map(lambda x: x[1].orientation, largest)
        yield data, max(set(orientations), key=orientations.count)

def load_data_file(fileName):
    return [TestData(line[0], int(line[1]), map(int,line[2:])) for line in map(lambda x: x.strip().split(), open(fileName))]


def train_neural_network(train_data, hiddenCount, fn, fn_, alpha):
    featureLength = len(train_data[0].data)
    classLength = 4
    weights = [None, 
        [[random.random()*2-1 for __ in range(featureLength+1)] for _ in range(hiddenCount)], 
        [[random.random()*2-1 for __ in range(hiddenCount)] for _ in range(classLength)]
    ]
    errors = [
        [0] * featureLength,
        [0] * hiddenCount,
        [0] * classLength,
    ]
    o = lambda x: [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]][x/90]
    normalize = lambda x:x/255.0
    total_avg_error = 0
    for iteration in range(5):
        print "iteration",iteration+1
        sum_errors=[]
        for input_set, output_set in imap(lambda x: (map(normalize,x.data), o(x.orientation)), train_data):
            a = [input_set+[0.3], [0]*hiddenCount, [0]*classLength]
            inp = [None, [0]*hiddenCount, [0]*classLength]

            for l in [1, 2]:
                for index, neuron_weights in enumerate(weights[l]):
                    inp[l][index] = numpy.dot(neuron_weights, a[l-1])
                    a[l][index] = fn(inp[l][index])

            #Propagate deltas backward.
            for j in range(classLength):
                errors[2][j] = fn_(inp[-1][j]) *(output_set[j] - a[-1][j]) 
            for index_layer_l  in range(len(errors[1])):
                temp = 0.0
                for index1, neuron_weights1 in enumerate(weights[2]):
                    temp += weights[2][index1][index_layer_l] * errors[2][index1]
                errors[1][index_layer_l] = fn_(inp[1][index_layer_l]) * temp

            for l in [1, 2]:
                for neuron_index, neuron_weights in enumerate(weights[l]):
                    for i,x in enumerate(neuron_weights):
                        weights[l][neuron_index][i] += alpha *errors[l][neuron_index]*a[l-1][i] 
            sum_errors.append(sum((x-y)**2 for x,y in zip(output_set,a[-1])))

        total_avg_error = sum(sum_errors)/float(len(sum_errors))
        average_error_iter.append(total_avg_error)
        print "Average error:", total_avg_error
    return weights, total_avg_error

def solve_neural_network(test_data, weights, fn):
    normalize = lambda x:x/255.0
    for test in test_data:
        input_arr = numpy.array(map(normalize,test.data+[0.3]))
        weights_1 = numpy.array(weights[1])
        mul1 =  map(fn,(numpy.dot(weights_1,input_arr.transpose())))
        mul2 = map(fn,(numpy.dot(numpy.array(weights[2]),mul1)))
        yield test, [0,90,180,270][max(enumerate(mul2), key=lambda x: x[1])[0]]

def solve_train_neural_network(train_data, test_data, hiddenCount, fn=sigmoid, fn_=sigmoid_, alpha=0.4):
    weights, total_avg_error = train_neural_network(train_data, int(hiddenCount), fn=fn, fn_=fn_, alpha=alpha)
    for result in solve_neural_network(test_data, weights, fn):
        yield result

    obj = {
        "alpha": alpha,
        "fn": {sigmoid: "sigmoid", tanh: "tanh", new: "new"}[fn],
        "fn_": {sigmoid_: "sigmoid_", tanh_: "tanh_", new_: "new_"}[fn_],
        "hiddenCount": hiddenCount,
        "weights": weights,
        "avg_error": total_avg_error,
    }
    fileName = "model-%0.5f"%total_avg_error
    with open(fileName, "w") as f:
        json.dump(obj, f)
    print "Model saved to", fileName

def solve_best(train_data, test_data, param):
    with open(param) as f:
        obj = json.load(f)
    fn = {"sigmoid": sigmoid, "tanh":tanh, "new":new}[obj["fn"]]
    for result in solve_neural_network(test_data, obj["weights"], fn):
        yield result

def main():
    _, train_file, test_file, algorithm, param = sys.argv
    start = time.time()
    train_data = load_data_file(train_file)
    test_data = load_data_file(test_file)

    confusion_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    algo_func = {"knn": knn, "nnet": solve_train_neural_network, "best": solve_best}[algorithm]
    for inp, predicted_orientation in algo_func(train_data, test_data, param):
        correct_orientation = inp.orientation
        print "Correct:", correct_orientation
        print "Predicted:", predicted_orientation
        confusion_matrix[correct_orientation/90][predicted_orientation/90] += 1
        print "\n".join("%3d %3d %3d %3d"%tuple(row) for row in confusion_matrix)
        print
    print "Confusion Matrix:"
    print "\n".join("%3d %3d %3d %3d"%tuple(row) for row in confusion_matrix)
    print "Overall Accuracy:", 100 * float(sum(confusion_matrix[i][i] for i in range(4)))/ \
                    sum(sum(cell for cell in row) for row in confusion_matrix), "%"
    end = time.time()
    print "Overall Time:",end-start
    pyplot.plot(range(len(average_error_iter)),average_error_iter)
    axes = pyplot.gca()
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    pyplot.show()
if __name__ == '__main__':
    random.seed()
    main()

