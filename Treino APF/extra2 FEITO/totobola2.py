def loadJornada():
    with open("Jornadas.csv", "r", encoding="utf-8") as f:
        dic = {}
        for line in f:
            line = line.strip().split(",")
            if line[0] not in dic:
                dic[line[0]] = list()
            dic[line[0]].append((line[0], line[1]))

    return dic

def aposta(dic):
    while True:
        j = input("Jornada? ")
        if j not in dic:
            print("Jornada inválida!")
        else:
            break

    aposta = []

    jogos = dic[j]
    for jogo in jogos:
        aposta.append(int(input("{} {} vs {}: ".format(j, jogo[0], jogo[1]))))

    count = 0
    with open("jornada{}.csv".format(j), "w", encoding="utf-8") as f:
        for i in aposta:
            count+=1
            f.write("{}, {}".format(count, i))



