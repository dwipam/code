"""
Author: Dwipam Katariya (Indiana University)
Title: Multiple Regression with Gradient Descent on House cost prediction
House Cost is predicted with respect to 2 features "sqft_living" and "sqft_living15"
Training data is 80% data of kl_house_data.gl and test data
20% .
3D plot of new model with respect to test data and 2D plot
with respect to (actual price (y-axis),predicted_price and sqft_living)
and (actual price (y-axis),predicted_price and sqft_living15) are 
generated.

Reference:- http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#text 
Data provider:- University of Washington

Output for Model 1 ( With Respect to "sqft_living"):

Avg Error: 1994.2875482 gradient magnitude: 18320016.7406 Weights: [-46999.88716555    281.91211912]
Predicted price on Test Data: [ 356134.44317093  784640.86422788  435069.83652353 ...,  663418.65300782
  604217.10799338  240550.4743332 ]
Derivative with respect to intercept: -4593151092.0
RSS: 2.75400047593e+14

Output for Model 2( With Respect to "sqft_living","sqft_living15"):

Avg Error: 1981.85389823 gradient magnitude: 994238192.216 Weights: [ -9.99999689e+04   2.45092040e+02   6.52584208e+01]
Predicted price on Test Data: [ 366641.63745263  762674.56984176  386323.59305871 ...,  682083.19252456
  585585.55374874  216557.50120715]
Derivative with respect to intercept: -4593151092.0
RSS: 2.70264381584e+14

** Graphs for Model 2 are stored in this same dir.

"""
import graphlab
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
def input_data(data,features_arr,output):
    data['constant_weight']=1 #Appending Intercept
    features_arr=['constant_weight']+features_arr
    feature_sframe = data[features_arr]
    features_sframe_numpy=feature_sframe.to_numpy()
    return(features_sframe_numpy,data[output].to_numpy())

def predict_output(data_matrix,weights):
    predicted_output=np.dot(data_matrix,weights)
    return (predicted_output)
def feature_derivative(predicted_output,actual_output,feature):
    errors = predicted_output-actual_output
    return 2*np.dot(errors,feature)
def regression_gradient_descent(data_matrix,actual_output,step_size,tolerance):
    converged = False
    #weights=np.ones(data_matrix.shape[1])
    weights = np.array([-100000,1.,1.])
    gradient_magnitude = 0
    prev_grad = 0
    while not converged:
        
        pred_out=predict_output(data_matrix,weights)
        error = pred_out-actual_output
        gradient_sum_squares = 0
        prev_grad = gradient_magnitude
        derivate = []
        for i in range(0,len(weights)):
            derivate.append(feature_derivative(pred_out,actual_output,data_matrix[:,i]))
            gradient_sum_squares += gradient_sum_squares+derivate[i]**2
            weights[i]=weights[i]-derivate[i]*step_size
        gradient_magnitude=math.sqrt(gradient_sum_squares)
        print "Avg Error:",math.sqrt(sum((error)**2))/len(error),"gradient magnitude:",gradient_magnitude,"Weights:",weights
        if gradient_magnitude < tolerance or  prev_grad == gradient_magnitude:
            converged = True
    return (weights)
        
    
def main():
    sales = graphlab.SFrame('kc_house_data.gl')
    train_data,test_data = sales.random_split(.8,seed = 0)
    data_matrix,output=input_data(train_data,['sqft_living','sqft_living15'],'price') 
    data_test_matrix,output_test = input_data(test_data,['sqft_living','sqft_living15'],'price')
    step_size = 4e-12 
    tolerance = 1e9
    weights = regression_gradient_descent(data_matrix,output,step_size,tolerance)
    output_predict = predict_output(data_test_matrix,weights)
    print "Predicted price on Test Data:",output_predict
    #print "Actual Price on Test Data:",output_test
    print "Derivative with respect to intercept:",-np.sum(output_test)*2
    print "RSS:", sum((output_predict-output_test)**2)
    fig = plt.figure()
    ax=fig.gca(projection = '3d')
    surf = ax.plot_trisurf(data_test_matrix[:,1],data_test_matrix[:,2],output_predict,cmap=matplotlib.cm.jet,linewidth=0.2)
    plt.show()
    plt.plot(data_test_matrix[:,1],output_test,'rs',data_test_matrix[:,1],output_predict,'g^')
    plt.show()
    plt.plot(data_test_matrix[:,2],output_test,'rs',data_test_matrix[:,2],output_predict,'g^')
    plt.show()
    
if __name__=='__main__':
    main()
