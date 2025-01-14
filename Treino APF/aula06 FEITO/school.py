# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            line = line.strip().split('\t')
            lst.append(tuple(line))
    return lst

# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    lst_media = []
    for aluno in reg:
        media = (float(aluno[5]) + float(aluno[6]) + float(aluno[7])) / 3
        lst_media.append((aluno[0],aluno[1], media))
    return lst_media


# c) Crie a função printPauta aqui...
def printPauta(lst):
    reg = notaFinal(lst)

    with open("pauta.txt", "w", encoding="utf-8") as f:
        print("{:>6s}{:^80s}{:>4s}".format("Numero", "Nome", "Nota"))
        f.write("{:>6s}{:^80s}{:>4s}".format("Numero", "Nome", "Nota"))
        for a in reg:
            print("{:>6d}{:^80s}{:>4.1f}" .format(int(a[0]), str(a[1]), float(a[2])))
            f.write("{:>6d}{:^80s}{:>4.1f}\n" .format(int(a[0]), str(a[1]), float(a[2])))

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)

    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    printPauta(lst)

# Call main function
if __name__ == "__main__":
    main()


