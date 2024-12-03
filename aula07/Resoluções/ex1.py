f = open("camoes.txt","r", encoding="utf-8")
alpha = {}

for line in f:
    s=line.strip().split()
    for c in line:
        c=c.lower()
        if c.isalpha():
            if c not in alpha:
                alpha[c]=0
            alpha[c]+=1


alpha_ordenada = sorted(alpha.items())

for a in alpha_ordenada:
    print("{:>2s}{:>6d}".format(a[0], a[1]))

