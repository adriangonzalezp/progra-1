input = input("Digite su lista de pares ordenados separados por un punto y coma: ")

# Convertir el string en una lista.
input = input.replace(";",",")
listString  = input.split(",")

listNumbers = []
for i in listString:
    listNumbers.append(int(i))

# Separar la lista en dominio y ambito.
listX = []
listY = []
contador = 0
while contador < len(listNumbers):
  if contador % 2 == 0:
    listX.append(int(listNumbers[contador]))
  else:
    listY.append(int(listNumbers[contador]))
  contador = contador+1

n = len(listX)

# Sumatorias de X, Y, y XY
sumX = 0
sumY = 0 

for i in listX:
    sumX = sumX + i
for i in listY:
    sumY = sumY + i
sumXY = sumX * sumY

# Medias de X y Y
mX = sumX / n
mY = sumY / n

# Valores de la ecuacion mayor
oXY = (sumXY / n) - (mX * mY)
oX = (((sumX ** 2) / n) - (mX ** 2)) ** 0.5
oY = (((sumY ** 2) / n) - (mY ** 2)) ** 0.5

# Operacion final
r = (oXY) / (oX * oY)
print(r)

# Explicar el resultado.
if r == 1:
    print("r = ",r,", existe una correlación positiva perfecta. Cuando una variable aumenta, la otra también lo hace en proporción constante.")
elif r == -1:
    print("R = ",r,", existe una correlación negativa perfecta (relación opuesta). Cuando una de ellas aumenta, la otra cambia su signo en proporción constante.")
elif r == 0:
    print("R = ",r,", no existe relación lineal, no necesariamente implica que las variables son independientes")
elif 0 < r < 1:
    print("R = ",r,", existe una correlación positiva.")
elif -1 < r < 0:
    print("R = ",r,", existe una correlación negativa.")