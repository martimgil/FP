#Função que calcula a média do aluno e se ele passa à cadeira
def isAproved(ct,cp):
    if ct<7 or cp<7:
        return "Reprovado por Nota Mínima"

    nota = 0.35*ct + (1-0.35)*cp
    if nota<9.5:
        return "Reprovado"
    else:
        return "Aprovado"


def main():
    assert(isAproved(5.3, 14.7) == "Reprovado por Nota Mínima")
    assert(isAproved(12, 8) == "Reprovado")
    assert(isAproved(10, 18) == "Aprovado")

    print("All tests passed!")

if __name__ == "__main__":
    main()
