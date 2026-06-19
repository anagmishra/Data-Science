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
data["variety"] = data["variety"].replace({"Setosa": 0, "Versicolor": 1, "Virginica": 2})
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

#x = data["variety"]
#y = data["petal.width"]
#plt.scatter(x, y)
#plt.title("Relationship of petal width with variety")
#plt.legend()
#plt.show()

#x = data["variety"]
#y = data["sepal.width"]
#plt.scatter(x, y)
#plt.title("Relationship of sepal width with variety")
#plt.legend()
#plt.show()

y = data["variety"]
x = data.drop("variety", axis = 1)
#If you want to drop row-wise, axis = 1, if you want to drop column-wise, axis = 0
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1) #Test size is to decide what part of the data is for training and what part is for testing, whereas random_state is to ensure that not a lot of data is jumbled when trained and tested
print(x_train.shape)

model = DecisionTreeClassifier(max_depth = 3, random_state=1) #Max_depth gives nmaximum number of classifications
model.fit(x_train, y_train) #It starts the training part

predictions = model.predict(x_test) #Gives predictions on data of x_test and tests accuracy of those predictions with y_test values
print("Accuracy", metrics.accuracy_score(predictions, y_test)) #Gives the accuracy score, but it must the y_test value, not the x_test one