import numpy as np
from matplotlib import pyplot as plt

x = [0, 2, 3, 4, 5]
y = [0, 4, 9, 16, 25]
c = ["red", "green", "green", "green", "red"]
plt.scatter(x, y, color=c)

#plt.show()


def graph(formula, x_range):  
    x = np.array(x_range)  
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)  
    plt.show()  

def my_formula(x):
    return 5*x - 2.5

graph(my_formula, range(0, 7))