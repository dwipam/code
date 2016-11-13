#Name: Dwipam Katariya
#IU ID: ddkatari

import sys
from collections import defaultdict
from collections import Counter
import math
import numpy as np
import pandas as pd
import os
from itertools import repeat

class node(object):
	#An object to store information for current split
	def __init__(self, attribute_name, attribute_value, split_data, depth, class_label, entropy, iG, child_node):
		self.attribute_name = attribute_name
		self.attribute_value = attribute_value
		self.split_data = split_data
		self.depth = depth
		self.class_label = class_label
		self.entropy = entropy
		self.iG = iG
		self.child_node = child_node
class entropy_obj(object):
    #An object to store entropy information for current split
	def __init__(self, idx, attribute_index, entropy):
		self.idx = idx
		self.attribute_index = attribute_index
		self.entropy = entropy
class decision_tree(object):
	def __init__(self,data,max_depth):
		self.target = Counter(data['Target_variable'])
		cr = len(data['Target_variable'])
		self.old_entropy = dict(map(lambda (k,v):(k,-((int(v)*1.0)/cr)*(math.log((int(v)*1.0)/cr,2))),\
				(self.target.iteritems())))
		self.old_entropy = sum(self.old_entropy.values())
		self.iG = 1.0
		self.root = 0
		self.max_depth = max_depth
        def classify(self, data, depth, node_obj,weight,index):
	#Constructs tree on the train data	
                data['weight'] = weight
                parent_queue = []
		if self.max_depth == 0:
			parent_queue.append((node(None, None, data, 0,self.return_class_label(data),self.old_entropy, self.iG, None)))
		entropies ={}
		attribute_indexes = [k for k,v in data.iteritems() if k not in ['Target_variable','weight']]
		if node_obj != None: attribute_indexes = [k for k in attribute_indexes if k != node_obj.attribute_name]
		for attribute_index in attribute_indexes:
			entr,idx = self.entropy(attribute_index, data)
			entropies[attribute_index]=entropy_obj(idx,attribute_index,entr)
                best_attr_split = min(entropies.values(),key=lambda x: x.entropy)
		if node_obj != None: igt = node_obj.entropy - best_attr_split.entropy
		if node_obj == None: igt = self.old_entropy - best_attr_split.entropy
		ole = best_attr_split.entropy
		if node_obj != None:
                        #Check if all the samples classified for node. If Entropy is 0 for all the nodes it won't split ahead
			if all(v==0.0 for v in  map(lambda x:x.entropy,entropies.values())):
				return parent_queue
		if depth-1 >= 0.0:
			if node_obj == None: print "\n\t Root Node: ", best_attr_split.attribute_index,"is at depth",\
					self.max_depth-depth+1,"\n"
			else :
				print "-"*85
				print " | ","Depth", self.max_depth-depth+1, " | ","Parent node",node_obj.attribute_name, \
						" | ","Split attribute ",best_attr_split.attribute_index, "  | ","for attribute value",\
						node_obj.attribute_value," | "
			split_datas = self.return_data(data, best_attr_split.idx)	
			root = None
			if node_obj != None: depth = node_obj.depth
			for k,_ in split_datas.iteritems():
					class_label = self.return_class_label(_)
					node_obj = node(best_attr_split.attribute_index, k, dict(_), depth-1, class_label, ole, igt, None)
					nodeObj = node(best_attr_split.attribute_index, k, dict(_), node_obj.depth, class_label, \
						ole,igt, self.classify(dict(_), \
						node_obj.depth if node_obj != None else depth-1, node_obj,weight,index)) 
					parent_queue.append(nodeObj)
		return parent_queue	
	def return_data(self, split_data, idx):
		#Given the index numbers, returns the data with the index numbers
		split_data = dict([(k,np.array(v)) for k,v in split_data.iteritems()])
		idx_t = idx
		new_split_data = {}
		for i in idx.keys():
			new_split_data[i] = map(lambda (k,v):(k,v[idx_t[i]]), split_data.iteritems())
		return new_split_data
	def return_class_label(self, data):
		#Returns the class label for the given data
		return Counter(dict(data)['Target_variable']).most_common()[0][0]
	def split(self, attribute_index,split_data):
		#Splits the data for the best attribute
		merge_dict = defaultdict(list)
		idx_dict = defaultdict(list)
		combine = zip(split_data[attribute_index], split_data['Target_variable'], split_data['weight'])
		idx  = zip(split_data[attribute_index], range(len(split_data[attribute_index])))
		for value, label, weight in combine:
			merge_dict[value].append((label,weight))
		for value, idx in idx:
			idx_dict[value].append(idx)

		merge_dict = {value: label for value,label in merge_dict.items() if label}
		idx_dict = {value: idx for value,idx in idx_dict.items() if idx}
		return(merge_dict,idx_dict)
	def entropy(self, attribute_index,split_data):
		#Given a data wfor an attribute, calculates the entropy
                merge_dict,idx_dict = self.split(attribute_index, split_data)
                entropy = 0
		N_i = sum(split_data['weight'])*1.0
		for key in merge_dict.keys():
                        curWeight = defaultdict(int)
			n_i =  sum(zip(*merge_dict[key])[1])
                        for k,v in merge_dict[key]: curWeight[k]+=v
			#Calculate entropy Entropy(Y|X)
			keyt = dict(map(lambda (k,v):(k,-((v*1.0)/n_i)*(math.log((v*1.0)/n_i,2))),(curWeight.iteritems())))
			entropy += (n_i/N_i)*sum(keyt.values())
			
		return (entropy,idx_dict)
	def predict(self, testdata, train_obj):
		#Predicts Label for each row in the Test Data
		testpredict = []
		if self.max_depth == 0:
			return list(len(testdata.values()[0])*train_obj[0].class_label)
               #This loop that I made, is very slow to convert columnar dictionary to an row format list
		#for i in range(len(testdata.values()[0])):
		#	testpredict.append([np.array(v)[i] for k,v in testdata.iteritems()])
                get_label = []	
               #Hence I used pandas. If you want to test above loop uncomment it and comment below line 
                testpredict = pd.DataFrame(testdata).values.tolist()
                for row in testpredict:
			get_label.append(self.retrieveLabelPredict(row, train_obj))
		return get_label 
	def retrieveLabelPredict(self, row, train_obj):
		#Given a row fro the test data, returns label for the respective row
		childs = []
		attr_val = []
		for i in range(0,len(train_obj)):
			if train_obj[i].attribute_value == row[train_obj[i].attribute_name-1]:
				if train_obj[i].child_node :
					hold =  self.retrieveLabelPredict(row, train_obj[i].child_node)
					if hold == None: return(train_obj[i].class_label)
					else: return(hold)
				else: return(train_obj[i].class_label)

