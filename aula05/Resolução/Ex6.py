def abreviar(frase):
    abreviacao = ""
    for letra in frase:
        a  = letra.isupper()
        if a == True:
            abreviacao += letra
        else:
            continue
    return abreviacao




def main():
    frase=str(input("Insira uma frase: "))
    print(abreviar(frase))

main()

