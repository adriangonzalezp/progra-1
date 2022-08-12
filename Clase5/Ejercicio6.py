libros = int(input("Digite la cantidad de libros comprados: "))
total = libros * 20

if libros <= 10:
    print("No se le aplica descuento, debe pagar: ", total, "$.")
elif 10 < libros <= 20:
    descuento = total * 0.1
elif 20 < libros <= 30:
    descuento = total * 0.2
else:
    descuento = total * 0.4

total = total - descuento
print("Por la compra de", libros, "libros se le aplica", descuento, "$ de descuento. Debe pagar: ", total, "$.")