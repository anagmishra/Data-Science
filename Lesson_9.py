import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
#Similar to matplotlib, except more graphical

data = pd.read_csv("COVID.csv")

print(data.head())
print(data.info())

data.columns = ("DateReported", "Country_code", "Country", "WHO_region", "New_cases", "Cumulative_cases", "New_deaths", "Cumulative_deaths")

#Date Reported is a string, so we are changing it to time format
data["DateReported"] = pd.to_datetime(data["DateReported"])

timeseriesdata = data.groupby("DateReported").sum()

f1 = go.Figure() #Creates empty canvas
f1.add_trace(go.Scatter(x = data.index, y = data["Cumulative_cases"], fill = "tonexty", line_color = "cyan"))
f1.update_layout(title = "Cumulative deaths worldwide")
f1.write_html("f1.html", auto_open = True)

f2 = go.Figure()
f2.add_trace(go.Scatter(x = data.index, y = data["Cumulative_deaths"], fill = "tonexty", line_color = "lime"))
f2.update_layout(title = "Cumulative deaths")
f2.write_html("f2.html", auto_open = True)

f3 = go.Figure()
f3.add_trace(go.Scatter(x = data.index, y = data["New_cases"], fill= "tonexty", line_color = "red"))
f3.update_layout(title = "New cases")
f3.write_html("f3.html", auto_open = True)

f4 = go.Figure()
f4.add_trace(go.Scatter(x = data.index, y = data["New_deaths"], fill = "tonexty", line_color = "orange"))
f4.update_layout(title = "New deaths")
f4.write_html("f4.html", auto_open = True)