import matplotlib.pyplot as plt

# Parameters of the generator
y0 = 1
a = 65
c = 1
m = 2048

# Initializing variables

aleatorios = []
back_ale = []

# Generating random numbers on a Normal distribution

for i in range(1000):
    if (i == 0):
        yi = ((a*y0)+c) % m
        aleatorios.append(yi)
        back_ale.append(y0)
    else:
        yi = ((a*aleatorios[i-1])+c) % m
        aleatorios.append(yi)
        back_ale.append(aleatorios[i-1])

for j in range(len(aleatorios)):
    aleatorios[j] = aleatorios[j]/m
    back_ale[j] = back_ale[j]/m

# Ploting

plt.scatter(aleatorios, back_ale, alpha=0.3, s=3, color='blue')
plt.title("Correlación de variable aleatoria generada")
plt.xlabel("xi_j")
plt.ylabel("xi_{j+1}")
plt.grid(True)
plt.show()