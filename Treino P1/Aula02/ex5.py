p1 = 0.12
s1 = 0.002
t = int(input("Tempo de ligação: "))

if t<=60:
    p = p1
else:
    p = p1 + s1*(t-60)

print("Preço da chamda: {:.2f}€" .format(p))
