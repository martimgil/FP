# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname) as file:
        file.readline()
        for l in file:
            linha=l.strip("\n")
            linha=linha.split(";")
            produtos[linha[0]]=tuple(linha[1:])
    return produtos

def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    dic={}
    while True:
        codeq= input("Code? ")
        parts = codeq.split(" ")
        if len(parts) > 1:
            q = int(parts[1])
        else:
            q = 1
        code=parts[0]
        if codeq=="":
            break
        elif code not in produtos:
            continue
        values=produtos[code]
        if code not in dic:
            dic[code]=q
        else:
            dic[code]+=q
        preço= float(values[2])*float(q)*(1+0.01*float(values[3].strip("%")))
        print(values[0],q,("{:.2f}".format(preço)))
    return dic

def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    n=int(input("Numero compra? "))-1
    cat={} #categoria (mercearias, etc...)
    tb=0
    ti=0
    tl=0
    for c, quant in compra[n].items():
        preco=quant*float(produtos[c][2])
        tb+=preco
        prod=produtos[c][0]
        iva=0.01*float(produtos[c][3].strip("%"))
        ti+=iva*preco
        precoi=preco*(1+iva)
        tl+=precoi
        if produtos[c][1] not in cat:
            cat[produtos[c][1]]=[quant,prod,iva,precoi]
            print(produtos[c][1])
        else:
            cat[produtos[c][1]].append((quant,prod,iva,precoi))
        print("{:5d} {:35s} ({:>2}%) {:10.2f}".format(quant,prod,int(iva*100),precoi))
    print("{:>48}{:10.2f}".format("Total Bruto: ",tb)) #preço sem iva)
    print("{:>48}{:10.2f}".format("Total IVA: ",ti)) #iva)
    print("{:>48}{:10.2f}".format("Total Liquido: ",tl))#preço total

def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup', 'Mercearia Salgado', 1.59, 0.23)}
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    compra=[]
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra.append(registaCompra(produtos))
        if op== "F":
            Fatura = fatura(produtos, compra)
        if op== "S":
            break
    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])

