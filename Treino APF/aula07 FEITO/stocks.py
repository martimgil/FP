
# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")
    # Show just first and last tuples:
    print("first:", lst[1])
    print("last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    for i in lst:
        totVol[i[NAME]]=i[VOLUME]
    print(totVol)
    return totVol

def maxValorization(lst):
    vMax = {}
    for i in lst:
        if i[1] in vMax:
            if (i[5]/i[2] - 1)> vMax[i[1]][1]:
                vMax[i[1]]=(i[0],i[5]/i[2]-1)
        else:
            vMax[i[1]]=(i[0],i[5]/i[2]-1)


    return vMax

def stocksByDateByName(lst):
    dic = {}
    # Complete ...
    for i in lst:
        if i[1] not in dic:
            dic[i[1]]={}
        dic[i[1]][i[0]]=(i[2], i[3], i[4], i[5], i[6])
    print(dic)
    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for i in portfolio:
        val += int(portfolio[i])*float(stocks[date][i][3])

    return val

if __name__ == "__main__":
    main()
