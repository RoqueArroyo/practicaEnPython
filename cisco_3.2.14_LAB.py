blocks = int(input("Ingresa el número de bloques: "))
i = 0
height = 0

while blocks - i > 0:
    height = height + 1
    i = i + 1
    blocks = blocks - i

print("La altura de la pirámide:", height)