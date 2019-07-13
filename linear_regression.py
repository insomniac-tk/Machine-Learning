from __future__ import division

import math

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(7) #aray of values of feature 'x'
y=np.array([15,14,12,0,17,14,13]) # response 
m=len(x) # number of items in the training dataset
mean = np.mean(y)
plt.plot(y,'yo')
ctr=1
p=q=0
while(ctr < 7):
    for i in range(7):
            s_squares=0
            s_normal=0
            prod_sum=0
            err = (p + q*x[i])-y[i]      
            sq_err = math.pow(err,2)
            s_squares+=sq_err
            s_normal+=err
            prod_sum+=err*x[i]
    t1= p - 0.1*(1/m)*s_normal
    t2= q - 0.1*(1/m)*prod_sum
    p=t1
    q=t2
    ctr+=1


predictions=[]
for i in range(m):
    tmp = x[i]*q + p
    predictions.append(tmp)

plt.plot(predictions)
plt.show()
