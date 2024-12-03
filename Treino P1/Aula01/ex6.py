import math

a = int(input("Cateto A: "))
b = int(input("Cateto B: "))

c = math.sqrt((a**2)+(b**2))

angulo = math.acos(a/c)
angulo = math.degrees(angulo)

print(c, angulo)
