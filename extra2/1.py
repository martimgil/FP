def validateNumber(number):
    if len(number)<3:
        return False
    if number[0]=="+":
        number=number[1:]
    return number.isdigit()
def newCall():
    while True:
        origem = str(input("Telefone origem?"))
        if validateNumber(origem):
            break
    while True:
        destino = str(input("Telefone destino?"))
        if validateNumber(destino):
            break
    duracao = int(input("Duração?"))
    return origem, destino, duracao
def readFile(ficheiro,lst):
    with open(ficheiro, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip().split("\t")
            lst.append(s)
    return lst
def listClients(numbers):
    lst=[]
    s=""
    for a in numbers:
        if a[0] not in lst:
            lst.append(a[0])
    lst.sort()
    s+="Clientes: "
    for i in lst:
        s+="{} ".format(i)
    print(s)
    return s
def fatura(lst):
    number= str(input("Cliente?"))
    print("Fatura do cliente {}".format(number))
    print("{:<15s}{:<10s}{:>10s}".format("Destino", "Duração", "Custo"))

    calls=[]
    total=0
    for a in lst:
        if a[0]==number:
            if a[1][0] == "2":
                valor = (0.02/60)*int(a[2])
                total += valor
            elif a[1][0] == "+":
                valor = (0.8/60)*int(a[2])
                total += valor
            elif a[0][0:2] == a[1][0:2]:
                valor=(0.04/60)*int(a[2])
                total += valor
            else:
                valor=(0.10/60)*int(a[2])
                total += valor
            print("{:<15s}{:<10s}{:>10.2f}".format(a[1], a[2], valor))
    print("{:<15s}{:<10s}{:>10.2f}".format(" ", "Total", total))
def main():
    lst=[]
    while True:

        print("1) Registar chamada")
        print("2) Ler ficheiro")
        print("3) Listar clientes")
        print("4) Fatura")
        print("5) Terminar")

        opcao = int(input("Opção? "))

        if opcao==1:
            origem, destino, duracao = newCall()
            lst.append([origem, destino, duracao])
        elif opcao==2:
            ficheiro = str(input("Ficheiro? "))
            lst = readFile(ficheiro, lst)

        elif opcao==3:
            listClients(lst)
        elif opcao==4:
            fatura(lst)
        elif opcao==5:
            break
main()