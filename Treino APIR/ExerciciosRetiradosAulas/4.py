def recurso():
	ctpr = float(input("CTPR?"))
	cpr = float(input("CPR?"))
	
	nota = ctpr*0.3 + cpr*0.7
	if ctpr<66 or cpr<66:
		nota = 66
		print("Reprovado por nota mínima")
	elif nota<95:
		print("Reprovado")
	else:
		print("Aprovado")
	

def normal():
	ctp = float(input("CTP? "))
	cp = float(input("CP?"))

	nota = ctp*0.3 + cp*0.7

	if ctp<66 or cp<66:
		nota = 66
		print("Reprovado por nota mínima")
		recurso()
	elif nota<95:
		print("Reprovado")
		recurso()
	else:
		print("Aprovado")
normal()
		