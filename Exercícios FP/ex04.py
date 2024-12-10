#Função para calcular o lucro do banco num empréstimo (A duração é dada em anos)
def lucro(juros, quantia, duracao):

    v_juros = (duracao*12)*(quantia*(juros/100))


    return v_juros

def main():

    assert(lucro(1000, 1.7, 2) == 408)
    assert(lucro(300, 4, 1) == 144)
    assert(lucro(2500, 2, 5) == 3000)

    print("All tests passed!")

if __name__ == "__main__":
    main()
