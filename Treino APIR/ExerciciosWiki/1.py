lst = [6,1,5,1,6]
n = []


for a in lst:
    if a not in n:
        n.append(a)
    else:
        b = n.index(a)
        n.pop(b)
        n.append(a)
print(n)



