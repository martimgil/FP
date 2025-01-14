with open("names.txt", "r", encoding="utf-8") as f:
    dic = {}
    f.readline()
    for line in f:
        names = (line.strip().split(" "))
        apelido = names [-1]
        nome = names[0]
        if apelido not in dic:
            dic[apelido] = set()
            dic[apelido].add(nome)
        else:
            dic[apelido].add(nome)
    for i in dic:
        print(i,":",dic[i])

