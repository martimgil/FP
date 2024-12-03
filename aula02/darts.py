import math

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

sec = 360//20
tan = y/x
ang = math.atan(tan)
ang = math.degrees(ang)
raio = math.sqrt(x**2 + y**2)


#SISTEMA DE PONTUAÇÃO DOS SETORES
ang = ang - 9
if -9<ang<9:
    p = 6
elif 9<ang<27:
    p = 13
elif 27<ang<45:
    p = 4
elif 45<ang<63:
    p = 18
elif 63<ang<81:
    p = 1
elif 81<ang<99:
    p = 20
elif 99<ang<117:
    p = 5
elif 117<ang<135:
    p = 12
elif 135<ang<153:
    p=9
elif 152<ang<171:
    p = 14
elif 171<ang<189:
    p = 11
elif 189<ang<207:
    p=8
elif 207<ang<225:
    p = 16
elif 225<ang<243:
    p=7
elif 243<ang<261:
    p = 19
elif 261<ang<279:
    p = 3
elif 279<ang<297:
    p = 17
elif 297<ang<315:
    p = 2
elif 315<ang<333:
    p = 15
elif 333<ang<351:
    p = 10
elif 351<ang<369:
    p = 6
else:
    p = 0



#SISTEMA DE MULTIPLICAÇÃO DOS SETORES

if raio < 12.7:
    p = 50
elif 12.7<raio<32:
    p = 25
elif 99<raio<107:
    p = 3*p
elif 162<raio<170:
    p = 2*p
elif raio > 225.5:
    p = 0
else:
    p = p


# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...

print(f"Score: {p}")
