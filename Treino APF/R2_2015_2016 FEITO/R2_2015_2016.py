import random

def sorteio():
	lst = []
	for i in range(4):
		a = random.randint(1,20)
		lst.append(a)
	return lst

def certos(chave, aposta):
	acertos=0
	numeros_corretos = []
	for numero in aposta:
		numero = int(numero)
		if numero in chave:
			acertos+=1
			numeros_corretos.append(numero)
	return acertos, numeros_corretos

def printAposta(chave):
	with open("apostas.csv", "r", encoding="utf-8") as f:
		s1=""
		s2=""
		lst = []
		for line in f:
			line = line.strip().split(",")
			aposta = line[2].strip().split(" ")
			lst.append([line[0], line[1], aposta])

		lst = sorted(lst, key=lambda a:a[0])

		for pessoa in lst:
			aposta = pessoa[2]
			acertos, numeros_corretos = certos(chave,aposta)
			if acertos==4:

				s1+="{:<30s} {:<30s}".format(pessoa[0],pessoa[1])
				for numero in aposta:
					numero=int(numero)
					if numero in numeros_corretos:
						s1+=("({}) ".format(numero))
					else:
						s1+=("{} ".format(numero))
				s1+="\n"
			elif acertos==3:
				s2+="{:<30s}{:<30s}".format(pessoa[0], pessoa[1])
				for numero in aposta:
					numero = int(numero)
					if numero in numeros_corretos:
						s2+=("({}) ".format(numero))
					else:
						s2+=("{} ".format(numero))
				s2+="\n"
	print("1ºs Prémios:")
	print("{:<30s} {:<30s} {}".format("Nome", "Distrito", "Aposta"))
	print(s1)
	print("2ºs Prémios:")
	print("{:<30s} {:<30s} {}".format("Nome", "Distrito", "Aposta"))
	print(s2)

def receita(chave):
	with open("apostas.csv", "r", encoding="utf-8") as f:
		lst = []
		receita = 0
		c0 = 0
		c1 = 0
		c2 = 0
		c3 = 0
		c4 = 0
		for line in f:
			line = line.strip().split(",")
			aposta = line[2].strip().split(" ")
			lst.append([line[0], line[1], aposta])
			acertos, numeros_corretos = certos(chave,aposta)

			receita+=1

			if acertos==0:
				c0+=1
			elif acertos==1:
				c1+=1
			elif acertos==2:
				c2+=1
			elif acertos==3:
				c3+=1
			elif acertos==4:
				c4+=1

		print("Receita: ", receita,"€")
		print("{:<10s}{:>10s}{:>10s}{:>6s}".format("Premio", "Montante", "Premiados", "Valor"))
		if c4>0:
			print("{:<10s}{:>10.2f}{:>10d}{:>10.2f}".format("1o premio", receita*0.30, c4, receita*0.3/c4))
		if c3>0:
			print("{:<10s}{:>10.2f}{:>10d}{:>10.2f}".format("2o premio", receita*0.20, c3, receita*0.3/c3))
		if c2>0:
			print("{:<10s}{:>10.2f}{:>10d}{:>10.2f}".format("3o premio", receita*0.10, c2, receita*0.3/c2))
		if c1>0:
			print("{:<10s}{:>10.2f}{:>10d}{:>10.2f}".format("4o premio", receita*0.10, c1, receita*0.3/c1))


def distribuicao(chave):
	with open("apostas.csv", "r", encoding="utf-8") as f:
		lst = {}

		for line in f:
			line = line.strip().split(",")
			aposta = line[2].strip().split(" ")
			if line[1] not in lst:
				lst[line[1]] = [0,0,0,0]
			acertos, numeros_corretos = certos(chave,aposta)

			if acertos==1:
				lst[line[1]][0] +=1
			elif acertos==2:
				lst[line[1]][1] +=1
			elif acertos==3:
				lst[line[1]][2] +=1
			elif acertos==4:
				lst[line[1]][3] +=1

		print("{:<20s} {:>10s} {:>10s} {:>10s} {:>10s}".format("Distrito", "4 Acertos", "3 Acertos", "2 Acertos", "1 Acertos"))
		for distritos in lst:
			print("{:<20s} {:>10d} {:>10d} {:>10d} {:>10d}".format(distritos, lst[distritos][3], lst[distritos][2], lst[distritos][1], lst[distritos][0]))





def main():
	chave = sorteio()
	print("Chave Sorteada: {} {} {} {}".format(chave[0], chave[1], chave[2], chave[3]))
	printAposta(chave)
	receita(chave)
	distribuicao(chave)
main()