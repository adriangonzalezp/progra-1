#-----------------------------------------#
# Ejercicio 1
# Maquina de voltaje 
#-----------------------------------------#

# Problema

maquinaPrendida = True
voltaje = 0
while(maquinaPrendida):
    if voltaje < 100:
        voltaje = voltaje + 1
    else:
        maquinaPrendida = False
    # Inserte algun bloque de codigo que haga que la maquina se apague cuando el voltaje supere los 100 voltios

# # Resultado deberia ser 100
print(voltaje)
