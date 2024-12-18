# Lista de strings
lista_strings = ["Python", "is", "fun", "cool", "awesome"]
nova_lista = []

inverter = lambda x : x.upper()[::-1] if len(x) % 2 != 0 else x

for item in lista_strings:
    nova_lista.append(inverter(item))

print(nova_lista)
# Deve printar ['Python', 'is', 'NUF', 'cool', 'EMOSEWA']


