from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# load dataset
dataset = pd.read_csv("diabetes.csv", header=None).values

#dataset[:,0:8] -> before colon (:) means consider all instances (all observances), 0:8 means 0th col to 8th col
#dataset[:,8] -> before colon (:) means consider all instances (all observances), 8 means just the target (just the last col)
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)

# create model
my_first_nn = Sequential()

#Adding the input layer using Dense function
my_first_nn.add(Dense(20, input_dim=8, activation='relu')) # hidden layer

#Adding other input layer using Dense function
my_first_nn.add(Dense(32, input_dim=8, activation='relu')) # adding second hidden layer
#my_first_nn.add(Dense(64, activation='relu')) # adding third hidden layer
#my_first_nn.add(Dense(128,  activation='relu')) # adding fourth hidden layer  //with input dim=8,output =64

#Adding the output layer using Dense function
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer

#Compile the model
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')

#Fit the model as per the train datasets
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)

#Get the summary
print(my_first_nn.summary())

#Evaluate the accuracy of the model
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))