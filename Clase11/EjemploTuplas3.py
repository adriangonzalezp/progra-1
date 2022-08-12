# Dadas las siguientes tuplas
tupla1 = (11,22,33,5)
tupla2 = (23,48,13,89)
tupla3 = (40,32,12,9)

# Hagamos un programa que haga otra tupla que contiene las sumas de las columnas.
#       = (74,102,58,103)

tuplaResultado = (tupla1[0] + tupla2[0] + tupla3[0],
                  tupla1[1] + tupla2[1] + tupla3[1],
                  tupla1[2] + tupla2[2] + tupla3[2],
                  tupla1[3] + tupla2[3] + tupla3[3])

print("Resultado: ", tuplaResultado)