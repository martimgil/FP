from aula02.Resoluçoes.ex9 import recurso

ctp = float(input("Nota CTP: "))
cp = float(input("Nota CP: "))

c = ctp*0.3 + cp*0.7

if ctp<66 or cp<66:
    print("Reprovado por nota mínima")
    recurso()
elif c<95:
    print("Reprovado por nota final")
    recurso()
else:
    print("Aprovado")

def recurso():
    ctpr = float(input("Nota CTPR: "))
    cpr = float(input("Nota CPR: "))

    cr = ctpr*0.3 + cpr*0.7

    if ctpr<66 or cp<66:
        print("Reprovado por nota mínima")
    elif cr<95:
        print("Reprovado por nota final")
    else:
        print("Aprovado")
