n=int(input("n: "))
soma=0
for i in range(n):
    leibniz = ((-1)**i)/(2*i+1)
    soma =soma + leibniz
    print(leibniz, soma)