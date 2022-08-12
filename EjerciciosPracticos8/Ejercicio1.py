input = int(input("Digite un numero: ")) 

dictionary = {}
for i in range(0,input+1):
    result = i * i
    dictionary[i] = result

print(dictionary)