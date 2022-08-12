# Mostrar el menu.
print("------------------------------")
print("Desea diagnosticar al paciente?")
print("1 = Si")
print("2 = No (Salir) ")

# Leer la eleccion del usuario.
opcion = int(input("Digite la opcion deseada: "))
print("------------------------------")

# Mientras opcion sea 1, se corre el codigo de pronostico.
while opcion == 1:

    # Leer el peso y la altura del paciente.
    peso = float(input("Digite el peso(en kg) del paciente: "))
    altura = float(input("Digite la altura(en metros) del paciente: "))
    

    # Calcular el IMC segun los datos ingresados.
    imc = (peso) / (altura ** 2)

    # Cadena de condicionales para diagnosticar al paciente segun el IMC.
    if imc < 16:
        print("El paciente padece de desnutricion grado 3")
    elif 16 < imc <= 17:
        print("El paciente padece de desnutricion grado 2")
    elif 17 < imc <= 18.5:
        print("El paciente padece de desnutricion grado 1")
    elif 18.5 < imc <= 25:
        print("El paciente presenta un indice de masa corporal normal.")
    elif 25 < imc <= 30:
        print("El paciente padece de sobre peso grado 1")
    elif 30 < imc <= 40:
        print("El paciente padece de sobre peso grado 2")
    else:
        print("El paciente padece de sobre peso grado 3.")

    # Volver a mostrar el menu.
    print("------------------------------")
    print("Desea diagnosticar otro paciente?")
    print("1 = Si")
    print("2 = No (Salir) ")
    opcion = int(input("Digite la opcion deseada: "))

# Fin del programa.    
print("------------------------------")
print("Gracias por usar el programa.")