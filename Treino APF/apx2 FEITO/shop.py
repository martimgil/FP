def loadDataBase(fname, produtos):
    with open(fname,'r')as f:
        f.readline()
        for line in f:
            codigo=line.split(';')[0]
            nome=line.split(';')[1]
            seccao=line.split(';')[2]
            prbase=line.split(';')[3]
            taxa=line.split(';')[4].replace("%\n"," ")
            produtos[codigo]=(nome,seccao,float(prbase),float(taxa)/100)
    return produtos


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    regista={}

    while True:
        p= input("Code? ")
        if p=="":
            break
        p=p.split()
        p1=p[0]

        if p1 in produtos:
            if len(p)==1:
                prtotal=produtos[p1][-2]+(produtos[p1][-2]*produtos[p1][-1])
                print(produtos[p1][0],1,round(prtotal,2))
                regista[p1]= regista.get(p1,0) + 1
            else:
                qt=int(p[1])
                prtotal=produtos[p1][-2]+(produtos[p1][-2]*produtos[p1][-1])
                print(produtos[p1][0],qt,round(prtotal*qt,2))
                regista[p1]= regista.get(p1,0) + qt
    return regista


def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    totalbruto=0
    totaliva=0
    totalliquido=0
    fat={}
    for prod,quantia in compra.items():
        preco=(produtos[prod][-2]+(produtos[prod][-2]*produtos[prod][-1]))*quantia
        fat[produtos[prod][1]]=fat.get(produtos[prod][1],set())
        fat[produtos[prod][1]].add(prod)
        print(fat)
        #print("{} {} ({}%) {}".format(quantia,produtos[prod][0],int(produtos[prod][-1]*100),round(preco,2)))
        totalbruto+=produtos[prod][-2]*quantia
        totaliva+=(produtos[prod][-2]*produtos[prod][-1])*quantia
        totalliquido+=preco

    for seccao, produt in fat.items():
        print(seccao)
        print(produt)

    print("Total Bruto:",round(totalbruto,2))
    print("Total IVA:",round(totaliva,2))
    print("Total Líquido:",round(totalliquido,2))


def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}

    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)


    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    while repetir:
        op = input(MENU).upper()
        if op == "C":
            compra = registaCompra(produtos)
        elif op == "F":
            fatura(produtos,compra)
        elif op =="S":
            break
    print("Obrigado!")

import sys
if __name__ == "__main__":
    main(sys.argv[1:])

