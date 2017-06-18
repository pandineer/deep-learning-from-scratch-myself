import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.arange(0, 6, 0.1) # ganarate values with 0.1 increments in between 0 and 6
y1 = np.sin(x)
y2 = np.cos(x)

# draw chart
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos") # draw chart using dashed line
plt.xlabel("x") # x-axis label
plt.ylabel("y") # y-axis label
plt.title('sin & cos') # title
plt.legend()
plt.show()
