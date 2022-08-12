def main():
    word = readWord()
    letter = readLetter()
    isIncluded = verifyLetter(word, letter)
    printResult(word,letter,isIncluded)

def readWord():
    word = input("Digite una palabra: ")
    word = word.lower()
    return word

def readLetter():
    letter = input("Digite la letra que desea verificar: ")
    letter = letter.lower()
    return letter

def verifyLetter(word,letter):
    isIncluded = False
    charList = []
    for l in word:
        charList.append(l)
    for element in charList:
        if element == letter:
            isIncluded = True
            break
    return isIncluded

def printResult(word,letter,isIncluded):
    print(f"La letra {letter} esta en la palabra '{word}'?: {isIncluded}")

main()