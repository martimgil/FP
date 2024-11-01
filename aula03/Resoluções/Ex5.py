def max2(n1, n2):
    if n1>n2:
        v = n1
    elif n1<n2:
        v = n2
    else:
        v = "Os valores são iguais"
    return v

def max3(n1,n2, n3):
    v = max2(max2(n1, n2), n3)
    return v


def main():
    op = int(input("Deseja comparar dois números ou três?"))
    if op == 2:
        m1 = int(input("Digite o primeiro número: "))
        m2 = int(input("Digite o segundo número: "))
        print(max2(m1, m2))
    elif op == 3:
        m1 = int(input("Digite o primeiro número: "))
        m2 = int(input("Digite o segundo número: "))
        m3 = int(input("Digite o terceiro número: "))
        print(max3(m1, m2, m3))
    else:
        print("Opção inválida")
        exit()
main()