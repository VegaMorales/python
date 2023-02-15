import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import math

def funcion(x):
    return (math.sqrt(1-pow((abs(x)-1),2)))

x = np.arange(-2,2,0.1)
y = funcion(x)
z1 = abs(x)-1
z2 = pow(z1,2)
z3 = 1-z2
#y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title("Dia del amor y la amistad")
plt.legend()
plt.savefig('corazon.png')
plt.show()

