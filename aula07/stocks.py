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
    for a in lst:
        totVol[a[0]]=a[6]
    return totVol

def maxValorization(lst):
    vMax = {}
    for a in lst:
        vMax[a[1]]=(a[0],a[5]-a[2]-1)


    return vMax

def stocksByDateByName(lst):
    dic = {}
    for a in lst:
        if a[1] not in dic:
            dic[a[1]] = {}
        dic[a[1]][a[0]] = (a[2], a[3], a[4], a[5], a[6])
    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for name, quantity in portfolio.items():
        if (name,date) in stocks:
            val += stocks[(name, date)[3]*quantity]

    return val

if __name__ == "__main__":
    main()
