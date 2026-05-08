import matplotlib.pyplot as plt
import numpy as np
x=[1, 2 ,3]
y=[4, 5, 6]
plt.plot(x, y)
plt.title("Line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#Matplotlib is used for making graphs and charts for better understanding of data
x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
y = [4, 6, 2, 8, 4, 7, 4]
plt.plot(x, y, color="cyan", marker="o", linestyle="--", linewidth=2, markersize=8, label="Temperature")
plt.title("Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.grid(True)
plt.legend()
plt.show()
"""Marker means adding symbols on data points. 
Linestyle means changing the style of the line"""
x = np.arange(-10, 11)
y= 2*x+3
plt.plot(x, y, color="lime", marker="o", linestyle="--", linewidth=3, markersize=9, label="Mathematical Operations")
plt.title("Mathematical Operations in Graphs")
plt.xlabel("X-axis")
plt.ylabel("Operated Y-axis")
plt.grid(True)
plt.legend()
plt.show()

x=np.arange(10, 30)
y=-x+5
plt.plot(x, y, color="red", marker=".", label="Calculations")
plt.title("Calculations in graphs")
plt.xlabel("X-axis")
plt.ylabel("Calculated Y-axis")
plt.grid(True)
plt.legend()
plt.show()

x=np.arange(20, 41)
y=2*x-5
plt.plot(x, y, color="pink", marker="s", linestyle=":", label="One more")
plt.title("Additional Calculations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()