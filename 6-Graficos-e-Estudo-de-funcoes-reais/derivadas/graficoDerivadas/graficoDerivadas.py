from sympy import *
import numpy as np
import matplotlib.pyplot as plt

var("t")
f_symb = 2*t**2 + t + 2
f_der1_symb = f_symb.diff(t) 
f_der2_symb = f_der1_symb.diff(t) 

f = lambdify(t,f_symb)
f_der1 = lambdify(t,f_der1_symb)
f_der2 = lambdify(t,f_der2_symb)

x = np.linspace(0,3,100)
y = f(x)
y_der1 = f_der1(x)
y_der2 = np.full(100,f_der2(x)) # vetor com 100 valores f_der2(x)

plt.plot(x,y,label="$f(t)$")
plt.plot(x,y_der1,label="$f'(t)$")
plt.plot(x,y_der2,label="$f''(t)$")
plt.legend()
plt.savefig("derivadas.png")
plt.show()
