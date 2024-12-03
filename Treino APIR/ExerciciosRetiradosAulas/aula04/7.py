def sentinelTotal():
    op = input("Valor: ")
    soma=0
    count=0

    while op!="":

        soma+=float(op)
        count+=1
        op = (input("Valor: "))

    media = soma/count
    return media


sentinelTotal()


