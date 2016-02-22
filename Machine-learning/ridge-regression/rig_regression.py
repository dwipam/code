"""
Author: Dwipam Katariya
Program: Ridge Regression with estimating best lambda for 10-fold cross validation


"""

import graphlab
import numpy as np
import matplotlib.pyplot as plt
import copy

def polynomial_sframe(sf, feature, degree):
    sf_feature_power = graphlab.SFrame()
    sf_feature_power[feature] = sf[feature]
    if degree>1:
        for i in range(2,degree+1):
            sf_feature_power[feature+'_power_'+str(i)]=graphlab.SArray(sf[feature]).apply(lambda x:x**i)
    return sf_feature_power

class frame_object(object):
    def __init__(self, l2_penal, RSStemp):
        self.l2_penal = l2_penal
        self.RSStemp = RSStemp

def k_fold(frame,kfold_degree,price):
    col_names = frame.column_names()
    solution_frame = []
    frame['price']=price
    for l2_penal in np.logspace(1,7,num=13):
        RSStemp = 0
        for i in range(0,kfold_degree):
            start = (len(price)*i)/kfold_degree
            end = (len(price)*(i+1))/kfold_degree-1
            validation_data = frame[start:end]
            train_data = frame[0:start].append(frame[end+1:len(frame['price'])-1])
            
            model1 = graphlab.linear_regression.create(train_data,target='price',features = col_names,validation_set=None,verbose=None,
                l2_penalty = l2_penal)
            RSStemp+=sum((model1.predict(validation_data)-validation_data['price'])**2)
        
        solution_frame.append(frame_object(l2_penal,(RSStemp/len(price))))
    return min(solution_frame,key=lambda x: x.RSStemp)
        
                   
def main():
    k_fold_degree = 10
    sales = graphlab.SFrame('kc_house_data.gl')
    train_data,test_data = sales.random_split(0.9,seed=1)
    #split1,split2 = sales.random_split(.5,seed=0)   To Manually Split for 4 sets
    #set1,set2 = split1.random_split(.5,seed=0)
    #set3,set4 = split2.random_split(.5,seed=0)
    #sales = set4
    #train_data = train_data.sort(['sqft_living','price'])
    train_data = graphlab.toolkits.cross_validation.shuffle(train_data, random_seed=1)
    poly_deg_frame = polynomial_sframe(train_data,'sqft_living',15)
    col_names = poly_deg_frame.column_names() 
    obj= k_fold(poly_deg_frame,k_fold_degree,train_data['price'])
    #poly_deg_frame['price']=sales['price']
    model1 = graphlab.linear_regression.create(poly_deg_frame,target='price',features = col_names,validation_set=None,verbose=None,
           l2_penalty = obj.l2_penal)
    plt.plot(test_data['sqft_living'],test_data['price'],'.',test_data['sqft_living'],model1.predict(test_data))
    plt.show()



if __name__=='__main__':
    main()
