import matplotlib.pyplot as plt
import numpy as np

u = np.array([4.54,4.51,4.49,4.47,4.42,4.33,4.29])
i = np.array([0.0419,0.05,0.0569,0.072,0.099,0.1378,0.172])

neg_r,e = np.polyfit(i,u,1) # u = -r.i + e
print("Valor de r: ", -neg_r)
print("Valor de e: ",e)
def f(x):
    return neg_r*x + e

i_reg = np.linspace(min(i),max(i),1000) # mil pontos
u_reg = f(i_reg)


plt.plot(i_reg,u_reg, label="Regressão")
plt.plot(i,u,'o',label="Dados")
plt.title("AL 2.1: Características da pilha nova")
plt.xlabel("I (A)")
plt.ylabel("U (V)")
plt.legend()
plt.savefig("regressaoPilhaNova.png")
plt.show()
