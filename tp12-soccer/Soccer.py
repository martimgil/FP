def openfile():
    with open("Soccer_Football_Clubs_Ranking.csv", "r", encoding='utf-8') as f:
        f.readline()
        lst = []

        for i in f:
            dados = i.strip().split(',')
            lst.append(tuple(dados))
    return lst

def searchByCoutry(lst, country):
    result = []
    for i in lst:
        country = country.lower()
        if i[2].lower() == country:
            result.append((i[0], i[1], i[3]))
    saveInfo(result)
    return result

def saveInfo(result):
    with open("results.txt", "w", encoding="utf-8") as f:
        for i in result:
            print(i)
            f.write((str(i)))

def dictByCountry(lst):
    d = {}
    for a in lst:
        if a[2] not in d:
            d[a[2]] = []
        d[a[2]]. append(a[1])
    return d



def main():
    lst = openfile()
    searchByCoutry(lst, "Portugal")
    print(dictByCountry(lst))







main()