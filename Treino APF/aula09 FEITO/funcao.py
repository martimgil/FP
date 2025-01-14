import math

def findZero(func, a, b, tol):
    if func(a) * func(b) > 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        
        if func(c) == 0:  
            return c
        elif func(a) * func(c) < 0:  
            b = c
        else: 
            a = c    
    return (a + b) / 2

def f(x):
    return x + math.sin(10 * x)

raiz = findZero(f, 0.2, 0.4, 0.0001)
print("Raiz encontrada:", raiz)
