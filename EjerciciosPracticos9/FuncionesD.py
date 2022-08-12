def main():
    num = readNum()
    while num != -231:
        unit = readUnit()
        convTemp = convertTemp(num,unit)
        num = readNum()

def readNum():
    n = int(input("Digite la temperatura: ")) 
    return n

def readUnit():
    entry = input("Que unidad de medida es? (Celsius o Farenheit): ")
    u = entry.lower()
    return u

def convertTemp(num,unit):
    if unit == "celsius":
        print(f"{num} C° son {convertCelsius(num)} F°")
    elif unit == "farenheit":
        print(f"{num} F° son {convertFarenheit(num)} C°")

def convertCelsius(num):
    f = (num * 1.8) + 32
    return f

def convertFarenheit(num):
    c = (num / 1.8) - 32
    return c

main()