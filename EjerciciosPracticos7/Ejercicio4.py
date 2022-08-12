userInput = input("Ingrese una serie de numeros separados por coma: ")

tuple = tuple(map(int,userInput.split(",")))

for element1 in tuple:
    for element2 in tuple:
        if element1 == element2:
            equal = True
        else:
            equal = False
            break

if equal == True:
    print("Son iguales.")
else:
    print("Son diferentes.")