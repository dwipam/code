"""
Author: Dwipam Katariya
Ridge Regression

"""



import graphlab
import matplotlib.pyplot as plt
import numpy as np




learning_rate = 1e-12
l2_penalty =  1e11
def transform_data(sales,actual_price):
	
	feature_vect = np.matrix(sales.to_numpy())
	feature_vect = np.insert(feature_vect,0,values = 1,axis = 1) #Axis = 1 for Y Axis and Axis = 0 for X Axis
	return (np.array(feature_vect),actual_price.to_numpy())
def feature_derivative(error, feature, weight, l2_penalty, constant_feature):
	if(constant_feature == True):
		return 2*(np.dot(error,feature))
	else:
		return (2*(np.dot(error,feature))+2*l2_penalty*weight)
def predict(weights,feature):
	return (np.dot(feature,weights))
def ridge_regression(sales,l2_penalty,actual_output,max_iter):
	weights = np.array([0.0,0.0,0.0])
	while (max_iter>0):
		predict_output = predict(weights,sales)
		error =  predict_output-actual_output
		gradient = []
		for i in range(0,len(weights)):
			gradient.append(feature_derivative(error,sales[:,i],weights[i],l2_penalty,True if i==0 else False))
			weights[i] = weights[i]-gradient[i]*learning_rate	
		max_iter-=1
		print weights
	return weights
def main():
	sales = graphlab.SFrame('kc_house_data.gl')
	sales,actual_output = transform_data(sales['sqft_living','sqft_living15'],sales['price'])
	weights = ridge_regression(sales,0.0,actual_output,1000)
	weights_l2 = ridge_regression(sales,l2_penalty,actual_output,1000)
	plt.plot(sales,actual_output,'k.',sales,predict(weights,sales),'b-',sales,predict(weights_l2,sales),'r-')
	plt.show()

if __name__=='__main__':
	main()
