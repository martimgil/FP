def loadFile(info):
    fname = str(input("Nome do ficheiro? "))
    with open(fname,"r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(";")
            info.append((line[0], line[1], line[2]))
    print("Foram importados {} registos." .format(len(info)))
    return info

def printMatriculas(info):
    info = sorted(info, key=lambda a:(a[2], a[0]))
    for car in info:
        print("{}:{}".format(car[2], car[0:2]))

def printCliente(info):
    if len(info)>0:
        registo = {}
        for car in info:
            if car[2] not in registo:
                registo[car[2]] = list()
            registo[car[2]].append(car[0])

        for nif in registo:
            veiculos = registo[nif]
            print("{} : {}".format(nif,veiculos))
    else:
        print("Não existem clientes!")

def validar(matricula):
    matricula = matricula.strip().split("-")
    if len(matricula)<3 or (len(matricula[0])!=2 or len(matricula[1])!=2 or len(matricula[2])!=2):
        return False
    else:
        for digit in matricula[0]:
            if digit.isdigit()==False:
               return False
        for digit in matricula[1]:
            if digit.isalpha()==False:
                return False
        for digit in matricula[2]:
            if digit.isdigit()==False:
                return False

        return True

def adicionar(parques):
    while True:
        matricula = input("Matricula? ")
        if validar(matricula)==True:
            break
        print("Invalida!")
    while True:
        tempo = input("Duracao? ")
        if tempo.isdigit() and int(tempo)>0:
            tempo = int(tempo)
            break
        print("Invalida!")
    parques.append([matricula, tempo])

    return parques

def registar(parques):
    if len(parques)>0:
        with open("parque.csv", "w", encoding="utf-8") as f:
            parques = sorted(parques, key = lambda a:a[1], reverse=True)
            for estacionamento in parques:
                f.write('{};{}\n'.format(estacionamento[0], estacionamento[1]))
        print("Ficheiro gravado com sucesso!")
    else:
        print("Não existem entradas no Parque!")

def fatura(info, parques):
    nif = input("NIF? ").strip()
    if not nif.isdigit():
        print("NIF inválido!")
        return
    print("Fatura NIF: ", nif)
    carros = {}
    custo = 0
    for a in info:
        if a[2] == nif:
            carros[a[0]] = a[1]
    print("{:<10s} {:>7s} {:>20s} {:>5s}".format("Matricula", "Marca", "Duracao", "Custo"))
    for matricula, tempo in parques:
        if matricula in carros:
            custo += tempo * 0.01
            print("{:<10s} {:>7s} {:>20s} {:>5.2f}".format(matricula, carros[matricula], str(tempo), tempo * 0.01))

def main():
    info = []
    parques = []
    while True:
        print("Opcoes disponiveis:\n0 - Terminar\n1 - Ler ficheiro de clientes\n2 - Imprimir clientes ordenados\n3 - Mostrar matriculas por Cliente\n4 - Adicionar acesso ao parque\n5 - Grava acessos ao parque\n6 - Gerar fatura para um cliente")
        op = int(input("Opcao? "))
        if op==0:
            print("Obrigado por usar software desenvolvido em FP!")
            break
        elif op==1:
            loadFile(info)
        elif op==2:
            printMatriculas(info)
        elif op==3:
            printCliente(info)
        elif op==4:
            adicionar(parques)
        elif op==5:
            registar(parques)
        elif op==6:
            fatura(info,parques)

main()