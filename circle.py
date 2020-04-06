import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 50)

x = np.cos(theta)
y = np.sin(theta)

plt.plot(x, y)
plt.axis("equal")

plt.show()
