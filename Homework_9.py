import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

data = pd.read_csv("adult.csv")

print(data.head())
print(data.info())

data.columns = ("age", "workclass", "fnlwgt", "education", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss", "hours_per_week", "native_country", "income")


data["income"] = data["income"].replace({"<=50K": 0, ">=50K": 1})

y = data["income"]
x = data.drop({"income", "workclass", "education", "marital_status", "occupation", "relationship", "race", "sex", "native_country"}, axis = 1)
print(x.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1) 
print(x_train.shape)

model = DecisionTreeClassifier(max_depth = 3, random_state=1) 
model.fit(x_train, y_train) 

predictions = model.predict(x_test) 
print("Accuracy", metrics.accuracy_score(predictions, y_test))