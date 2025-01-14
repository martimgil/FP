def loadDataBase(fname, produtos):
    with open(fname, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            line = line.strip().split(";")
            iva = float(line[4].replace("%", "")) / 100
            produtos[line[0]] = (line[1], line[2], float(line[3]), iva)
    return produtos

def registaCompra(produtos):
    carrinho = {}
    while True:
        code = input("Code? ")
        if code == "":
            break
        else:
            code = code.strip().split(" ")
            if code[0] in produtos:
                resultado = produtos[code[0]]
                quantidade = int(code[1]) if len(code) > 1 else 1
                preco_final = resultado[2] * (1 + resultado[3])
                print("{} {} {:.2f}".format(resultado[0], quantidade, preco_final * quantidade))

                if code[0] not in carrinho:
                    carrinho[code[0]] = quantidade
                else:
                    carrinho[code[0]] += quantidade
    return carrinho

def fatura(produtos, compra):
    categoria = {}
    total_bruto = 0
    total_iva = 0
    total_liquido = 0
    for produto in compra:
        info = produtos[produto]
        quantidade = compra[produto]
        new_info = (quantidade, info[0], info[2], info[3])
        if info[1] not in categoria:
            categoria[info[1]] = list()
        categoria[info[1]].append(new_info)

    for cat in categoria:
        infos = categoria[cat]
        print(cat)
        for produto in infos:
            preco_bruto = produto[2] * produto[0]
            preco_final = preco_bruto * (1 + produto[3])
            print("     {}  {:<20s} ({:>5.0f}%) {:>10.2f}".format(produto[0], produto[1], produto[3] * 100, preco_final))
            total_bruto += preco_bruto
            total_iva += preco_bruto * produto[3]
            total_liquido += preco_final

    print("{:>25s}{:>8.2f}".format("Total Bruto: ", total_bruto))
    print("{:>25s}{:>8.2f}".format("Total IVA: ", total_iva))
    print("{:>25s}{:>8.2f}".format("Total Liquido: ", total_liquido))

def main():
    produtos = {}
    loadDataBase("produtos.txt", produtos)

    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    compra = []
    while repetir:
        op = input(MENU).upper()
        if op == "C":
            compra.append(registaCompra(produtos))
        elif op == "F":
            if len(compra) > 1:
                n = int(input("Insira o número da compra: ")) - 1
                fatura(produtos, compra[n])
            else:
                fatura(produtos, compra[0])
        elif op == "S":
            break
    print("Obrigado!")

main()