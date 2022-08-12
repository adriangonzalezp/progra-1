nota = float(input("Digite la nota final: "))

if nota >= 95:
    print("Su GPA es A+")
elif 95 > nota and nota >= 92.5:
    print("Su GPA es A")
elif 92.5 > nota and nota >= 89:
    print("Su GPA es A-")
elif 89 > nota and nota >= 84:
    print("Su GPA es B+")
elif 84 > nota and nota >= 79:
    print("Su GPA es B")
elif 79 > nota and nota >= 74.5:
    print("Su GPA es B-")
elif 74.5 > nota and nota >= 70:
    print("Su GPA es C")
else:
    print("Su GPA es D")