class boosted_trees(object):
    #Class object to store hyppothesis for bagging and boosting
    def __init__(self,alpha,hypothesis):
        self.alpha = alpha
        self.hypothesis = hypothesis

class ensemble(object):
                
                
                def learn_bagged(self, tdepth, numbags, datapath):
                    data = datapath
                    samples = []
                    tree = decision_tree(data,tdepth)
                    data['Target_variable'] = [int(x) for x in data['Target_variable']]
                   #Intialize constant weights, so that we don't need to change our entropy function. 
                    weight = [x*1.0/len(data['Target_variable']) for x in repeat(1,len(data['Target_variable']))]
                    #Sample with replacement using numpy function
                    for i in range(numbags):
                        sample = self.sample(np.random.choice(range(len(data['Target_variable'])),len(data['Target_variable']),\
                                replace=True),data)
                        #Store all the hypothesis so that they can be used for majority voting
                        samples.append(boosted_trees(1,tree.classify(sample,tdepth,None,weight,0)))
                    return samples

                def sample(self,index,data):
                    return dict([(k,np.array(v)[index].tolist()) for k,v in data.iteritems()])
                
                def learn_boosted(self,tdepth, numtrees, datapath):
                    #Returns boosted trees with tdepth and numtrees. 
                    #Gets datapath as the data after data manipulation from main function.
                    data = datapath
                    data['Target_variable'] = [int(x) for x in data['Target_variable']]
                    weight = [x*1.0/len(data['Target_variable']) for x in repeat(1,len(data['Target_variable']))]
                    index = range(len(data['Target_variable']))
                    models = []
                    tree = decision_tree(data,tdepth)
                    for i in range(0,numtrees):
                        #Get h(theta(m)) 
                        hypothesis = tree.classify(data,tdepth,None,weight,index)
                        predicted = tree.predict(data,hypothesis)
                        print("\n ----------------On Train-----------------")
                        confusion_matrix(data['Target_variable'],predicted)
                        #error function 1: from washington website  
                        #error =0.5 - (np.dot(weight,map(lambda x:x[0]*x[1],zip(data['Target_variable'],predicted))))*0.5
                        #error function 2: from lecture slide
                        #error = sum(map(lambda x:x[2],[x for x in zip(data['Target_variable'],predicted,weight) if x[0]!=x[1]]))
                        #error function 3: https://web.stanford.edu/~hastie/Papers/samme.pdf
                        error = (sum(map(lambda x:x[2],[x for x in zip(data['Target_variable'],predicted,weight) if x[0]!=x[1]])))/sum(weight)
                        #calculate alpha
                        alpha = 0.5*math.log((1-error)/(error),2)
                        total_weight = sum(weight)
                        #Calculate new weights
                        weight = map(lambda x:self.update_weight(x,alpha,total_weight),zip(predicted, data['Target_variable'],weight))
                        models.append(boosted_trees(alpha, hypothesis))
                        print "Error: ",error
                        print "Alpha: ",alpha,"\n"
                    return models
                
                def predict(self, models, testdata, tdepth,dec):
                    #Predict from bagged treest or boosted trees
                    tree = decision_tree(testdata,tdepth)
                    res = []
                    for model in models:
                        #As we have initialzed alpha as constant for bagging this should only matter in case of boosting
                        res.append([model.alpha*x for x in tree.predict(testdata, model.hypothesis)])
                    if dec=='boost':
                        #Only sum up alpha if boosting, and return label -1 if x(i) < 0 else return 1
                        res = map(lambda x:sum(x),zip(*res))
                        res = map(lambda x: -1 if x<0 else 1,res)
                    else:
                        #Return label with majority vote
                        res = map(lambda x:max(x,key=x.get),map(lambda x:Counter(x),zip(*res)))
                    return res

                def update_weight(self, x, alpha, total_weight):
                    predicted_i, actual_i, weight_i = x
                    return ((weight_i/total_weight)*math.exp(actual_i*alpha*predicted_i*-1.0))

