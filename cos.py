import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.cos(x)

plt.xlim(0, 2*np.pi)
plt.ylim(-1.1, 1.1)

plt.title("Fonction cosinus")

plt.plot(x, y, label="cos(x)")
plt.legend()

plt.xlabel("abscisses")
plt.ylabel("ordonnées")

plt.show()
