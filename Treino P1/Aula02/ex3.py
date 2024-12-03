n1 = int(input("Primeiro número? "))
n2 = int(input("Segundo número? "))
n3 = int(input("Terceiro número? "))

if n1>n2 and n1>n3:
    print("O primeiro número é o maior.")
elif n2>n1 and n2<n3:
    print("O segundo número é o maior.")
elif n3>n1 and n3>n2:
    print("O terceiro número é o maior.")
else:
    print("Os números são iguais.")
