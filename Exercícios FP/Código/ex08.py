#Função que calcula a soma dos números pares e faz o produto dos número ímpares
def contas(lista):
    soma = 0
    produto = 1

    for num in lista:
        if num % 2 == 0:
            soma += num
        else:
            produto *= num

    return soma, produto

def main():
    lista = [1, 2, 3, 4, 5, 6]

    soma, produto = contas(lista)

    print(f"Soma dos números pares: {soma}")
    print(f"Produto dos números ímpares: {produto}")

if __name__ == "__main__":
    main()