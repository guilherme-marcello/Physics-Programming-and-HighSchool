from sympy import *
var("t") # a variável t passa a ser simbólico
f_symb = 2*t**2 + t + 2
f_der1_symb = f_symb.diff(t) # derivar f_symb
f_der2_symb = f_der1_symb.diff(t) # derivar a primeira derivada
print(f_der1_symb)  
print(f_der2_symb)
f_symb(2)
