import pandas as pd
df = pd.read_csv("titanic.csv")
#To get the particular column out the condition
names = df.loc[df["Age"]>18,"Name"]
print(names)
#Slicing - First one is for rows, second one is for columns
print(df.iloc[9:25,2:5])
#Changing the value in the dataset - Specify the number of rows and columns we want to change
df.iloc[0:3, 2] = "Alex"
print(df["Name"])
#to_csv is used to save the data
df.to_csv("titanic1.csv")
#Creating a new column in the data frame
df["new_column"] = df["Fare"] + 20
print(df["new_column"])
df["column2"] = df["Fare"] * df["Pclass"]
print(df["column2"])
#Renaming the column name
df_rename = df.rename(columns={"Pclass":"Passenger Class", "Fare":"Payment"})
print(df_rename.info())
#Performing mathematical calculations on multiple columns
print(df[["Age", "Fare"]].mean())
print(df.agg({"Age": ["min", "max", "median"],
              "Fare": ["min", "max", "median"]}))
#Group by data (category wise)
print(df[["Pclass", "Age"]].groupby("Pclass").mean())
print(df.groupby("Pclass")["Age"].mean())
#Sorting the data
df = df.sort_values(by="Age")
print(df[["Name", "Age"]].head())
df.sort_values(by=["Pclass", "Age"], ascending=False)
print(df[["Pclass", "Age"]].head())
#Operations on text data
df["Name_lower"] = df["Name"].str.lower()
print(df["Name_lower"].head())
df["Name_split"] = df["Name"].str.split(" ")
print(df["Name_split"].head())
df["Sex_replace"] = df["Sex"].replace({"male": "Male", "female": "Female"})
print(df["Sex_replace"].head())