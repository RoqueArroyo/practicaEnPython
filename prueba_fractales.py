import numpy as np
import matplotlib.pyplot as plt

# Funciones del IFSP para Sierpiński
def f1(x, y):
    return x/2, y/2

def f2(x, y):
    return x/2 + 0.5, y/2

def f3(x, y):
    return x/2, y/2 + 0.5

funciones = [f1, f2, f3]
probabilidades = [1/3, 1/3, 1/3]

# Juego del Caos
x, y = 0, 0
n_iteraciones = 50000
puntos = np.zeros((n_iteraciones, 2))

for i in range(n_iteraciones):
    f = np.random.choice(funciones, p=probabilidades)
    x, y = f(x, y)
    puntos[i] = [x, y]

# Graficar (omitir primeros 100 puntos)
plt.figure(figsize=(8, 8))
plt.scatter(puntos[100:, 0], puntos[100:, 1], s=0.1, c='black')
plt.axis('off')
plt.show()