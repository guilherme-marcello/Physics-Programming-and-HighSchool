import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([1.1,5.5,16,27.7])

a,b,c = np.polyfit(x,y,2) # ax**2 + b*x + c
print(a)
print(b)
print(c)

def f(x):
    return a*x**2 + b*x + c

x_reg = np.linspace(min(x),max(x),1000) # mil pontos entre os máximos de x
y_reg = f(x_reg)

plt.plot(x_reg,y_reg, label="Regressão")
plt.plot(x,y,'o',label="Dados")
plt.legend()
plt.savefig("regressao2.png")
plt.show()

