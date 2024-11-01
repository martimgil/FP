n=int(input("N: "))
a = 0
s=0
while a<=n:
    a = a + 1
    r = n%a
    if r==0:
        print(a)
        s=s+a
    else:
        continue


if s<16:
    print("Deficiente")
elif s==n:
    print("Perfeito")
else:
    print("Abundante") 

