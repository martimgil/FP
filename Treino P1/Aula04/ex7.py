def sentinelTotal():
    soma = 0
    count = 0
    while True:
        v = input("Insira número:")
        if v=="":
            break
        else:
            v = int(v)
            soma +=v
            count +=1
    media = soma/count
    return media

print(sentinelTotal())