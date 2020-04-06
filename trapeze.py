import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)

y = np.cos(x)

plt.plot(x, y)

integrale = 0
for i in range(29):
    integrale = integrale + (y[i+1]-y[i])*(x[i+1]-x[i])/2
    # dessin du rectangle
    x_trap = [x[i], x[i+1], x[i+1], x[i], x[i]]
    y_trap = [0, 0, y[i+1], y[i], 0]
    plt.plot(x_trap, y_trap)
print("integrale = ", integrale)

plt.show()
