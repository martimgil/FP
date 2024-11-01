import math as m

#Determinar a hipotenua
c1 = float(input("Insira o valor do lado A: "))
c2 = float(input("Insira o valor do lado B: "))
h=m.hypot(c1,c2)

cos = c1/h
ang = m.acos(cos)
ang = m.degrees(ang)
print("O valor da hipotenusa é {:.1f} e o ângulo entre a hipotenua e o lado A são {:.1f}" .format(h, ang))