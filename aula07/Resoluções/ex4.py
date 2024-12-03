teams = []
AllMatches = []
resultados = {}
tabela={}

def allMatches(teams):
    assert len(teams) >= 2, "Requires two or more teams!"
    for casa in teams:
        for fora in teams:
            if casa == fora:
                continue
            else:
                AllMatches.append((casa, fora))
    return AllMatches

def results():
    for matches in AllMatches:
        home = str(input("Resultado casa: "))
        away = str(input("Resultado fora: "))
        resultados[matches] = (home, away)
    return resultados

def table():
    for a in teams:
        tabela[a]=[0,0,0,0,0,0]


    for match in resultados:
        if resultados[match][0]> resultados[match][1]:
            tabela[match[0]][0]+=1
            tabela[match[1]][1] += 1
            tabela[match[0]][5] +=3


        elif resultados[match][1]> resultados[match][0]:
            tabela[match[1]][0] += 1
            tabela[match[0]][1] += 1
            tabela[match[1]][5] +=3
        else:
            tabela[match[1]][2]+= 1
            tabela[match[0]][2] += 1
            tabela[match[0]][5] +=1
            tabela[match[1]][5] +=1

        tabela[match[0]][3]+= float(resultados[match][0])
        tabela[match[1]][3] += float(resultados[match][1])
        tabela[match[0]][4] += float(resultados[match][1])
        tabela[match[1]][4] += float(resultados[match][0])

def showTable():
    print("{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}{:>8s}".format("Team","Wins","Loses", "Draw", "Scored", "Suffs", "Points"))
    for a in tabela:
       print("{:>8s}{:>8d}{:>8d}{:>8d}{:>8.2f}{:>8.2f}{:>8d}".format(a, tabela[a][0], tabela[a][1], tabela[a][2], tabela[a][3], tabela[a][4], tabela[a][5]))



def theChampions():
    winner = teams[0]
    for a in range(1, len(teams)):
        if tabela[teams[a]][5] > tabela[winner][5]:
            winner = teams[a]
        elif tabela[teams[a]][5] == tabela[winner][5]:
            d1 = int(tabela[teams[a]][3]) - int(tabela[teams[a]][4])
            d2 = int(tabela[winner][3]) - int(tabela[winner][4])
            if d1>d2:
                winner=teams[a]
    return winner





def main():

    while True:
        team = str(input("Insira nome da equipa: "))
        if team == "":
            break
        teams.append(team)
    allMatches(teams)
    results()
    table()
    showTable()
    print(theChampions())
main()