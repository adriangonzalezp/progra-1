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
    discriminante = calcularDiscriminante(lista)
    print(discriminante)
    soluciones = calcularSoluciones(discriminante,lista)
    print(soluciones)

def calcularDiscriminante(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]
    return (b * b) - (4 * a * c)

def calcularSoluciones(discriminante, lista):
    soluciones = list()
    if discriminante < 0:
        return soluciones
    else:
        a = lista[0]
        b = lista[1]
        c = lista[2]
        if discriminante == 0:
            soluciones.append(None)
            return soluciones
        else:
            soluciones.append(None)
            soluciones.append(None)
            return soluciones


main()