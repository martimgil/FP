def trocas(lista, num1, num2):

    if num1 in lista and num2 in lista:
        index1 = lista.index(num1)
        index2 = lista.index(num2)

        lista[index1], lista[index2] = lista[index2], lista[index1]

    return lista

def main():
    assert(trocas([1, 3, 5], 3, 5) == [1, 5, 3])
    assert(trocas([8, 9, 5, 11], 9, 11)== [8, 11, 5, 9])
    print("All tests passed!")

if __name__ == "__main__":
    main()