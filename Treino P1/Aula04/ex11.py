def divisores(n):
    soma = 0
    for i in range(1,n):
        v = n%i
        if v == 0:
            if n==i:
                continue
            else:
                 print(i)
                 soma += i

    if soma<16:
        print("Número Defeciente")
    elif soma == 6:
        print("Número Perfeito")
    else:
        print("Número abundante")

n=20
divisores(n)