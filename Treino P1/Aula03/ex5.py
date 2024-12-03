def max2():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if a>b:
        return a
    elif b>a:
        return b
    else:
        return "Os números são iguais."

def max3():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))

    return max2(max2(a, b), c)
