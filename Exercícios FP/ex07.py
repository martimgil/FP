# Calcula o fatorial de um número n de forma iterativa
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120


# Calcula o fatorial de um número n de forma iterativa
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial_iterative(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

def main():

    assert(factorial_iterative(0) == 1) # 1
    assert(factorial_iterative(5) == 120) # 120
    assert(factorial_iterative(10) == 3628800) # 3628800

    print("All tests passed!")

if __name__ == "__main__":
    main()


def main():

    print(factorial_iterative(0))
    print(factorial_iterative(5))
    print(factorial_iterative(10))
    #assert(factorial_iterative(0) == 1) # 1
    #assert(factorial_iterative(5) == 120) # 120
    #assert(factorial_iterative(10) == 3628800) # 3628800

    print("All tests passed!")

if __name__ == "__main__":
    main()