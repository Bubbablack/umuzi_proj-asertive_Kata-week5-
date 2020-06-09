from dictionary import dic

def lettersToMorseCode(word):
    final = ""
    for ch in word:
        for key in dic:
            if ch == key:
                final += dic[key]
                final += " "
    final.rstrip()  
    assert len(word) == len(final.split())
    assert word.count(" ") == final.count("/")
    return(final)  