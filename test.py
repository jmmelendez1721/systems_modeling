import matplotlib.pyplot as plt
import numpy as np
y0 = 1
a = 65
c = 1
m = 2048

aleatorios = []
back_ale = []

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

#plt.scatter(back_ale, aleatorios, alpha=0.5, s=10)


#plt.plot(aleatorios[:-1], aleatorios[1:], '*')
#plt.plot(back_ale[:-1], back_ale[1:], '*')
#plt.plot(aleatorios, back_ale, '*')

plt.scatter(aleatorios, back_ale, alpha=0.3, s=3, color='blue')
plt.title("Correlación entre xi_j y xi_{j+1}")
plt.xlabel("xi_j")
plt.ylabel("xi_{j+1}")
plt.grid(True)

plt.show()