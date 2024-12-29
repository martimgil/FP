def loadfile(fname1,lst):
    with open(fname1, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            line = line.strip().split("\t")
            lst.append(line)

def notaFinal(reg):


lst = []
loadfile("school1.csv", lst)