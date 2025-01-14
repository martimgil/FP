#Implemente uma função que recebe uma lista de números inteiros e devolve uma nova lista com os índices onde ocorre um aumento no valor
# em relação
# ao número imediatamente anterior na lista original.

#Regras:
#A função deve percorrer a lista e identificar os índices onde o elemento atual é maior que o elemento anterior.
#Esses índices devem ser adicionados a uma nova lista, que será devolvida como resultado.

#Entrada: [3, 7, 5, 8, 6, 10]

def numList(lst):
    ind = []
    for a in range(1,len(lst)):
        if lst[a]>lst[a-1]:
            ind.append(a)

    return ind

print(numList([3, 7, 5, 8, 6, 10]))