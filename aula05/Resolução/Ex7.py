def ispalindrome(s):
    frase=""
    for letra in s[::-1]:
        frase += letra
    if frase == s:
        resultado = True
    else:
        resultado = False
    return resultado
def main():
    s = str(input("Insira uma palavra: "))
    ispalindrome(s)
main()