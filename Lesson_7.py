import matplotlib.pyplot as plt

brands = ["Adidas", "Nike", "HRX", "Tommy Hilfiger"]
shares = [30, 40, 20, 10]
plt.pie(shares, labels=brands,autopct="%1.1f%%")
plt.title("Brands and their shares")
plt.show()

#pie chart
x = ["Maths", "Physics", "Chemistry", "Biology", "History", "Geography"]
y = [93, 94, 97, 98, 100, 96]
colors = ["Red", "Orange", "Cyan", "Lime", "Pink", "Purple"]
plt.pie(y, labels=x, colors=colors, shadow=True, startangle=90, radius=1.5, counterclock=False, autopct="%1.2f%%")
plt.title("Subjects and Marks")
plt.show()

#stackplot
days = [1, 2, 3, 4, 5]
study = [2, 3, 4, 2, 3]
sports = [1, 3, 2, 4, 2]
sleep = [8, 6, 4, 5, 6]
plt.stackplot(days, study, sports, sleep, labels=["study", "sports", "sleep"])
plt.legend(loc = "upper left")
plt.title("Daily routine")
plt.show()

#scatterplot - They show the relationship between variables
studyhrs = [1, 2, 3, 4, 5, 6]
marks = [20, 30, 40, 60, 80, 95]
plt.scatter(studyhrs, marks)
plt.title("Study hours and effect on marks")
plt.show()

#subplots - Two graphs together
marks = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
plt.hist(marks, bins=8, edgecolor = "black")
plt.title("Histogram")
plt.show()

#Histogram - Used for frequency distribution