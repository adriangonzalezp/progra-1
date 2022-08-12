def main():
    word = readWord()
    vocals = vocalCount(word)
    printResult(word,vocals)

def readWord():
    word = input("Digite una palabra: ")
    return word

def vocalCount(word):
    charList = []
    for letter in word:
        charList.append(letter)
    vocals = 0
    for l in charList:
        if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
            vocals = vocals + 1
    return vocals

def printResult(word, vocals):
    print(f"La palabra {word} tiene {vocals} vocales.")

main()