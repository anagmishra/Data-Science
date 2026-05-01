import pandas as pd
data = pd.read_csv("titanic.csv")
age1 = data[(data["Age"]>=20) & (data["Age"]<=40)]
print(age1["Name"])
print(age1["Fare"])

fare1 = data[data["Fare"]>100]
print(fare1[["Name", "Pclass"]])
print("\n")
survived = data[(data["Survived"] == 1) & (data["Pclass"] == 3)]
print(survived["Name"])

data.iloc[0:5, 2] = "Test passenger"
print(data["Name"])

data.iloc[10:26, 7] = 24
print(data[["Name", "Fare"]])

data["Fare Rate"] = data["Fare"]/(data["Siblings/Spouses Aboard"] + 1)
print(data.info())
print(data[["Name", "Fare Rate"]])

data.loc[data["Age"] < 12, "AgeGroup"] = "Child"
data.loc[(data["Age"] >= 12) & (data["Age"] <= 18), "AgeGroup"] = "Teen"
data.loc[data["Age"] > 18, "AgeGroup"] = "Adult"
print(data[["Name", "AgeGroup"]])
print(data["Name"].count())