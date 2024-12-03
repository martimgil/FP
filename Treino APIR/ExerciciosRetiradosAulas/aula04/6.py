def leibnizPi4(n):
    soma=0
    for a in range(n):
        soma += ((-1)**a)/(2*a+1)
    return soma

print(leibnizPi4(1000))

