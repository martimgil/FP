def upper(str):
    abreviacao=""
    for l in str:
        if l.isupper() == True:
            abreviacao += l

    return abreviacao
print(upper("Universidade de Aveiro"))

def ispalindrome(s):
    a1 = s
    a2 =""
    for i in s[::-1]:
        a2 += i
    if a1 == a2:
        return True

    else:
        return False
print(ispalindrome("Olá"))