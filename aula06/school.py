# Complete o programa!

# a)
def loadFile(fname, lst):
    f=open(fname,"r")
    next(f)
    for line in f:
        line = line.strip().split("\t")
        info = (int(line[0]), str(line[1]), float(line[5]), float(line[6]), float(line[7]))
        lst.append(info)


    return lst

# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    lst_media = []
    for aluno in reg:
        nota1 = aluno[2]
        nota2 = aluno[3]
        nota3 = aluno[4]
        media = (nota1 + nota2 + nota3) / 3
        info = (aluno[0], aluno[1], media)
        lst_media.append(info)
    return lst_media


# c) Crie a função printPauta aqui...
def printPauta(lst):
    print("{:>6}{:^50}{:>6}".format("Numero", "Nome", "Nota"))
    f=open("pauta.txt", "w")
    for aluno in lst:
        print("{:>6}{:^50}{:>6.1f}".format(aluno[0], aluno[1], aluno[2]))
        f.write("{:>6}{:^50}{:>6.1f}\n".format(aluno[0], aluno[1], aluno[2]))


# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    notas = notaFinal(lst)
    # ordenar a lista
    notas.sort()
    # mostrar a pauta
    printPauta(notas)


# Call main function
if __name__ == "__main__":
    main()


