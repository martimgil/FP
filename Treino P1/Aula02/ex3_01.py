n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
n4 = int(input("Quarto número: "))

if n4>n2 and n4>n3 and n4>n1:
    print(n4)
elif n3>n1 and n3>n2 and n3>n4:
    print(n3)
elif n2>n1 and n2>n3 and n2>n4:
    print(n2)
else:
    print(n1)