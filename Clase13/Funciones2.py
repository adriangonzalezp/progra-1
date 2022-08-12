def main():
    listaCoeficientes = leerCoeficientes()
    encontrarSoluciones(listaCoeficientes)

def leerCoeficientes():
    lista = []
    lista.append(int(input("Escriba el coeficiente A: ")))
    lista.append(int(input("Escriba el coeficiente B: ")))
    lista.append(int(input("Escriba el coeficiente C: ")))
    return lista

def encontrarSoluciones(lista):
    print(lista)


main()