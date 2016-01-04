"""
Author: Dwipam Katariya
This is a simple linear regression program where, 
slopes and intercepts are calculated on the train_data and then predicted on the
test data. 
I use graphlab for SFrame and SArray and numpy for fast data processing.
Train_data is the 80% data of the original data, where as 20% is the test data. 
Data that is used, is provided by University of Washington(Statistics Department)
"""
import graphlab
import numpy as np
import matplotlib.pyplot as plt
def simple_regression(kings_sales):
    test_data,train_data = split_data(kings_sales)
    w0,w1=calc_plots(train_data)
    print "Intercept Y:",w0,"Slope M:",w1
    output_feature = get_regression_predictions(test_data['sqft_living'], w0, w1)
    plt.plot(test_data['sqft_living'],test_data['price'],'.',test_data['sqft_living'],output_feature,'-')
    (output_feature-test_data['price'])**2
    rss = (output_feature-test_data['price'])**2
    print "Predicted Price:",output_feature
    rss = sum(rss) 
    print "Resedual Sum:",rss
    plt.show()
def calc_plots(train_data):
    y=np.asarray(train_data['price'])
    xi=train_data['sqft_living']
    xi=np.asarray(xi)
    on=np.ones(int(len(xi)))
    A=np.array([xi,on])
    w=np.linalg.lstsq(A.T,y)[0]
    return (w[1],w[0])
def get_regression_predictions(input_feature, intercept, slope):
    input_feature = graphlab.SArray(input_feature)
    output_feature = intercept+slope*(input_feature)   
    return output_feature 
def split_data(kings_sales):
    test_data,train_data = kings_sales.random_split(.8,seed=0)
    return (train_data,test_data)

def main():
    kings_sales = graphlab.SFrame('/home/dwipam/ML-Assignment/Assigment-1/kc_house_data.gl/')
    simple_regression(kings_sales)
    

if __name__== '__main__':
    main()
    
