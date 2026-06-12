import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Splitting the data into training and testing:
from sklearn.model_selection import train_test_split
# Alogrithm that we will be using for the predictions/ applying the machine learning
from sklearn.tree import DecisionTreeClassifier
# For finding accuracy
from sklearn import metrics

data = pd.read_csv("iris.csv")
print(data.head())
print(data.info())

# Data preprocessing
data["variety_replace"] = data["variety"].replace({"Setosa": "1", "Versicolor": "2", "Virginica": "3"})
print(data.head())

#Data Visualization
#x = data["variety"]
#y = data["petal.length"]
#plt.scatter(x, y)
#plt.title("Relationship of petal length with variety")
#plt.legend()
#plt.show()

#x = data["variety"]
#y = data["sepal.length"]
#plt.scatter(x, y)
#plt.title("Relationship of sepal length with variety")
#plt.legend()
#plt.show()

y = data["variety_replace"]
x = data.drop("variety_replace", axis = 1)
#If you want to drop row-wise, axis = 1, if you want to drop column-wise, axis = 0
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
print(x_train.shape)
