#encoding: utf-8
#F1_2015_2016 - mastermind
import random

def segredo():
	return str(random.randint(1000,9999))

def valida(v):
	if len(v)!=4:
		print("Use 4 algarismos!")
		return False
	else:
		for a in v:
			if a.isdigit()==False:
				print("Use 4 algarismos!")
				return False
	return True

def pontuacao(n, t):
	pos_correta = 0
	pos_errada = 0
	errada = 0
	for i in range(len(t)):
		if n[i] == t[i]:
			pos_correta+=1
		elif n[i] in t[i:]:
			pos_errada +=1
		else:
			errada +=1

	return pos_correta, pos_errada, errada

def recorde(total):
	with open("recorde.txt", "r", encoding="utf-8") as f:
		recorde_atual = f.readline().strip().split("-")

	if total > int(recorde_atual[0]):
		nome = str(input("Novo recorde! Nome? "))
		with open("recorde.txt", "w", encoding="utf-8") as f:
			f.write("{}-{}".format(total, nome))

def jogo():
	tentativas = 10
	pont = 0
	pontuacao_total = 0
	seg = segredo()
	print("Adivinhe o segredo de 4 algarismos. ")
	print("(SEGREDO: {})".format(seg))

	while True:
		tentativas -=1
		while True:
			aposta = str(input("Tentativa {}?".format(10-tentativas)))
			if valida(aposta):
				break
		pos_correta, pos_errada, errada = pontuacao(aposta, seg)
		pontuacao_total += (pos_correta*10+pos_errada*1)
		print("{} certas, {} no lugar errado, {} pontos, total: {} pontos ".format(pos_correta, pos_errada,pos_correta*10+pos_errada, pontuacao_total))


		if pos_correta == 4:
			pontuacao_total+=100*tentativas
			print("Conseguiu em {} tentativas".format(10-tentativas))
			break

	print("Total: {} pontos".format(pontuacao_total))
	recorde(pontuacao_total)

jogo()