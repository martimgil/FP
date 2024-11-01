pf = float(input("Preço fabrico: "))
pc = float(input("Preço de capa: "))
imp = int(input("Imposto: "))
spa = float(input("SPA: "))
unidades=int(input("Unidades: "))
lucro = (pc-spa)/(1+imp/100) - pf
lucro_total = unidades*lucro

print("Lucro total: {:.2f}" .format(lucro_total))

imposto = (pc - spa)*(imp/100)
imposto_total = unidades*imposto
print("Imposto total: {:.2f}" .format(imposto_total))