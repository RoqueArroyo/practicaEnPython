my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = []

for i in range(0, len(my_list)):
    if my_list[i] not in my_list[:i]:
        new_list.append(my_list[i])

print("La lista con elementos únicos:")
print(new_list)