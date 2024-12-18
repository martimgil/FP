def readGames():
    lst = []
    with open ("Jornadas.csv", "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip().split(",")
            print(s)
            lst.append(s)
    return lst
readGames()

#def jornada(n, lst):
    #for i in lst:
       # if i[0]==n:
            

def main():
    lst = readGames()
    n = int(input("Jornada?"))

main()