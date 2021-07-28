import os
import pickle
os.chdir('C:\Users\v_sim\Desktop\Files\Data')

def get_data():
    with open('X.pkl', 'rb') as f:
        X = pickle.load(f)
        
    with open('y.pkl', 'rb') as f:
        y = pickle.load(f)
        
    print(X.shape)
    print(y.shape)
    return X,y