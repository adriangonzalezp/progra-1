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
    
def calcularDiscriminante(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]
    return (b * b) - (4 * a * c)


main()