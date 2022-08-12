input1 = input("Digite un set separado por comas: ")
input2 = input("Digite otro set separado por comas: ")

set1 = set(map(int,input1.split(",")))
set2 = set(map(int,input2.split(",")))
setResult = set()

intercept = None
for element in set1:
    intercept = False

    for element2 in set2:
        if element == element2:
            intercept = True

    if intercept == False:
        setResult.add(element)

print(setResult)