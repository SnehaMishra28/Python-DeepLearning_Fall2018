import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating Dataframe Wine using panda libraries
wine = pd.read_csv('winedata.csv')

# Print the first 5 rows from wine data using head() function
print(wine.head())

# Printing the unique Class from values from csv file
print('The wine data Contains following Unique Class Value:', wine['Class'].unique())

# Describe the wine data
print(wine.describe())

# Plot the Categories in wine data using seaborn and matplotlib
sns.countplot(wine['Class'], label="Count")
plt.show()
