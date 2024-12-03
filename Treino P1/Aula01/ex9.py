pf = 20
pc = 24.95
spa = 0.2
imp = 0.23
lucro = (pc - spa)/(1+imp)-pf
print(lucro)
unidades = 500
lucro_total = unidades*lucro
print(lucro_total)
imposto = (pc-spa)/(pf+lucro)-1
imposto_total = unidades*imposto

print(imposto_total)
