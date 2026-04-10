import pandas as pd
d1 = {"name": ["Divya", "Kriti", "Ranvijay", "Cyrus", "Shekhar", "Sanya"], "Maths": [100, 99, 98, 97, 96, 95], "Science": [92, 90, 88, 86, 84, 82], "English": [34, 56, 78, 98, 100, 24]}
df = pd.DataFrame(d1)
print(df["Maths"].mean())
print(df["Science"].mean())
print(df["English"].mean())
print(df["Maths"].max())
print(df["Science"].max())
print(df["English"].max())