import matplotlib.pyplot as plt
import numpy as np

#Bar plots are used when comparing categories, comparing quantities, and showing rankings
products = ["Shoes", "Bags", "Pens", "Clothes", "laptops"]
sales = [6, 34, 87, 25, 98]
plt.bar(products, sales)
plt.title("Bar chart")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

students = ["Rohan", "Kevin", "Yashwanth", "Jonathan", "Arisha", "Zahra"]
marks = [87, 94, 90, 88, 93, 99]
colors = ["red", "pink", "lime", "cyan", "orange", "black"]
plt.bar(students, marks, color=colors)
plt.title("Marks of students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()