def loadFile(fname, info):
    with open(fname,"r", encoding="utf-8") as f:
        info = []
        for line in f:
            line = line.strip().split(",")
            info.append(tuple(line))
    return info

def clubsByCountry(pais, info, fname):
    with open(fname, "w", encoding="utf-8") as f:
        for team in info:
            if pais==team[2]:
                print("{}   {}   {}".format(team[1], team[0], team[3]))
                f.write("{}   {}   {}\n".format(team[1], team[0], team[3]))


def dictByCountry(info):
    dic = {}
    for team in info:
        pais = team[2]
        if pais not in dic:
            dic[pais] = set()
        dic[pais].add(team[1])

    return dic

def bestRank(info):
    best_team = [info[0][1], info[0][4]]
    for team in info:
        if team[4]>best_team[1]:
            best_team = [team[1], team[4]]

    return best_team

def search(info, nome):
    result = []
    for team in info:
        if nome==team[1]:
            result.append(team)
            print(team)
    if len(result)==0:
        print("Erro!")


def mediumRank(info):
    dic = {}
    soma = 0
    results = []

    for team in info:
        pais = team[2]
        if pais not in dic:
            dic[pais] = set()
        dic[pais].add(team[0])

    for pais in dic:
        soma = 0
        count = 0
        for rank in dic[pais]:
            soma+=int(rank[0])
            count+=1
        results.append([pais, soma/count])
    results = sorted(results, key=lambda a:a[1])
    for pais in results:
        print("{} {}".format(pais[0], pais[1]))


def main():
    info=[]
    while True:
        print("0 - Abandonar")
        print("1 - Ler ficheiro")
        print("2 - Pesquisar por país")
        print("3 - Ver clubes por país")
        print("4 - Ver clube que mais subiu no ranking")
        print("5 - Pesquisar clube")
        print("6 - Determinar ranking médio")

        op = int(input("Opção? "))

        if op==0:
            break
        elif op==1:
            loadFile("Soccer_Football_Clubs_Ranking.csv", info)
        elif op==2:
            pais = str(input("País? "))
            clubsByCountry(pais, info, "rankCountry.txt")
        elif op==3:
            dictByCountry(info)
        elif op==4:
            print(bestRank(info))
        elif op==5:
            name = str(input("Nome? "))
            search(info, name)
        elif op==6:
            mediumRank(info)







main()