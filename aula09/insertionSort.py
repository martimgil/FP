def insertionSort(lst, key=None):
    # Se nenhuma função key for fornecida, use a função identidade
    if key is None:
        key = lambda x: x
    
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(lst)):
        # Sabemos que lst[:i] está ordenada
        x = lst[i]  # x é o elemento a ser inserido
        kx = key(x)  # kx é a chave do elemento a ser inserido
        # Elementos em lst[:i] que são > kx devem ser movidos uma posição à frente
        j = i - 1
        while j >= 0 and key(lst[j]) > kx:
            lst[j + 1] = lst[j]
            j -= 1
        # Insere x na última posição vazia
        lst[j + 1] = x
        # Agora sabemos que lst[:i+1] está ordenada
    return lst

def main():
    # Lista original
    lst0 = ["paulo", "augusto", "maria", "paula", "bernardo", "tito"]
    print("lst0", lst0)

    # Ordenar em ordem lexicográfica:
    lst = lst0.copy()
    insertionSort(lst)
    print("lst1", lst)
    assert lst == sorted(lst0)

    # Ordenar por comprimento (requer argumento key):
    lst = lst0.copy()
    insertionSort(lst, key=lambda x: len(x))
    print("lst2", lst)
    assert lst == sorted(lst0, key=len)

    # Ordenar por comprimento, depois em ordem lexicográfica:
    myorder = lambda s: (len(s), s)
    lst = lst0.copy()
    insertionSort(lst, key=myorder)
    print("lst3", lst)
    assert lst == sorted(lst0, key=myorder)

if __name__ == "__main__":
    main()