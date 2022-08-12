#para recorrer listas en python, lo mejor es usar el FOR
lista = [20, 31, 11, 123, 345, 987, 45, 80, 42, 34, 67, 98]
for unNumero in lista:
    if unNumero % 2 == 0:
        print("El numero", unNumero, "es par")
    else: 
        print("El numero", unNumero, "es impar")