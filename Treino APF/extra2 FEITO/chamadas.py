def validarNumero(numero):
    if (len(numero)<3 and numero[0]!="+") or (len(numero)<4 and numero[0]=="+"):
        return False
    if numero[0]=="+" or numero[0].isdigit():
        for number in numero[1:]:
            if number.isdigit()==False:
                return False
    else:
        return False
        
    return True
    
 
def novaChamada(registo):
    while True:
        origem = input("Telefone origem? ")
        if validarNumero(origem)==True:
            break
    
    while True:
        destino = input("Telefone destino?")
        if validarNumero(destino)==True:
            break
    
    tempo = int(input("Duração (s)?"))
    
    registo.append([origem, destino, tempo])
    return registo
    
    
def lerFicheiro(registo):
    
    ficheiro = str(input("Ficheiro? "))
    
    with open(ficheiro, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split("\t")
            print(line)
            registo.append(line)
            
    return registo
    
            
def listarClientes(registo):
    clientes = []
    s = "Clientes: "
    for chamada in registo:
        if chamada[0] not in clientes:
            clientes.append(chamada[0])
    for cliente in clientes:
        s+=(" {}".format(cliente))

    print(s)

        
        
def fatura(registo):
    numero = input("Cliente? ")
    print("Fatura do cliente {}".format(numero))
    print("{:<12s}{:>12s}{:>10s}" .format("Destino", "Duração", "Custo"))
    
    for chamada in registo:
        origem = chamada[0]
        destino = chamada[1]
        tempo = chamada[2]
        
        if origem == numero: 
            if destino[0] == "2":
                custo = int(tempo)*(0.02/60)
            elif destino[0] == "+":
                custo = int(tempo)*(0.8/60)
            elif origem[:2]==destino[:2]:
                custo = int(tempo)*(0.04/60)
            else:
                custo = int(tempo)*(0.1/60)
            print("{:<12s}{:>12s}{:>10.2f}" .format(destino, tempo, custo))


def main():
    registo = []
    while True:
        print("1) Registar chamada")
        print("2) Ler ficheiro")
        print("3) Listar clientes")
        print("4) Fatura")
        print("5) Terminar")
        opcao = int(input("Opção? "))
        
        if opcao == 1:
            registo = novaChamada(registo)
        elif opcao == 2:
            registo = lerFicheiro(registo)
        elif opcao == 3:
            listarClientes(registo)
        elif opcao == 4:
            fatura(registo)
        elif opcao == 5:
            break
            
            
main()