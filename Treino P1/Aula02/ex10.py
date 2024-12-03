import math

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

d = math.sqrt(x**2 + y**2)
angulo = math.degrees(math.atan(y/x))

angulo = angulo - 9

if -9<angulo<9:
    p = 6
elif 9<angulo<27:
    p=13
elif 27<angulo<45:
    p = 4
elif 45<angulo<63:
    p = 18
elif 63<angulo<81:
    p = 1
elif 81<angulo<99:
    p = 20
elif 99<angulo<117:
    p = 5
elif 117<angulo<135:
    p = 12
elif 135<angulo<153:
    p = 9
elif 153<angulo<171:
    p = 14
elif 171<angulo<189:
    p = 11
elif 189<angulo<207:
    p = 8
elif 207<angulo<225:
    p = 16
elif 225<angulo<243:
    p = 7
elif 243<angulo<261:
    p = 19
elif 261<angulo<279:
    p = 3
elif 279<angulo<297:
    p = 17
elif 297<angulo<315:
    p = 2
elif 315<angulo<333:
    p = 15
elif 333<angulo<351:
    p = 10
elif 351<angulo<369:
    p = 6
else:
    p = 0


if d < 12.7:
    p = 50
elif 12.7< d <32:
    p = 25
elif 99< d <107:
    p = 3*p
elif 162< d <170:
    p = 2*p
elif d > 225.5:
    p = 0
else:
    p = p


# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...

print(f"Score: {p}")