#Função que calcula a média do aluno e se ele passa à cadeira
def isAproved(teo, pratica):
    if teo < 7 or pratica < 7:
        return "Reprovado por Nota Mínima"
    
    media = (teo * 0.35) + (pratica * 0.65)
    if media < 9.5:
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