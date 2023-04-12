import numpy as np
import random
X = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
layer_weights =[0.3,0.3,0.3]
T=[0,1,0,1,0,1,1,1]

#(x1/\x2)\/x3
theta = 0.5
nu = 0.02
y_list=[]
def activation(x, layer_weights, theta):
    a=0
    for x_i, weight_i in zip(x,layer_weights):
        a+=x_i*weight_i
    if a > theta:
        return 1
    else:
        return 0
while True:
    delta_sum=0
    for x,t in zip(X,T):
        y=activation(x,layer_weights,theta)
        delta = t-y
        delta_sum=delta_sum+abs(delta)
        if t==y:
            y_list.append(y)
        #print(x,y,delta)
        d=[nu * delta * x_i for x_i in x]
        for i in range(len(layer_weights)):
            layer_weights[i]= layer_weights[i] +d[i]
    if delta_sum==0:
        break
    else:
        y_list.clear()
for i in range(len(T)):
    print(X[i],y_list[i])
print(layer_weights)