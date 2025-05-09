import matplotlib.pyplot as plt

# Parameters
a = 7

# functions
def generator():
    # Parameters of the generator
    y0 = 1
    a = 65
    c = 1
    m = 2048

    # Initializing variables
    aleatorios = []

    for i in range(1000):
        if (i == 0):
            yi = ((a*y0)+c) % m
            aleatorios.append(yi/m)
        else:
            yi = ((a*aleatorios[i-1])+c) % m
            aleatorios.append(yi/m)

    return aleatorios

#Variables

X = generator()
Y = list(map(lambda x: x ** 2, X))