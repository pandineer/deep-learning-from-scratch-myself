import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 2 is correct answer
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# If 2 has highest probability
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(mean_squared_error(np.array(y), np.array(t)))

# If 7 has highest probability
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(mean_squared_error(np.array(y), np.array(t)))
