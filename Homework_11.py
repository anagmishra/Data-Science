import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("COVID.csv")

print(data.head())
print(data.info())