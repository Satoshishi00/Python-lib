import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.pie([24, 18],
       labels=["Femmes", "Hommes"],
       autopct="%1.1f pourcents")
plt.title("Représentation hommes - femmes")
plt.show()
