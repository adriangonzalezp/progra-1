#Complete los espacios en blanco dentro de la función smallest_num_list
# para que la función devuelva el número más pequeño que se encuentra en la lista. 

def smallest_num_list( list ):
    min = 0
    for num in list:
        if num < min:
            min = num
    return min
print(smallest_num_list([5, 8, -8, 0]))
