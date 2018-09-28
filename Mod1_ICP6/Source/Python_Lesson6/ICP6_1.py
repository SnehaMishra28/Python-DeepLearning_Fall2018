import pandas as pd
import numpy as np
import matplotlib as math
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

# Importing dataset
irisdataset = datasets.load_iris()
x = irisdataset.data
y = irisdataset.target

'''attr_name = ['sepal length','sepal width','petal length','petal width']
field_names = ['Num']+attr_name + ['class']
data = pd.read_csv("iris.csv", names=field_names)'''

# split the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

# split the data for training and testing
model = GaussianNB().fit(x_train, y_train)
predicted = model.predict(x_test)
print(np.mean(model == y_test))

# Accuracy of NavesBayes on Training Sets
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(model.score(x_train, y_train)))

# Accuracy of NavesBayes on Testing Sets
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(model.score(x_test, y_test)))


# print the accuracy score of predicted and actual values on test set
print('\n\nAccuracy of the Naive Bayes Classification is on Test Data Prediction: ', model.score(x_test, y_test))


# Function to split data to test and train sets
def splitdata(data, blocks_num = 1, test_block=0):
    blocks = np.array_split(data,blocks_num)
    test_set = blocks[test_block]
    if blocks_num > 1:
        del blocks[test_block]
    training_set = pd.concat(blocks)
    return training_set, test_set


'''def predict(self):
    predictions = {}
    for _, row in self.__test_set.iterrows():
        results = {}
        for k, v in self.__priors:
            p = 0
            for attribute in attr_name:
                prob = self.__calculate_probability(row[attribute], self.__mean_variance[
                    k][attr_name][0], self.__mean_variance[k][attribute][1])
                if prob > 0:
                    p += math.log(prob)
            results[k] = math.log(v) + p
        predictions[int(row["Num"])] = max([key for key in results.keys() if results[
            key] == results[max(results, key=results.get)]])
    return predictions


def calculate_accuracy(test_set, predictions):
    correct = 0
    for _, t in test_set.iterrows():
        if t["class"] == predictions[t["Num"]]:
            correct += 1
    return (correct / len(test_set)) * 100.0'''