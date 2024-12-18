lista_pessoas = [("João", 25), ("Ana", 20), ("Carlos", 30)] 

resultado = sorted(lista_pessoas, key = lambda x: (len(x[0]), x[1]))

print(resultado)
