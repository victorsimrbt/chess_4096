import pickle
import numpy as np
import os
os.chdir('C:\Users\v_sim\Desktop\Files\Data')

with open('dataset.pkl', 'rb') as f:
    dataset = pickle.load(f)
    
X,y = np.hsplit(dataset,2)

print(X.shape,y.shape)

new_X = []
for i in range(len(X)):
    new_X.append(X[i][0])
    
new_y = []
for i in range(len(y)):
    value = y[i][0]
    zeros_1 = np.zeros((64,64))
    zeros_1[value[0],value[1]] = 1
    val = [zeros_1]
    new_y.append(val)
    
with open('X.pkl', 'wb') as f:
    pickle.dump(np.array(new_X), f)
    
with open('y.pkl', 'wb') as f:
    pickle.dump(np.array(new_y), f)