class read_data(object):
	#Return dictionary with key as variable index and value as the column 
	def read(self,f,target_variable_index):
		dict = {}
		extract_data = []
		for line in f:
			extract_data.append(line.strip().split(','))
                extract_data = extract_data[1:]
                i = 0
                for _ in range(0,len(extract_data[1])):
                        if _ == 21:continue
                        idx = _
			y = "Target_variable" if _ == target_variable_index else i
                        dict[y] = [x[idx] for x in extract_data]	
                        i += 1
                dict['Target_variable'] = map(lambda x: 1 if x == '1' else -1,dict['Target_variable'])
                return dict	

def confusion_matrix(actual,predicted):
	#Creates confusion matrix
        actual = map(lambda x: 0 if x == -1 else 1,actual)
        predicted = map(lambda x: 0 if x == -1 else 1,predicted)
	unique = list(set(actual))
	tp = 0; fp=0; fn=0; tn=0;
	for i in range(len(actual)):
		tp = tp+1 if actual[i] == predicted[i] and actual[i] == unique[1] else tp
		fp = fp+1 if actual[i] != predicted[i] and actual[i] == unique[0] else fp
		tn = tn+1 if actual[i] == predicted[i] and actual[i] == unique[0] else tn
		fn = fn+1 if actual[i] != predicted[i] and actual[i] == unique[1] else fn
	print "Predicted\t", unique[0],"\t", unique[1]
	print "Actual"
	print unique[0],"\t\t",tn,"\t",fp
	print unique[1],"\t\t",fn,"\t",tp
	print "\nAccuracy: ", round((tp+tn*1.0)/(tp+fp+tn+fn),2)
	return (tp+tn*1.0)/(tp+fp+tn+fn)

def main():
        #Read data
	read = read_data()
        path = os.listdir(sys.argv[4])
        path = [x for x in path if '.csv' in x]
        trainpath = sys.argv[4]+'/'+[x for x in path if 'train' in x][0]
        testpath = sys.argv[4]+'/'+[x for x in path if 'test' in x][0]
	with open(trainpath,'r') as f:
		traindata = read.read(f,20)
	with open(testpath,'r') as f:
		testdata = read.read(f,20)
        ensembleObj = ensemble()	
	f.close()
        if sys.argv[1] == 'boost':
            models = ensembleObj.learn_boosted(int(sys.argv[2]),int(sys.argv[3]),traindata)
        else:
            models = ensembleObj.learn_bagged(int(sys.argv[2]), int(sys.argv[3]),traindata)   
        res = ensembleObj.predict(models, testdata, int(sys.argv[2]),sys.argv[1])
        print("\n ----------------On Test-----------------")
        confusion_matrix(testdata['Target_variable'],res)
if __name__=='__main__':main()
