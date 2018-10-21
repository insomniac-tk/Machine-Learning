import random
import matplotlib.pyplot as plt
"""
K-Means falls under the category of centroid-based clustering. A centroid is a data point (imaginary or real) at the center of a cluster. In centroid-based clustering, clusters are represented by a central vector or a centroid. 
This centroid might not necessarily be a member of the dataset.
Centroid-based clustering is an iterative algorithm in which the notion of similarity is derived by how close a data point is to the centroid of the cluster.
"""

print("A basic example of centroid based clustering!")

xs = []
ys = []
#generating random data points 
for i in range(500):
    tmp=[]
    x= random.randint(1,500)
    y = random.randint(1,500)
    xs.append(x)
    ys.append(y)

c1_index = random.randint(1,len(xs)) #Choose a random index
c2_index = random.randint(1,len(xs))
c1 = xs[c1_index],ys[c1_index] #get the element from that index to serve as centroid
c2 = xs[c2_index],ys[c2_index]

cluster_1 = []
cluster_2 = []

print("Centroids :",c1,",",c2)

for i in range(len(xs)):
    tmp=[] # current coordinate pair x,y
    tmp.append(xs[i])
    tmp.append(ys[i])
    dist_c1 = abs(xs[i]-c1[0]) + abs(ys[i]-c1[1])#|x1-c1.x| + |y1-c1.y|
    dist_c2 = abs(xs[i]-c2[0]) + abs(ys[i]-c2[1])
    
    if dist_c1 <= dist_c2:
        cluster_1.append(tmp) #current x,y is closer to cluster1
    else:
        cluster_2.append(tmp) #current point closer to cluster 2

print(cluster_1,"\n",cluster_2)
#cluster1 and cluster2 are a lists of lists
c1_x=[]
c1_y=[]
c2_x=[]
c2_y=[]

for i in range(len(cluster_1)):
    c1_x.append(cluster_1[i][0])
    c1_y.append(cluster_1[i][1]) 

for i in range(len(cluster_2)):
    c2_x.append(cluster_2[i][0])
    c2_y.append(cluster_2[i][1]) 

plt.plot(xs,ys,'bo')
plt.axis([0,520,0,520])
plt.show()    
plt.plot(c1_x,c1_y,'ro',c2_x,c2_y,'yo')
plt.show()