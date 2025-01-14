
def loadFile(fname):
    lst = []
    with open(fname, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            line = line.strip().split(",")
            lst.append(tuple(line))
    return lst

def rankCountry(country, lst):
    results = []
    for club in lst:
        if club[2] == country:
            results.append((club[1], club[0], club[3]))
            print("{} {} {} ".format(club[1], club[0], club[3]))
    return results

def dic(lst):
    results = {}
    for club in lst:
        if club[2] not in results:
            results[club[2]]=list()

        results[club[2]].append(club[1])
    return results

def search(lst, name):
    result= []
    for club in lst:
        if club[1] == name:
            result.append(club)

    if len(result) ==0:
        print("Sem resultados!")
    else:
        print(result)

def mediumRank(lst):
    countrys = []
    clubs = dic(lst)
    values = []
    for club in lst:
        if club[2] not in countrys:
            countrys.append(club[2])

    rankings = {}
    for club in lst:
        if club[2] not in rankings:
            rankings[club[2]]=list()
        rankings[club[2]].append(club[0])
    for country in rankings:
        sum = 0
        ranks = rankings[country]
        for rank in ranks:
            sum += int(rank)
        medium = sum/len(ranks)
        values.append((country, medium))

        print(country, medium)

    values=sorted(values, key=lambda country: country[1])
    print(values)




def rank(lst):
    max_club = max(lst, key=lambda a: int(a[4]))
    return max_club

def saveRankCountry(results, fname):
    with open(fname, "w", encoding="utf-8") as f:
        for club in results:
            f.write("{} {} {}\n".format(club[0], club[1], club[2]))

def main():
    lst = []
    while True:
        print("Menu:")
        print("0. Sair")
        print("1. Carregar ficheiro")
        print("2. Imprimir clubes de um país")
        print("3. Criar dicionário de países e clubes")
        print("4. Procurar clube pelo nome")
        print("5. Determinar ranking médio de cada país")
        op = int(input("Opção? "))
        if op == 0:
            break
        elif op == 1:
            fname = input("Ficheiro? ")
            lst = loadFile(fname)
        elif op == 2:
            country = input("País? ")
            rankCountry(country, lst)
        elif op == 3:
            print(dic(lst))
        elif op == 4:
            name = input("Nome? ")
            search(lst, name)
        elif op == 5:
            mediumRank(lst)

main()


main()
