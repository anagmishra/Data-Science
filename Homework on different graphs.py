import matplotlib.pyplot as plt
import numpy as np

hours = [1, 2, 3, 4, 5, 6, 7, 8]
traffic = [11, 16, 21, 26, 31, 36, 41, 46]

plt.bar(hours, traffic)
plt.title("Bar chart")
plt.xlabel("Number of hours")
plt.ylabel("Number of vehicles")
plt.legend()
plt.show()

plt.plot(hours, traffic, color="pink", marker="s", linestyle=":", label="Trend of traffic growth")
plt.title("Line graph")
plt.xlabel("Number of hours")
plt.ylabel("Traffic")
plt.grid(True)
plt.legend()
plt.show()

marks = np.array([2, 30, 31, 45, 48, 55, 56, 58, 66, 74, 75, 79, 80, 85, 95, 97, 98, 98, 99, 99])
plt.hist(marks, bins=5, edgecolor = "black")
plt.title("Histogram")
plt.show()
print(marks[marks>75])

days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
steps = np.array([8000, 8500, 8800, 9000, 11000, 13000, 4500, 6000, 8900, 12400, 17000, 12300, 3000, 6500, 12000, 13000, 14380, 7000, 15000, 8000, 8500, 8800, 9000, 11000, 13000, 4500, 6000, 8900, 12400, 17000])
plt.plot(days, steps, color="cyan", marker="o", linestyle="--", label="Daily steps")
plt.title("Daily Steps")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.grid(True)
plt.legend()
plt.show()

days = [5, 6, 10, 11, 12, 15, 16, 17, 19, 24, 25, 29, 30]
plt.scatter(days, steps[steps>10000])
plt.title("Days above 10000 steps")
plt.show()

expenses = ["Rent", "Food", "Transport", "Entertainment", "Savings"]
shares = [25, 20, 15, 5, 35]
colors = ["Red", "Orange", "Cyan", "Lime", "Purple"]
plt.pie(shares, labels=expenses, colors=colors, shadow = True, startangle=85, autopct="%1.1f%%")
plt.title("Expenses and Contribution")
plt.show()

days = [1, 2, 3, 4, 5, 6, 7]
study = [2, 3, 1, 4, 5, 7, 8]
school = [8, 8, 7, 7, 4, 0, 0]
sleep = [11, 11, 14, 11, 14, 13, 12]
leisure = [3, 2, 2, 2, 1, 4, 4]
plt.stackplot(days, study, school, sleep, leisure, labels = ["study", "school", "sleep", "leisure"])
plt.legend()
plt.title("Time Management Schedule")
plt.xlabel("Days of the Week")
plt.ylabel("Devoted hours")
plt.show()