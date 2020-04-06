import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)

y = np.cos(x)

plt.plot(x, y)

integrale = 0
for i in range(29):
    integrale = integrale + y[i+1]*(x[i+1]-x[i])
    # dessin du rectangle
    x_rect = [x[i], x[i+1], x[i+1], x[i], x[i]]
    y_rect = [0, 0, y[i], y[i], 0]
    plt.plot(x_rect, y_rect)
print("integrale = ", integrale)

plt.show()
