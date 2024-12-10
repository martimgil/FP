"""
Complete a função para devolver a mediana da lista de valores lst.
A função não deve modificar a lista.
Se a lista tiver um número ímpar de valores,
a mediana é o valor no meio da lista ordenada.
Se a lista tiver um número par de valores,
a mediana é a média dos dois valores no meio da lista ordenada.
"""

def median(lst):
    assert len(lst) > 0
    lst_ordenada = sorted(lst)
    n = len(lst)
    meio = n//2

    if n%2==0:
        return (lst_ordenada[meio-1]+lst_ordenada[meio])/2
    else:
        return lst_ordenada[meio]

def check(lst):
    backup = lst.copy()
    m = median(lst)
    return m, lst
