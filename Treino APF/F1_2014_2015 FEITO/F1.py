# -*- encoding: utf8 -*-
# NOME:
# NMEC:
# Use este ficheiro para o exercicio F1

def readFile():
	leituras = []
	with open("contador.txt", "r", encoding="utf-8") as f:
		for line in f:
			line = line.strip()
			leituras.append(round(int(line)/1000,2))
	return leituras

def simples(leituras):
	gasto = round((leituras[-1] - leituras[0]), 1)
	preco = round(gasto * 0.1528, 2)

	print("Tarifa Simples (kWh): {:.0f}".format(gasto))
	print("Tarifa Simples (Euros): {:.2f}\n".format(preco))

	return preco


def ciclo_diario(leituras):
	leituras_dia = {}
	leituras_dia["domingo"] = leituras[0:25]
	leituras_dia["segunda"] = leituras[24:49]
	leituras_dia["terca"] = leituras[48:73]
	leituras_dia["quarta"] = leituras[72:97]
	leituras_dia["quinta"] = leituras[96:121]
	leituras_dia["sexta"] = leituras[120:145]
	leituras_dia["sabado"] = leituras[144:]

	vazio = 0
	cheia = 0
	for dia in leituras_dia:
		valores = leituras_dia[dia]
		vazio += (valores[8] - valores[0] + valores[24] - valores[22])
		cheia += valores[22] - valores[8]

	gasto = vazio + cheia
	valor = round(vazio * 0.0946 + cheia * 0.1785, 2)

	print("Tarifa Bi-Horária - ciclo diario - vazio (kWh): {:.0f}".format(vazio))
	print("Tarifa Bi-Horária - ciclo diario - vazio (Euros): {:.2f}".format(vazio * 0.0946))
	print("Tarifa Bi-Horária - ciclo diario - fora-vazio (kWh): {:.0f}".format(cheia))
	print("Tarifa Bi-Horária - ciclo diario - fora-vazio (Euros): {:.2f}".format(cheia * 0.1785))
	print("Tarifa Bi-Horária - ciclo diario - Total (Euros): {:.2f}\n".format(valor))

	return valor

def ciclo_semanal(leituras):
	leituras_dia = {}
	leituras_dia["domingo"] = leituras[0:25]
	leituras_dia["segunda"] = leituras[24:49]
	leituras_dia["terca"] = leituras[48:73]
	leituras_dia["quarta"] = leituras[72:97]
	leituras_dia["quinta"] = leituras[96:121]
	leituras_dia["sexta"] = leituras[120:145]
	leituras_dia["sabado"] = leituras[144:]

	vazio = 0
	cheia = 0

	for dia in leituras_dia:
		valores = leituras_dia[dia]

		if dia == "sabado":
			vazio += (valores[10] - valores[0] + valores[18] - valores[13] + valores[24] - valores[22])
			cheia += (valores[13] - valores[10] + valores[22] - valores[18])
		elif dia == "domingo":
			vazio += (valores[24] - valores[0])
		else:
			vazio += (valores[7] - valores[0])
			cheia += (valores[24] - valores[7])

	gasto = round(vazio * 0.0946 + cheia * 0.1785, 2)
	print("Tarifa Bi-Horária - ciclo semanal - vazio (kWh): {:.0f}".format(vazio))
	print("Tarifa Bi-Horária - ciclo semanal - vazio (Euros): {:.2f}".format(vazio * 0.0946))
	print("Tarifa Bi-Horária - ciclo semanal - fora-vazio (kWh): {:.0f}".format(cheia))
	print("Tarifa Bi-Horária - ciclo semanal - fora-vazio (Euros): {:.2f}".format(cheia * 0.1785))
	print("Tarifa Bi-Horária - ciclo semanal - Total (Euros): {:.2f}\n".format(gasto))

	return gasto

def opcao(simples,diario,semanal):
	if simples<diario and simples<semanal:
		print("Tarifário Simples é o mais adequado")
	elif diario<simples and diario<semanal:
		print("Tarifário Bi-Horário com ciclo diário é o mais apropriado")
	elif semanal<simples and semanal<diario:
		print("Tarifário Bi-Horário com ciclo semanal é o mais apropriado")
def main():
	leituras = readFile()
	t_simples = simples(leituras)
	diario = ciclo_diario(leituras)
	semanal = ciclo_semanal(leituras)

	opcao(t_simples, diario, semanal)

main()


