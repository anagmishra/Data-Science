import pandas as pd
data = pd.read_csv("iris.csv")
sepal_length = data["sepal.length"]
sepal_width = data["sepal.width"]
petal_length = data["petal.length"]
petal_width = data["petal.width"]
row1 = data[data["variety"]=="Setosa"]
row2 = data[data["variety"]=="Versicolor"]
row3 = data[data["variety"]=="Virginica"]

print(row1.shape)
print(row2.shape)
print(row3.shape)


print(sepal_length.head())
print(sepal_length.info())
print(sepal_length.mean())
print(sepal_length.min())
print(sepal_length.max())

print(sepal_width.head())
print(sepal_width.info())
print(sepal_width.mean())
print(sepal_width.min())
print(sepal_width.max())

print(petal_length.head())
print(petal_length.info())
print(petal_length.mean())
print(petal_length.min())
print(petal_length.max())

print(petal_width.head())
print(petal_width.info())
print(petal_width.mean())
print(petal_width.min())
print(petal_width.max())
