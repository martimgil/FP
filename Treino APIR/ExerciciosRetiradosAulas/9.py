def sequence():
	soma = 0
	count = 0
	
	n = (input("Insira número: "))
	
	while n!="":
		n=float(n)
		soma +=n
		count+=1
		n=(input("Insira número: "))
	
	media = soma/count
	
	print(media)

sequence()
