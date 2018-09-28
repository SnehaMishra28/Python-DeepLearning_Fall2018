# Importing the libraries
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import datasets

# Importing dataset
dataset = datasets.load_iris()
x = dataset.data
y = dataset.target

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# Fitting SVC Classification to the Training set with linear kernel
svc_linear = SVC(kernel='linear', C=1, gamma=0.1).fit(X_train, y_train)

# Accuracy of SVM Linear kernel on Training set
print('\n\nAccuracy of the SVM Linear Kernel Classification is: ', svc_linear.score(X_train, y_train))

# Accuracy of SVM Linear Kernel on Test Set
print('\n\nAccuracy of the SVM Linear Kernel Classification is: ', svc_linear.score(X_test, y_test))

# Fitting SVC Classification to the Training set with rbf  kernel
svc_rbf = SVC(kernel='rbf', C=1, gamma=0.1).fit(X_train, y_train)

# Accuracy of SVM Linear kernel on Training set
print('\n\nAccuracy of the SVM RBF Kernel Classification is: ', svc_rbf.score(X_train, y_train))

# Accuracy of SVM RBF Kernel on Test Set
print('\n\nAccuracy of the SVM  RBF Classification is: ', svc_rbf.score(X_test, y_test))