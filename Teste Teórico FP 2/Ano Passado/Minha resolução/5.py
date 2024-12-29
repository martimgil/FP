def soma_recursiva(n):
    if n<=0:
        return 0
    else:
        return n + soma_recursiva(n-1)

def main():
    testes = [5, 10, 0, -3, 1]
    resultados = {n: soma_recursiva(n) for n in testes}
    print(resultados) # Deve printar {5: 15, 10: 55, 0: 0, -3: 0, 1: 1}

if __name__ == '__main__':
    main()
