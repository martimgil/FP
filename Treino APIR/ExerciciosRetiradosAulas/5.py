r = int(input("R: "))

if r<=1000:
    tax = 0.1*r
elif r<=2000:
    tax = 0.2*r-100
else:
    tax = 0.3*r-300

print(tax)