from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import math 

x=np.arange(10) #aray of values of feature 'x'
y=np.array([1,3,2,5,7,8,8,9,10,12]) # response 
m=len(x) # number of items in the training dataset
mean = np.mean(y)

plt.plot(y,'ro')


#Helper Functions
def hypothesis_function(slope,intercept,x):
    return intercept + slope*x

def cost_function(slope,intercept,x,result):
    cost=0
    m=len(x)
    for i in range(len(x)):
        error = hypothesis_function(slope,intercept,x[i]) - result[i]
        cost+=math.pow(error,2)
        print x[i],result[i],cost
    avg = cost/(2*m)
    return avg

def summation_of_error(slope,intercept,x,result):
    m=len(x)
    s=0
    for i in range(m):
        err = hypothesis_function(slope,intercept,x[i]) - result[i]
        s+=err
    return s

def gradient_descent(slope,intercept,x,result,alpha=0.1):
    size = len(x)
    sum_of_features = np.sum(x)
    epochs=0
    while(epochs<3):
        sum_of_errors = summation_of_error(slope,intercept,x,result)
        tmp_intercept = intercept - (alpha/size)*sum_of_errors
        tmp_slope = slope - (alpha/size)*sum_of_errors*sum_of_features
        intercept = tmp_intercept
        slope=tmp_slope
        print sum_of_errors
        epochs+=1
    return intercept,slope
print x,y
p1,p2=gradient_descent(1,1,x,y)
print p1,p2
predicitons=[]
for i in range(len(x)):
    v=hypothesis_function(p1,p2,x[i])
    predicitons.append(v)
plt.plot(predicitons)
plt.show()