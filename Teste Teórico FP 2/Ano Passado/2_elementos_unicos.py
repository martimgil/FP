def elementos_unicos(lista_de_listas):
    s = set()
    d = {}
    for item in lista_de_listas:
        for i in item:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

            if d[i] == 1:
                s.add(i)
            elif d[i] > 1:
                s.remove(i)
    return s

def main():
    listas_teste = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    print(elementos_unicos(listas_teste)) # Deve printar {1, 2, 4, 6, 7}

    listas_teste = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [1, 2, 7]]
    print(elementos_unicos(listas_teste)) # Deve printar {4, 6}

if __name__ == '__main__':
    main()