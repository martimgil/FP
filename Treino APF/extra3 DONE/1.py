import sys,random

def printStocks(stocks):
    for empresa in stocks:
        print("{} {} {} {} {} {}".format(empresa[0], empresa[1], empresa[2], empresa[3], empresa[4], (empresa[3] - empresa[2])/empresa[2]*100 ))

def sorted3(stocks):
    return sorted(stocks, key=lambda a:(a[0], -a[4]))


def main():
    # Cada tuplo = (empresa, cidade, abertura, fecho, volume)
    stocks = [ ('INTC', 'London', 34.249, 34.451, 1792860),
               ('TSLA', 'London', 221.33, 229.63, 398520),
               ('EA', 'Paris', 72.63, 68.98, 1189510),
               ('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
               ('TSLA', 'Paris', 217.35, 217.75, 252500),
               ('ATML', 'Frankfurt', 8.23, 8.36, 810440),
               ]
    stocks = [r for r, c in zip(stocks, sys.argv[-1]*3) if c != '-']
    random.shuffle(stocks)   # Shuffle elements / Baralha os elementos
    stocks0 = stocks.copy()

    print("----")
    printStocks(stocks)      # CHAMADA / CALL
    print(sorted3(stocks))
    stocks2 = [stock for stock in stocks if stock[1]=="Paris"]
    print(sorted3(stocks2))



main()