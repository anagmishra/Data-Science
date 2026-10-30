import pandas as pd
d1 = {"name":["Anag", "Rohit", "Aashi"], "age":[16, 17, 18], "city":["Lucknow", "Delhi", "Mumbai"]}
df = pd.DataFrame(d1)
print(df.head())
print(df.shape)
print(df["name"])
print(df["age"].max())
print(type(df["age"]))
print(df["age"].shape)
print(df.info()) #Gives typical summary of data
print(df.describe()) #It givtes the important calculations on the numerical columns
#csv stands for comma separated values
data = pd.read_csv("titanic.csv")
print(data.head())
print(data.info())
print(data.describe())
print(data.dtypes)
nameandage = df[["name", "age"]]
print(nameandage.head())
#filtering out rows
above35 = data[data["Age"]>35]
print(above35.head())
print(above35.shape)
#Combining multiple conditions together
class2and3 = data[data["Pclass"].isin([2, 3])]
print(class2and3[["Name", "Pclass"]].head())
print(class2and3.shape)
class2a3 = data[(data["Pclass"]==2)| (data["Pclass"]==3)]
print(class2a3[["Name", "Pclass"]].head())
print(class2a3.shape)
age = data[(data["Age"]>=20) & (data["Age"]<=30)]
print(age[["Name", "Age"]].head())
print(age.shape)
male1 = data[(data["Sex"]=="male") & (data["Pclass"]==1)]
print(male1["Fare"].mean())
female1 = data[(data["Sex"]=="female") & (data["Pclass"]==1)]
print(female1["Fare"].mean())
male2 = data[(data["Sex"]=="male") & (data["Pclass"]==2)]
print(male2["Fare"].mean())
female2 = data[(data["Sex"]=="female") & (data["Pclass"]==2)]
print(female2["Fare"].mean())
male3 = data[(data["Sex"]=="male") & (data["Pclass"]==3)]
print(male3["Fare"].mean())
female3 = data[(data["Sex"]=="female") & (data["Pclass"]==3)]
print(female3["Fare"].mean())