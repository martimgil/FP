def jogos():
    with open("Jornadas.csv", "r", encoding="utf-8") as f:
        registo = {}
        for line in f:
            line = line.strip().split(",")

            if line[0] not in registo:
                registo[line[0]] = set()

            registo[line[0]].add((line[1], line[2]))

    return registo

def calcular_multiplas(apostas):
    total_apostas = 1
    for aposta in apostas.values():
        total_apostas *= len(aposta)
    return total_apostas

def jornada(registo):
    carteira = 0
    while True:
        print("Saldo: {:.2f} euros".format(carteira))
        n = input("Jornada? (0 para sair): ")
        if n == "0":
            break
        if n in registo:

            with open("Jornada{}.csv".format(n), "w", encoding="utf-8") as f:
                jogos = registo[n]
                count = 1
                apostas = {}

                for jogo in jogos:
                    while True:
                        aposta = input("{} {} vs {} (1, X, 2, 1X, X2, 12, 1X2): ".format(count, jogo[0], jogo[1]))
                        if set(aposta).issubset({"1", "X", "2"}) and len(aposta) <= 3:
                            apostas[str(count)] = list(aposta)
                            f.write("{},{}\n".format(count, aposta))
                            count += 1
                            break
                        else:
                            print("Aposta inválida! Use apenas 1, X, 2, ou combinações como 1X, X2, 12, 1X2.")

                # Calcular o número total de apostas equivalentes
                total_apostas = calcular_multiplas(apostas)
                custo_total = total_apostas * 0.40
                carteira -= custo_total

                print("\nApostas registadas para a Jornada {}: {} apostas equivalentes".format(n, total_apostas))
                print("Custo total: {:.2f} euros".format(custo_total))
                print("Novo saldo: {:.2f} euros\n".format(carteira))

            with open("Jogos.csv", "r", encoding="utf-8") as f2:
                with open("Jornada{}.csv".format(n), "r", encoding="utf-8") as f:
                    print("Jornada {}".format(n))
                    count = 1
                    apostas = {}
                    for line in f:
                        line = line.strip().split(",")
                        apostas[line[0]] = line[1]

                    corretos = 0
                    for line2 in f2:
                        if count > 9:
                            break
                        line2 = line2.strip().split(",")
                        casa = line2[1]
                        fora = line2[2]
                        golos1 = int(line2[3])
                        golos2 = int(line2[4])
                        if str(count) in apostas:
                            aposta = apostas[str(count)]
                            if (aposta == "1" and golos1 > golos2) or (aposta == "2" and golos1 < golos2) or (aposta == "X" and golos1 == golos2):
                                resultado = "CERTO"
                                corretos += 1
                            else:
                                resultado = "ERRADO"
                            print("{:<1s} {} {}-{} {} : {} ({})".format(str(count), casa, fora, golos1, golos2, aposta, resultado))
                        else:
                            print("{:<1s} {} {}-{} {} : Sem aposta".format(str(count), casa, fora, golos1, golos2))

                        count += 1
                    if corretos == 7:
                        print("TEM {} CERTAS. 3º PRÉMIO".format(corretos))
                        carteira += 100
                    elif corretos == 8:
                        print("TEM {} CERTAS. 2º PRÉMIO".format(corretos))
                        carteira += 1000
                    elif corretos == 9:
                        print("TEM {} CERTAS. 1º PRÉMIO".format(corretos))
                        carteira += 5000
                    else:
                        print("TEM {} CERTAS. SEM PRÉMIO".format(corretos))

        else:
            print("Jornada inválida!")

def main():
    registo = jogos()
    jornada(registo)

main()
