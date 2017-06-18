import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.arange(0, 6, 0.1) # ganarate values with 0.1 increments in between 0 and 6
y = np.sin(x)

# draw chart
plt.plot(x, y)
plt.show()
