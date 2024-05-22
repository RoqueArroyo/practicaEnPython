# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if (letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U"):
       continue
    else:
        print(letter)