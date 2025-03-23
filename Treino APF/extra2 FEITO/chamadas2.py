def validarNum(n):
    if n[0]=="+":
        if len(n)>4:
            for i in n[1:]:
                if i.isdigit()==False:
                    return False
        else:
            return False
    else:
        if len(n)>3:
            for i in n:
                if i.isdigit()==False:
                    return False
        else:
            return False
    return True

def newCall(reg):

    while True:
        origem = str(input("Telefone origem? "))
        if validarNum(origem):
            break

    while True:
        destino = str(input("Telefone destino? "))
        if validarNum(destino):
            break

    duracao = int(input("Duração (s)? "))

    reg.append((origem,destino, duracao))

    return reg


def loadFile(reg):
    fname = input("Ficheiro? ")

    with open(fname,"r", encoding="utf-8") as f:
        for line in f:
            line= line.strip().split("\t")
            reg.append((line[0], line[1], line[2]))

    return reg

def listClients(reg):
    s = "Clientes: "
    lst=[]
    for chamada in reg:
        if chamada[0] not in lst:
            lst.append(chamada[0])

    for numero in lst:
        s+="{} ".format(numero)
    print(s)
def fatura(reg):
    numero  = str(input("Cliente? "))
    print("Fatura do cliente {}".format(numero))
    total = 0
    for chamada in reg:
        if chamada[0]==numero:
            if chamada[1][0] == "2":
                custo = int(chamada[2])*(0.02/60)
                total+=custo
            elif chamada[1][0]=="+":
                custo = int(chamada[2])*(0.8/60)
                total+=custo
            elif chamada[1][:2] == numero[:2]:
                custo = int(chamada[2])*(0.04/60)
                total+=custo
            else:
                custo=int(chamada[2])*(0.1/60)
                total+=custo

            print("{:<20s} {:>10s} {:>10.2f} ".format(chamada[1], chamada[2], custo))
            print("{:<20s} {:>10s} {:>10.2f} ".format("", "Total:", total))


def main():
    reg=[]
    while True:
        print("1) Registar chamada")
        print("2) Ler ficheiro")
        print("3) Listar clientes")
        print("4) Fatura")
        print("5) Terminar")

        op = int(input("Opção? "))

        if op==1:
            newCall(reg)
        elif op==2:
            loadFile(reg)
        elif op==3:
            listClients(reg)
        elif op==4:
            fatura(reg)
        elif op==4:
            break
        else:
            print("Opção não existe!")





main()