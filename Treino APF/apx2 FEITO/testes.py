produtos = {}
with open("produtos.txt") as file:
    file.readline()
    for l in file:
        linha=l.strip("\n")
        linha=linha.split(";")
        produtos[linha[0]]=tuple(linha[1:])
print(produtos)
