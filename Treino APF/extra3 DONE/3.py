def quantityOf(t,m):
    quantidade = 0

    for i in t:
        if i[0] == m:
            quantidade += i[1]

    return quantidade

def unload(t,m,q):
    for i in t[::-1]:
        if i[0]==m:
            i[1]-=q
            q=0
            if i[1]==0:
                t.remove(i)
            elif i[1]<0:
                q = abs(i[1])
                t.remove(i)

    if q==0:
        return 0
    else:
        return q

def merchandise(t):
    a = {}

    for i in t:
        if i[0] not in a:
            a[i[0]]=0
        a[i[0]]+=i[1]

    return a

def trainsPerMerchandise(trains):
    merch = {}
    for train in trains:
        print("train: ", train)
        print("trains[train]", trains[train][0])
        for merch2 in trains[train]:
            if merch2[0] not in merch:
                merch[merch2[0]] = set()
            merch[merch2[0]].add(train)

    return merch

def main():
    t = [[ "coal", 30], ["rice", 50], ["iron", 5], ["rice", 42], ["coal", 45]]
    print("t: ", t)
    print(unload(t, "rice", 40))
    print(unload(t, "coal", 50))
    print(unload(t, "iron", 20))
    print("c)")
    print(merchandise(t))
    trains =  {"T1": [["salt", 46], ["sand", 53], ["sand", 11], ["sand", 4], ["iron", 5]], "T2": [["rice", 51]], "T3": [["coal", 53]], "T4": [["sand", 56], ["rice", 53], ["coal", 25]]}
    print(trainsPerMerchandise(trains))


main()
