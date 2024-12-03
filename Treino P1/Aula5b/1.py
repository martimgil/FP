#A sequência de Fibonacci começa com os números 0 e 1. Depois, cada elemento consecutivo da sequência obtém-se pela soma dos dois elementos anteriores.
# Complete a função genFibonacci(n) para devolver uma lista com os n primeiros números de Fibonacci. Por exemplo, se n=6,
# deve devolver [0, 1, 1, 2, 3, 5]. Pode presumir que n>=2.

def genFibonacci(n):
    assert n >= 2
    s = [0,1]
    for i in range(2,n):
        s.append(s[i-2]+s[i-1])
    return s
print(genFibonacci(6))