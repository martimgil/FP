def insertTeam():
    equipas = []
    while True:
        nome = str(input("Insira o nome da equipa: "))
        if nome == "":
            break
        else:
            equipas.append(nome)
    return equipas
def gerarJogos(equipas):
    jogos = []
    for casa in equipas:
        for fora in equipas:
            if casa != fora:
                jogos.append((casa, fora))
    return jogos

def resultadoJogo(jogos):
    resultado = dict()
    for casa, fora in jogos:
        casa_Res = int(input("Insira resultado da equipa da casa: "))
        fora_Res = int(input("Insira resultado da equipa de fora: "))
        resultado[casa, fora] = (casa_Res, fora_Res)
    return resultado

def table(equipas, resultados):
    tabela = {}
    for equipa in equipas:
        tabela[equipa] = [0,0,0,0,0,0]

    for partida in resultados:
        casa = partida[0]
        fora = partida[1]
        casa_Res = resultados[partida][0]
        fora_Res = resultados[partida][1]

        if casa_Res>fora_Res:
            tabela[casa][0] +=1
            tabela[casa][5] += 3
            tabela[casa][2] +=1

        elif fora_Res>casa_Res:
            tabela[fora][0] +=1
            tabela[fora][5] += 3
            tabela[fora][2] +=1
        else:
            tabela[casa][5] +=1
            tabela[fora][5] += 1
            tabela[casa][1] +=1
            tabela[fora][1] +=1


        tabela[casa][3] += casa_Res  # golos marcados
        tabela[fora][3] += fora_Res  # golos marcados
        tabela[casa][4] += fora_Res  # golos sofridos
        tabela[fora][4] += casa_Res  # golos sofridos

    return tabela

def printTable(tabela):
    print("{:^10s}{:^10s}{:^10s}{:^10s}{:^20s}{:^20s}{:^10s}" .format("Equipas","Vitórias", "Empates", "Derrotas", "Golos Marcados", "Golos Sofridos", "Pontos"))
    equipas = tabela.keys()
    equipas= sorted(equipas,key = lambda equipa:(tabela[equipa][5], tabela[equipa][3] - tabela[equipa][4]), reverse=True)
    for equipa in equipas:
        print("{:^10s}{:^10d}{:^10d}{:^10d}{:^20d}{:^20d}{:^10d}" .format(equipa,tabela[equipa][0], tabela[equipa][1],tabela[equipa][2],tabela[equipa][3],tabela[equipa][4],tabela[equipa][5]))

def theChampion(tabela):
    equipas = tabela.keys()
    equipas= sorted(equipas,key = lambda equipa:(tabela[equipa][5], tabela[equipa][3] - tabela[equipa][4]), reverse=True)
    winner = equipas[0]

    return winner


def main():
    equipas = insertTeam()
    jogos = gerarJogos(equipas)
    resultados = resultadoJogo(jogos)
    tabela = table(equipas, resultados)
    printTable(tabela)
    print(theChampion(tabela))
main()