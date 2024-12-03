def hondt(votes, numseats):
    Ni = [0]*len(votes)
    print(Ni)
    for dep in range(numseats):
        Qi = [0]*len(votes)
        for i in range(len(votes)):
            q=votes[i]/(1+Ni[i])
            Qi.append(q)
        a = max(Qi)
        b = Qi.index(a)
        print(b)
        Ni[b] +=1
    return Ni

hondt([15300, 12000, 6600, 5100], 6)