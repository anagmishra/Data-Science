import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data = pd.read_csv("iris.csv")
print(data.head())
print(data.info())

data["variety"] = data["variety"].replace({"Setosa": 0, "Versicolor": 1, "Virginica": 2})
print(data.head())

y = data["variety"]
x = data.drop(["variety","sepal.length"], axis = 1)
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1) 

model = DecisionTreeClassifier(max_depth = 3, random_state=1) 
model.fit(x_train, y_train)

predictions = model.predict(x_test) 
print("Accuracy", metrics.accuracy_score(predictions, y_test)) 

y = data["variety"]
x = data.drop(["variety","sepal.width"], axis = 1)
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1) 

model = DecisionTreeClassifier(max_depth = 3, random_state=1) 
model.fit(x_train, y_train)

predictions = model.predict(x_test) 
print("Accuracy", metrics.accuracy_score(predictions, y_test)) 

y = data["variety"]
x = data.drop(["variety","petal.length"], axis = 1)
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1) 

model = DecisionTreeClassifier(max_depth = 3, random_state=1) 
model.fit(x_train, y_train)

predictions = model.predict(x_test) 
print("Accuracy", metrics.accuracy_score(predictions, y_test)) 

y = data["variety"]
x = data.drop(["variety","petal.width"], axis = 1)
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1) 

model = DecisionTreeClassifier(max_depth = 3, random_state=1) 
model.fit(x_train, y_train)

predictions = model.predict(x_test) 
print("Accuracy", metrics.accuracy_score(predictions, y_test)) 
