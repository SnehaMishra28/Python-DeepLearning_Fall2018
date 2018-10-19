from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# load dataset
dataset = pd.read_csv("housing.csv", header=None).values
print(dataset[:,0:13])

#dataset[:,0:13] -> before colon (:) means consider all instances (all observances), 0:13 means 0th col to 13th col
#dataset[:,13] -> before colon (:) means consider all instances (all observances), 13 means just the target (just the last col)
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:13], dataset[:,13],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)

# create model
my_first_nn = Sequential()

# Instantiate
linreg = LinearRegression()

# Fitting model to train  data
linreg.fit(X_train, Y_train)

y_pred = linreg.predict(X_test)

print(metrics.mean_absolute_error(Y_test, y_pred))

#print(metrics.mean_squared_error())

#Adding the input layer using Dense function
my_first_nn.add(Dense(20, input_dim=13, activation='relu')) # hidden layer

#Adding the input layer using Dense function
my_first_nn.add(Dense(32, activation='relu')) # hidden layer

#Adding the output layer using Dense function
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer

#Compile the model
my_first_nn.compile(loss='mean_squared_error', optimizer='adam')

#Fit the model as per the train datasets
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)

#Get the summary
print(my_first_nn.summary())

#Evaluate the accuracy of the model
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))