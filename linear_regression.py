import matplotlib.pyplot as plt
import numpy as np 
x=np.arange(9) #array of values of feature 'x'
y=np.array([1,3,2,5,7,8,8,9,10,12]) # response 
print y
plt.plot(y,'bo')
plt.ylabel('Responses')
plt.xlabel('Features')
plt.show()