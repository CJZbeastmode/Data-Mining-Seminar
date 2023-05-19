import numpy as np
from matplotlib import pyplot as plt

x = [1, 2, 3, 8, 9, 10]
y = [0, 0, 0, 0, 0, 0]
c = ["red", "red", "red", "green", "red", "green"]
plt.scatter(x, y, color=c)
plt.axvline(x = 5.5, color = 'b', label = 'axvline - full height')

plt.show()