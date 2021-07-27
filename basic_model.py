import pickle
from keras.models import Input,Model
from keras.layers import Dense,Flatten,Concatenate,Reshape
from keras.layers.convolutional import Conv2D
from keras.callbacks import EarlyStopping
import os
os.chdir('C:\Users\v_sim\Desktop\Files\Data')

with open('X.pkl', 'rb') as f:
    X = pickle.load(f)
    
with open('y.pkl', 'rb') as f:
    y = pickle.load(f)
    
print(X.shape)
print(y.shape)

epochs = 100

input_layer= Input(shape=(8,8,12))
x = Conv2D(filters=64,kernel_size = 2,strides = (2,2))(input_layer)
x = Conv2D(filters=128,kernel_size=2,strides = (2,2))(x)
x = Conv2D(filters=256,kernel_size=2,strides = (2,2))(x)
x = Flatten()(x)

x = Dense(4096,activation = 'softmax')(x)
output = Reshape((1,64,64))(x)

model = Model(inputs=input_layer,outputs=output)
es = EarlyStopping(monitor='loss')

model.compile(optimizer = 'adam',loss = 'categorical_crossentropy')

model.fit(X,y,epochs = epochs,callbacks = [es])

model.save('chess_model')