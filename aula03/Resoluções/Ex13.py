a = int(input("a = "))
b = int(input("b = "))

def mdc(a,b):
    r = a%b
    if r == 0:
        resultado = b
    elif r>0:
        resultado = mdc(b,r)
    else:
        resultado = False
    return resultado

print("Resultado: ", mdc(a, b))
