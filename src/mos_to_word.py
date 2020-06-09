
code = input("please enter your moss code here")


def decode(sentance):
    scode = ""
    if sentance == "/":
        scode += " "
    elif sentance == ".-":
        scode += "a"
    elif sentance == "-...":
        scode += "b"
    elif sentance == "-.-.":
        scode += "c"
    elif sentance == "-..":
        scode += "d"
    elif sentance == ".":
        scode += "e"
    elif sentance == "..-.":
        scode += "f"
    elif sentance == "--.":
        scode += "g"
    elif sentance == "....":
        scode += "h"
    elif sentance == "..":
        scode += "i"
    elif sentance == ".---":
        scode += "j"
    elif sentance == "-.-":
        scode += "k"
    elif sentance == ".-..":
        scode += "l"
    elif sentance == "--":
        scode += "m"
    elif sentance == "-.":
        scode += "n"
    elif sentance == "---":
        scode += "o"
    elif sentance == ".--.":
        scode += "p"
    elif sentance == "--.-":
        scode += "q"
    elif sentance == ".-.":
        scode += "r"
    elif sentance == "...":
        scode += "s"
    elif sentance == "-":
        scode += "t"
    elif sentance == "..-":
        scode += "u"
    elif sentance == "...-":
        scode += "v"
    elif sentance == ".--":
        scode += "w"
    elif sentance == "-..-":
        scode += "x"
    elif sentance == "-.--":
        scode += "y"
    elif sentance == "--..":
        scode += "z"
    elif sentance == "-----":
        scode += "0"
    elif sentance == ".----":
        scode += "1"
    elif sentance == "..---":
        scode += "2"
    elif sentance == "...--":
        scode += "3"
    elif sentance == "....-":
        scode += "4"
    elif sentance == ".....":
        scode += "5"
    elif sentance == "-....":
        scode += "6"
    elif sentance == "--...":
        scode += "7"
    elif sentance == "---..":
        scode += "8"
    elif sentance == "----.":
        scode += "9"
        
    return(scode)


temp = ""
full = ""
count = 0
for ch in code:
    if ch == ".":
        temp += "."
    elif ch == "-":
        temp += "-"
    elif ch == "/":
        count +=1
        temp += "/"
    elif ch == " ":
        count +=1
        full += decode(temp)
        temp = ""
    else:
        print("error")
full += decode(temp)
print(full)
numb = len(full)
assert numb == count