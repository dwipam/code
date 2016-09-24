#Name: Dwipam Katariya
#IU ID: ddkatari

import sys
from collections import defaultdict
from collections import Counter
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
	def __init__(self, idx, attribute_index, entropy):
		self.idx = idx
		self.attribute_index = attribute_index
		self.entropy = entropy
class decision_tree(object):
	def __init__(self,data,max_depth):
		self.target = Counter(data['Target_variable'])
		global cr
		cr = len(data['Target_variable'])
		self.old_entropy = dict(map(lambda (k,v):(k,-((int(v)*1.0)/cr)*(math.log((int(v)*1.0)/cr,2))),\
				(self.target.iteritems())))
		self.old_entropy = sum(self.old_entropy.values())
		self.iG = 1.0
		self.root = 0
		self.max_depth = max_depth
	def classify(self, data, depth, node_obj):
	#Constructs tree on the train data	
		parent_queue = []
		if self.max_depth == 0:
			parent_queue.append((node(None, None, data, 0,self.return_class_label(data),self.old_entropy, self.iG, None)))
		entropies ={}
		attribute_indexes = [k for k,v in data.iteritems() if k != 'Target_variable']
		if node_obj != None: attribute_indexes = [k for k in attribute_indexes if k != node_obj.attribute_name]
		for attribute_index in attribute_indexes:
			entr,idx = self.entropy(attribute_index, data)
			entropies[attribute_index]=entropy_obj(idx,attribute_index,entr)
		best_attr_split = min(entropies.values(),key=lambda x: x.entropy)
		if node_obj != None: igt = node_obj.entropy - best_attr_split.entropy
		if node_obj == None: igt = self.old_entropy - best_attr_split.entropy
		ole = best_attr_split.entropy
		#import pdb;pdb.set_trace()
		if node_obj != None:
			if all(v==0.0 for v in  map(lambda x:x.entropy,entropies.values())):   #Check if all the samples classified for node. If Entropy is 0 for all the nodes it won't split ahead
				return parent_queue
		if depth-1 >= 0.0:
			if node_obj == None: print "\n\t Root Node: ", best_attr_split.attribute_index,"is at depth",\
					self.max_depth-depth+1,"\n"
			else :
				print "-"*80
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
						node_obj.depth if node_obj != None else depth-1, node_obj)) 
					parent_queue.append(nodeObj)
		return parent_queue	
	def return_data(self, split_data, idx):
		#Given the index numbers, returns the data with the index numbers
		split_data = dict([(k,np.array(v)) for k,v in split_data.iteritems()])
		global idx_t
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
		combine = zip(split_data[attribute_index], split_data['Target_variable'])
		idx  = zip(split_data[attribute_index], range(len(split_data[attribute_index])))
		for value, label in combine:
			merge_dict[value].append(label)
		for value, idx in idx:
			idx_dict[value].append(idx)
		merge_dict = {value: label for value,label in merge_dict.items() if label}
		idx_dict = {value: idx for value,idx in idx_dict.items() if idx}
		return(merge_dict,idx_dict)
	def entropy(self, attribute_index,split_data):
		#Given a data wfor an attribute, calculates the entropy
		merge_dict,idx_dict = self.split(attribute_index, split_data)
		entropy = 0
		N_i = len(split_data[attribute_index])*1.0
		for key in merge_dict.keys():
			global n_i
			n_i = len(merge_dict[key])
			keyt = Counter(merge_dict[key])
			#Calculate entropy Entropy(Y|X)
			keyt = dict(map(lambda (k,v):(k,-((v*1.0)/n_i)*(math.log((v*1.0)/n_i,2))),(keyt.iteritems())))
			entropy += (n_i/N_i)*sum(keyt.values())
			
		return (entropy,idx_dict)
	def predict(self, testdata, train_obj):
		#Predicts Label for each row in the Test Data
		testpredict = []
		if self.max_depth == 0:
			return list(len(testdata.values()[0])*train_obj[0].class_label)
		for i in range(len(testdata.values()[0])):
			testpredict.append([np.array(v)[i] for k,v in testdata.iteritems()])
		get_label = []	
		for row in testpredict:
			get_label.append(self.retrieveLabelPredict(row, train_obj))
		return get_label 
	def retrieveLabelPredict(self, row, train_obj):
		#Given a row fro the test data, returns label for the respective row
		childs = []
		attr_val = []
		for i in range(0,len(train_obj)):
			#import pdb;pdb.set_trace()
			if train_obj[i].attribute_value == row[train_obj[i].attribute_name-1]:
				if train_obj[i].child_node :
					hold =  self.retrieveLabelPredict(row, train_obj[i].child_node)
					if hold == None: return(train_obj[i].class_label)
					else: return(hold)
				else: return(train_obj[i].class_label)
class read_data(object):
	#Return dictionary with key as variable index and value as the column 
	def read(self,f,target_variable_index):
		dict = {}
		extract_data = []
		for line in f:
			extract_data.append(line.split())
				
		for _ in range(0,len(extract_data[1])):
			idx = _
			
			#import pdb;pdb.set_trace()
			_ = "Target_variable" if _ == target_variable_index else _
			dict[_] = [x[idx] for x in extract_data]	
		return dict	
def confusion_matrix(actual,predicted):
	#Creates confusion matrix
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
	print "\n Accuracy: ", (tp+tn*1.0)/(tp+fp+tn+fn)
	return (tp+tn*1.0)/(tp+fp+tn+fn)
def main():
	#import pdb;pdb.set_trace()
	read = read_data()
	with open(sys.argv[1],'r') as f:
		traindata = read.read(f,int(sys.argv[2]))
	traindata.pop(int(sys.argv[6]))
	with open(sys.argv[3],'r') as f:
		testdata = read.read(f,int(sys.argv[4]))
	idx_list = testdata.pop(int(sys.argv[6]))
	tr = []
	ts = []
	for i in range(int(sys.argv[5]),int(sys.argv[5])+1): #To run for multiple depths try changing the value here in range function
		tree = decision_tree(traindata,i)
		classify = tree.classify(traindata,i,None)
		predictLabels = tree.predict(traindata, classify)
		print("\n ----------------On Train-----------------")
		tr.append(confusion_matrix(traindata['Target_variable'],predictLabels))
		predictLabels = tree.predict(testdata, classify)
		print("\n ----------------On Test------------------")
		ts.append(confusion_matrix(testdata['Target_variable'],predictLabels))
	tr_plt, = plt.plot(tr, label = "Train", linestyle="--")
	ts_plt, = plt.plot(ts, label = "Test", linestyle="-")
	leg = plt.legend(handles = [tr_plt],loc=1)
	ax = plt.gca().add_artist(leg)
	plt.legend(handles = [ts_plt],loc=4)
	plt.xticks(np.arange(0,int(sys.argv[5]),1.0))
	#plt.show() #If you are running for multiple depths, uncomment this line to show the plot
if __name__=='__main__':main()
