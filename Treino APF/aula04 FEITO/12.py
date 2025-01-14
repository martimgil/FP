def divisores(n):
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    soma = sum(lst)
    for b in lst:
        print(b)
    if soma < n:
        print("Deficiente")
    elif soma == n:
        print("Perfeito")
    else:
        print("Abundante")

divisores(16)