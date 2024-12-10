#Função para trocar elementos de posição numa lista
def trocas(lst,a,b):
    ai = lst.index(a)
    bi = lst.index(b)

    lst.remove(a)
    lst.remove(b)
    lst.insert(bi, a)
    lst.insert(ai,b)


    return lst

def main():
    assert(trocas([1, 3, 5], 3, 5) == [1, 5, 3])
    assert(trocas([8, 9, 5, 11], 9, 11)== [8, 11, 5, 9])
    print("All tests passed!")

if __name__ == "__main__":
    main()