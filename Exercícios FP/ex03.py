# Calculadora de IMC
# Recebe o peso e a altura, calcula o IMC e imprime o resultado juntamente com a categoria
def main():
    # receber peso e altura
    peso = float(input("Digite o peso (em kilogramas): ")) 
    altura = float(input("Digite a altura (em metros): "))
    print(IMC(peso, altura))
    # para testar, use os valores 80 e 1.80 para peso e altura, respectivamente 
    # em que o resultado deve ser 24.69 e Saudável

#Função para calcular o IMC
def IMC(peso, altura):
    imc = peso/altura**2
    if imc<18.5:
        return "Magro"
    elif imc<25:
        return "Saudável"
    elif imc<30:
        return "Forte"
    else:
        return "Obeso"


if __name__ == "__main__":
    main()