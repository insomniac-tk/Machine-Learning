from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import math 
p0=p1=0 # p0=>theta0 and p1=>theta1
y_axis=np.arange(15)
x=np.arange(10) #aray of values of feature 'x'
y=np.array([1,3,2,5,7,8,8,9,10,12]) # response 
m=len(x) # number of items in the training dataset


#The Cost Function

def J(p1,p2,X,Y): #paramters : (y intercept,slope,feature vector,response vector)
    summation=0
    for i in range(len(X)):
        err = (p1 + p2*X[i]) - Y[i] #(th0 + th1*xi) - yi 
        sq_err = math.pow(err,2)
        summation +=sq_err
    return (1/(2*len(X)))*summation



plt.style.use(['bmh'])
plt.plot(y,'bo')
plt.xticks(x)
plt.yticks(y_axis)
plt.ylabel('Responses')
plt.xlabel('Value of Single Feature')
plt.show()
