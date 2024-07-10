def generar_teseracto():
    vertices = []
    for i in range(16):
        vertex = []
        for j in range(4):
            vertex.append((i >> j) & 1)
        vertices.append(vertex)
    return vertices

def encontrar_celdas(vertices):
    celdas = []
    for i in range(4):  # para cada coordenada
        for val in [0, 1]:  # fijar coordenada a 0 o 1
            celda = []
            for vertice in vertices:
                if vertice[i] == val:
                    celda.append(vertice)
            celdas.append(celda)
    return celdas

vertices = generar_teseracto()
celdas = encontrar_celdas(vertices)

for i, celda in enumerate(celdas):
    print(f"Celda {i + 1}: {celda}")