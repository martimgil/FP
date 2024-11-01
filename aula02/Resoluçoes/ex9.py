def recurso():
    print("--- EPOCA DE RECURSO ---")
    ctp_r = float(input("Insira a nota da componente teorico-pratica: "))
    cp_r = float(input("Insira a nota da componente prática: "))
    nf_r = 0.30*ctp_r + 0.7 *cp_r

    if ctp_r <6.5 or cp_r <6.5:
        print("Reprovado por nota mínima")
    elif nf_r < 9.5 :
        print("Reprovado por nota final")
    else:
        nf_r=int(nf_r)
        print("Aprovado com a nota final de {:2d}".format(nf_r))


print("--- CÁLCULO DA NOTA FINAL - FUNDAMENTOS DE PROGRAMAÇÃO ---")

ctp = float(input("Digite a nota da componente teórico-prática: "))
cp = float(input("Digite a nota da componente prática: "))

nf = 0.30 * ctp + 0.70 * cp

if ctp <6.5 or cp <6.5:
    print("Reprovado por nota mínima")
    recurso()
elif nf < 9.5:
    print("Reprovado por nota final")
    recurso()
else:
    nf = int(nf)
    print("Aprovado com a nota final de {:2d}".format(nf))  

  