import pandas as pd
data = pd.read_csv("titanic.csv")

print(data[["Age", "Fare", "Sex"]].groupby("Sex").mean())

print(data[data["Survived"]==1].groupby("Pclass").count())

print(data.agg({"Age":"max", "Fare": "max"}))

data = data.sort_values(by="Pclass", ascending=True)
data = data.sort_values(by="Fare", ascending=False)
print(data["Pclass"].head())
print(data["Fare"].head())

data["NameLower"] = data["Name"].str.lower()
print(data["NameLower"].head())
data["Surname"] = data["Name"].str.split(" ").str[-1]
print(data["Surname"].head())
data["Sex_short"] = data["Sex"].replace({"male": "M", "female": "F"})
print(data[["Sex_short", "Name"]].head())