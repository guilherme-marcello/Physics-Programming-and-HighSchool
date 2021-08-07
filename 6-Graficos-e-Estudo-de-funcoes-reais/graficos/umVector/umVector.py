import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

x = np.array([0,1,2,3])
y = f(x)
plt.plot(x,y) # desenhar pontos
plt.savefig("graf.png")
plt.show()
