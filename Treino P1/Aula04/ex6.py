def leibnizPi4(n):
    soma = 0
    for i in range (n):
        v = (-1)**i/(2*i+1)
        soma +=v
    return soma

n =2000000000000
print(leibnizPi4(n))