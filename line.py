import numpy as np
import matplotlib.pyplot as plt

# x1 = np.linspace(min, max, nb_points)
x1 = np.linspace(0, 15, 7)
print(x1)

y = np.zeros(7)
print(y)

#plt.plot(x1, y, 'o')
plt.plot(x1, y, 'o')

plt.xlim(0, 10)
plt.ylim(-1, 3)

plt.show()

