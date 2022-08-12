cambio = int(input("Digite el tipo de cambio: "))
colones = int(input("Digite el monto en colones que quiere ingresar: "))

while colones != 0:
    dolares = colones / cambio
    print("Por ", colones, " colones recibe ", dolares, "$")
    colones = int(input("Digite el monto en colones que quiere ingresar: "))


print("Gracias por utilizar el servicio de cambio.")