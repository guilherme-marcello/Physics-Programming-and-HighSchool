import matplotlib.pyplot as plt

def f(x):
    return x**2

x = [0,1,2,3,4]
y = [f(elemento) for elemento in x]

plt.plot(x,y)
plt.savefig("save.png")
plt.show()


