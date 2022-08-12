numero = int(input("Digite el numero que desea calcular Fibonacci: "))

if numero == 1 or numero == 2:
    print("El fibonacci de", numero, "es", 1)
else:
    n_2 = 1
    n_1 = 1
    actual = 3
    fibo = 0
    while actual <= numero: 
        fibo = n_2 + n_1
        n_1 = n_2
        n_2 = fibo
        actual = actual + 1
    print("El fibonacci de", numero, "es", fibo)

print(range(0,9))
