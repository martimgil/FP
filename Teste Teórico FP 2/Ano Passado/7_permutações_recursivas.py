def permutacoes_recursivas(s):
    
    if len(s) == 1:
        return s
    
    permutacoes = set()
    for i, letra in enumerate(s):
        permutacoes_resto = permutacoes_recursivas(s[:i] + s[i+1:])

        for permutacao in permutacoes_resto:
            permutacoes.add(letra + permutacao)

    return permutacoes

def main():
    exemplo = "abc"
    print(permutacoes_recursivas(exemplo)) # Deve printar {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}

    exemplo = "aab"
    print(permutacoes_recursivas(exemplo)) # Deve printar {'aab', 'aba', 'baa'}

    exemplo = "aaa"
    print(permutacoes_recursivas(exemplo)) # Deve printar {'aaa'}


if __name__ == '__main__':
    main()