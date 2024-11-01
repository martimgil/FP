n=int(input("n:"))

def media(n):    
    soma=0
    c=0
    while True:
        n=(input("n:"))
        if n=="":
            break
        else:
            n = int(n)
            soma = soma + n
            c=c+1
    media = soma/c
    return (media)

print(media(n))


