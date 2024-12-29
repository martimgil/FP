def contar_digitos_recursivo(n):
    n = abs(n)
    if n<10:
        return 1
    else:
        return 1 + contar_digitos_recursivo(n//10)

def main():
    testes_digitos = [12345, 7, 100000, -54321]
    resultados_digitos = {n: contar_digitos_recursivo(n) for n in testes_digitos}
    print(resultados_digitos) # Deve printar {12345: 5, 7: 1, 100000: 6, -54321: 5}

if __name__ == '__main__':
    main()