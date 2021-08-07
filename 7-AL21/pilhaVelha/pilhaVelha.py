import matplotlib.pyplot as plt
import numpy as np

u = np.array([3.75,3.71,3.55,3.35,3.19])
i = np.array([0.0348,0.0415,0.0692,0.1085,0.1290])

neg_r,e = np.polyfit(i,u,1) # u = -r.i + e
print("Valor de r: ", -neg_r)
print("Valor de e: ",e)
def f(x):
    return neg_r*x + e

i_reg = np.linspace(min(i),max(i),1000) # mil pontos
u_reg = f(i_reg)


plt.plot(i_reg,u_reg, label="Regressão")
plt.plot(i,u,'o',label="Dados")
plt.title("AL 2.1: Características da pilha velha")
plt.xlabel("I (A)")
plt.ylabel("U (V)")
plt.legend()
plt.savefig("regressaoPilhaNova.png")
plt.show()
