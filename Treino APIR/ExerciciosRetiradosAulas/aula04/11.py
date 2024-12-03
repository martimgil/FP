op  = int(input("N: "))
lst=[]
for i in range(1, op):
    if op%i ==0:
        lst.append(i)
print(lst)
soma = 0
for b in lst:
    soma+=b
if soma<op:
    print("Número deficiente")
if soma==op:
    print("Número perfeito")
if soma>op:
    print("Número abundante")