import math

diameter = float(input("Diameter (m)? "))
height = float(input("Height(m)?"))
num_cols = int(input("Number of columns? "))

radius = diameter/2
surface_area_per_colums = 2*math.pi*radius*height

total_surface_area = surface_area_per_colums * num_cols
paint_volume = total_surface_area / 8 #Litros de tinta

paint_volume = round(paint_volume, 2)

latas_grandes = paint_volume//3
restante_pequenas = paint_volume - (latas_grandes*3)

latas_pequenas = restante_pequenas/0.75

if latas_pequenas>=4:
    latas_grandes += 1
    latas_pequenas=0

print("----")
print(f"Paint Volume(l): {paint_volume}")

