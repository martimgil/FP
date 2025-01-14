def compareFiles(f1Name, f2Name):
    f1 = open(f1Name, "r", encoding="utf-8")
    f2 = open(f2Name, "r", encoding="utf-8")
    while True:
        line1 = f1.read(1024)
        line2 = f2.read(1024)
        if line1!=line2:
            print("não são iguais")
            f1.close()
            f2.close()
            break
    print("sao iguais")
    f1.close()
    f2.close()
compareFiles("pauta.txt", "pauta.txt")

