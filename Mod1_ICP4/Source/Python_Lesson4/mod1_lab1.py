#Import numpy
import numpy as np

# Initializing arrays
a = np.array([1,2,3,1,2,1,1,1,3,2,2,1])
b = np.array([12,12,3,12,12,1,12,1,3,2,2,11])

# Printing the arrays
print(a)
print(b)

countsa = np.bincount(a)
countsb = np.bincount(b)
print(countsa)
print(countsb)

print(np.argmax(countsa))
print(np.argmax(countsb))
print(np.max(countsb))