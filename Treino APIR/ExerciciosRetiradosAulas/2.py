pf = 20
pc = 24.95
imp = 0.23
spa = 0.2
exemplares = 500


lucro = (pc - spa)/(1+imp) - pf


lucro_total = exemplares*lucro

imp = (pc - spa)*0.23

imp_total = imp * exemplares

print(lucro_total,"\n",imp_total)
