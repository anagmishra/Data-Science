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