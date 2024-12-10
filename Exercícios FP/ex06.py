#Função para verificar se o número é uma capicua
#Exemplo -> 1221 é uma capicua
#Exemplo -> 123 não é uma capicua

def capicua(n):
    n=str(n)
    i = ""
    for m in n[::-1]:
        i += m
    if i == n:
        return True
    else:
        return False




def main():
    assert(capicua(19891) == True)
    assert(capicua(251) == False)
    assert(capicua(101) == True)
    assert(capicua(2) == True)
    assert(capicua(-11) == False)
    print("All tests passed!")

if __name__ == "__main__":
    main()