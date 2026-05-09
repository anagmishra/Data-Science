import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 6, 0.1)
y1 = x
plt.plot(x, y1, color="pink", marker="s", linestyle=":", linewidth=3, label="Version 1")
plt.axis([-10, 10, -10, 10])
plt.title("1st type graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()

x = np.arange(-5, 6, 0.1)
y2 = x*x
plt.plot(x, y2, color="lime", marker="o", linestyle=":", linewidth=4, label="Version 2")
plt.axis([-10, 10, 0, 30])
plt.title("2nd type graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()

x = np.arange(-5, 6, 0.1)
y3 = x*x*x
plt.plot(x, y3, color="red", marker=".", linestyle="--", linewidth=7, label="Version 3")
plt.axis([-10, 10, -10, 20])
plt.title("3rd type graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()


m = int(input("Enter the slope m:"))
c = int(input("Enter the y-intercept c:"))

x = np.arange(-20, 21)
y = m*x + c
plt.plot(x, y, color="purple", marker="o", linestyle=":", linewidth=12, label="Inputted graph")
plt.title("Inputted graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
