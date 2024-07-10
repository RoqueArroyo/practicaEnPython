import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generar los vértices del teseracto
def generar_teseracto():
    return np.array([[(int(i >> j) & 1)-0.5 for j in range(4)] for i in range(16)])

# Proyectar de 4D a 3D
def proyectar(vertices, angle):
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    
    # Matrices de rotación en 4D (rotación en el plano wx y yz)
    rot_wx = np.array([
        [cos_angle, 0, 0, -sin_angle],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [sin_angle, 0, 0, cos_angle]
    ])
    
    rot_yz = np.array([
        [1, 0, 0, 0],
        [0, cos_angle, -sin_angle, 0],
        [0, sin_angle, cos_angle, 0],
        [0, 0, 0, 1]
    ])

    # Aplicar rotaciones
    rotated = vertices @ rot_wx @ rot_yz

    # Proyección simple de 4D a 3D (ignorando w)
    return rotated[:, :3]

# Conectar vértices para dibujar el teseracto
def conectar_vertices(ax, vertices):
    edges = [
        (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7),
        (4, 5), (4, 6), (5, 7), (6, 7), (8, 9), (8, 10), (8, 12), (9, 11),
        (9, 13), (10, 11), (10, 14), (11, 15), (12, 13), (12, 14), (13, 15),
        (14, 15), (0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)
    ]
    for (i, j) in edges:
        ax.plot3D(*zip(vertices[i], vertices[j]), color="b")

# Función de actualización para la animación
def actualizar(frame):
    angle = frame * np.pi / 180
    vertices_proyectados = proyectar(vertices, angle)
    ax.cla()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    conectar_vertices(ax, vertices_proyectados)
    return ax,

# Configuración inicial
vertices = generar_teseracto()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear la animación
ani = FuncAnimation(fig, actualizar, frames=range(360), interval=50, blit=True)

plt.show()