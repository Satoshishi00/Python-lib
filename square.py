import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 1, 0, 0])
y = np.array([0, 0, 1, 1, 0])

plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)

# garder un raport de proportionnalité égual entre l'abscisse et l'ordonné
plt.axis("equal")

plt.plot(x, y, label="square")

plt.legend()

plt.show()
