word = input("please enter a string ")

for ch in word:
    if ch == " ":
        print("/", end=" ")
    if ch == "a":
        print(".-", end = " ")
    if ch == "b":
        print("-...", end = " ")
    if ch == "c":
        print("-.-.", end = " ")
    if ch == "d":
        print("-..", end = " ")
    if ch == "e":
        print(".", end = " ")
    if ch == "f":
        print("..-.", end = " ")
    if ch == "g":
        print("--.", end = " ")
    if ch == "h":
        print("....", end = " ")
    if ch == "i":
        print("..", end = " ")
    if ch == "j":
        print(".---", end = " ")
    if ch == "k":
        print("-.-", end = " ")
    if ch == "l":
        print(".-..", end = " ")
    if ch == "m":
        print("--", end = " ")
    if ch == "n":
        print("-.", end = " ")
    if ch == "o":
        print("---", end = " ")
    if ch == "p":
        print("-..-", end = " ")
    if ch == "q":
        print("--.-", end = " ")
    if ch == "r":
        print(".-.", end = " ")
    if ch == "s":
        print("...", end = " ")
    if ch == "t":
        print("-", end = " ")
    if ch == "u":
        print("..-", end = " ")
    if ch == "v":
        print("...-", end = " ")
    if ch == "w":
        print(".--", end = " ")
    if ch == "x":
        print("-..-", end = " ")
    if ch == "y":
        print("-.--", end = " ")
    if ch == "z":
        print("--..", end = " ")
    if ch == "1":
        print(".----", end = " ")
    if ch == "2":
        print("..---", end = " ")
    if ch == "3":
        print("...--", end = " ")
    if ch == "4":
        print("....-", end = " ")
    if ch == "5":
        print(".....", end = " ")
    if ch == "6":
        print("-....", end = " ")
    if ch == "7":
        print("--...", end = " ")
    if ch == "8":
        print("---..", end = " ")
    if ch == "9":
        print("----.", end = " ") 
    if ch == "0":
        print("-----", end = " ")
print("\n")

code = input("please enter your moss code here")
temp = ""
sentance = ""

for char in code:
    if char == "." or "-":
        temp += char
    else:
        print("be better")
    print(temp)
      