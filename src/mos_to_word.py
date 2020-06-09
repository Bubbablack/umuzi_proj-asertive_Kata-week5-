from dictionary import dic

def decode(temp):
    final = ""
    for key in dic:
        if temp == dic[key]:
            final += key
    return(final)  

def morseCodeToLetters(code):
    temp = ""
    full = ""
    for ch in code:
        if ch == ".":
            temp += "."
        elif ch == "-":
            temp += "-"
        elif ch == "/":
            temp += "/"
        elif ch == " ":
            full += decode(temp)
            temp = ""
    full += decode(temp)
    assert len(code.split()) == len(full)
    assert code.count('/') == full.count(" ")
    return(full)