import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)

y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x, y1, "r--", label='cos(x)', linewidth=4)
plt.plot(x, y2, "b-.", label='sin(x)')
plt.plot(x, y1-0.5, "o", label='pas de ligne')
plt.plot(x, y1-1, ":", label='ligne :')
plt.plot(x, y1-1.5, "d", label='ligne d')

plt.legend()

plt.show()
