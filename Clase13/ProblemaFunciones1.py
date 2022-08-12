def main():
    listaNumeros = leerLista()
    promedio = encuentraPromedio(listaNumeros)
    numeroMayor = encuentraMayor(listaNumeros)
    numeroMenor = encuentraMenor(listaNumeros)
    mediana = encuentraMediana(listaNumeros)
    mostrarResultados(listaNumeros,promedio,numeroMayor,numeroMenor,mediana)

def leerLista():
    lista = input("Escriba la lista de numeros separasdos por coma: ")
    resultado = list(map(int,lista.split(",")))
    return resultado

def encuentraPromedio(listaNumeros):
    acum = 0
    for i in listaNumeros:
        acum = acum + i
    return (acum / len(listaNumeros))

def encuentraMayor(listaNumeros):
    return max(listaNumeros)

def encuentraMenor(listaNumeros):
    return min(listaNumeros)

def encuentraMediana(listaNumeros):
    listaNumeros.sort()
    listaNumerosLen = len(listaNumeros)
    index = int((listaNumerosLen - 1) / 2)
    if listaNumerosLen % 2 == 0:
        i1 = listaNumeros[index + 1]
        i2 = listaNumeros[index]
        return (i1 + i2) / 2
    else:   
        return listaNumeros[index]

def mostrarResultados(listaNumeros,promedio,numeroMayor,numeroMenor,mediana):
    listaNumeros.sort()
    print(f"Lista ordenada: {listaNumeros} ")
    print(f"El promedio es: {promedio}")
    print(f"El mayor es: {numeroMayor}")
    print(f"El menor es: {numeroMenor}")
    print(f"La mediana es: {mediana}")

main()