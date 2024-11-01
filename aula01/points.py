import math as m
# This program reads the coordinates of two points (x1,y1) and (x2,y2).

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

# create tuples from coordinates
p1 = (x1, y1)
p2 = (x2, y2)

print("Point1:", p1)
print("Point2:", p2)


# Vector P1P2
v1x = x2 - x1
v1y = y2 - y1
v = m.sqrt((v1x**2)+(v1y**2))

print(v)



# Compute and print the distance between the points!
# ...

