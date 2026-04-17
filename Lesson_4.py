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