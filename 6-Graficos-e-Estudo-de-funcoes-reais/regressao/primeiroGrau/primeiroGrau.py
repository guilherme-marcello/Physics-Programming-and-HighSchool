import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([1.2,2.9,5.3,7.7])

m,b = np.polyfit(x,y,1) # mx + b
print(m)
print(b)

def f(x):
    return m*x + b

x_reg = np.linspace(min(x),max(x),1000) # mil pontos entre os máximos de x
y_reg = f(x_reg)

plt.plot(x_reg,y_reg, label="Regressão")
plt.plot(x,y,'o',label="Dados")
plt.legend()
plt.savefig("regressao1.png")
plt.show()
