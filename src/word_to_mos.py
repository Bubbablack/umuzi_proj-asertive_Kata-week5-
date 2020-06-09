word = input("please enter a string ")
count= 0
num_ch = len(word)

for ch in word:
    if ch == " ":
        count += 1
        print("/", end=" ")
    elif ch == "a":
        count += 1
        print(".-", end = " ")
        count += 1
    elif ch == "b":
        print("-...", end = " ")
        count +=1
    elif ch == "c":
        print("-.-.", end = " ")
        count += 1
    elif ch == "d":
        print("-..", end = " ")
        count += 1
    elif ch == "e":
        print(".", end = " ")
        count += 1
    elif ch == "f":
        print("..-.", end = " ")
        count += 1
    elif ch == "g":
        print("--.", end = " ")
        count += 1
    elif ch == "h":
        print("....", end = " ")
        count += 1
    elif ch == "i":
        print("..", end = " ")
        count += 1
    elif ch == "j":
        print(".---", end = " ")
        count += 1
    elif ch == "k":
        print("-.-", end = " ")
        count += 1
    elif ch == "l":
        print(".-..", end = " ")
        count += 1
    elif ch == "m":
        print("--", end = " ")
        count += 1
    elif ch == "n":
        print("-.", end = " ")
        count += 1
    elif ch == "o":
        print("---", end = " ")
        count += 1
    elif ch == "p":
        print("-..-", end = " ")
        count += 1
    elif ch == "q":
        print("--.-", end = " ")
        count += 1
    elif ch == "r":
        print(".-.", end = " ")
        count += 1
    elif ch == "s":
        print("...", end = " ")
        count += 1
    elif ch == "t":
        print("-", end = " ")
        count += 1
    elif ch == "u":
        print("..-", end = " ")
        count += 1
    elif ch == "v":
        print("...-", end = " ")
        count += 1
    elif ch == "w":
        print(".--", end = " ")
        count += 1
    elif ch == "x":
        print("-..-", end = " ")
        count += 1
    elif ch == "y":
        print("-.--", end = " ")
        count += 1
    elif ch == "z":
        print("--..", end = " ")
        count += 1
    elif ch == "1":
        print(".----", end = " ")
        count += 1
    elif ch == "2":
        print("..---", end = " ")
        count += 1
    elif ch == "3":
        print("...--", end = " ")
        count += 1
    elif ch == "4":
        print("....-", end = " ")
        count += 1
    elif ch == "5":
        print(".....", end = " ")
        count += 1
    elif ch == "6":
        print("-....", end = " ")
        count += 1
    elif ch == "7":
        print("--...", end = " ")
        count += 1
    elif ch == "8":
        print("---..", end = " ")
        count += 1
    elif ch == "9":
        print("----.", end = " ")
        count += 1 
    elif ch == "0":
        print("-----", end = " ")
        count += 1
print("\n")

assert count == num_ch
