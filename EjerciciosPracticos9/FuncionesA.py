def main():
    coefficients = readcoefficients()
    findSolutions(coefficients)
def readcoefficients():
    coefficients = []
    coefficients.append(int(input("Escriba el coeficiente A: ")))
    coefficients.append(int(input("Escriba el coeficiente B: ")))
    coefficients.append(int(input("Escriba el coeficiente C: ")))
    return coefficients

def findSolutions(coefficients):
    discriminant = calcDiscrimininant(coefficients)
    solutions = calcSolutions(discriminant,coefficients)
    print(solutions)

def calcDiscrimininant(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    return(b**2) - (4 * a * c)

def calcSolutions(discriminant,coefficients):
    solutions = list()
    if discriminant < 0:
        return solutions
    else:
        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        if discriminant == 0:
            solutions.append((b**2)/(2*a))
        else:
            solutions.append(findSolution(discriminant,a,b,True))
            solutions.append(findSolution(discriminant,a,b,False))
            return solutions

def findSolution(discriminant,a,b,isNegative):
    if isNegative:
        return ((b**2) - discriminant) / (2*a)
    else:
        return ((b**2) + discriminant) / (2*a)

main()