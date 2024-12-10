soma = 0
count = 0

def imc(altura, peso):
    imc=peso/altura**2
    
    return imc
    
def classificacao(imc):
    if imc<18.5:
        print("Baixo Peso\n")
    elif imc<25:
        print("Normal\n")
    else:
        print("Obesidade\n")
        
def lerValorRealPositivo(item):
    valor = float(input(item))
    if valor<0:
        print("Número inválido!\n")
        return lerValorRealPositivo(item)
    else:
        return valor
        
def menu():
    global count, soma
    print("Opções disponíveis:\n")
    print("0 - sair\n")
    print("1 - introduzir nova medida\n")
    print("2 - mostrar média atual\n")
    opcao = int(input("Opção? "))
    if opcao == 1:
        peso = lerValorRealPositivo("Peso? ")
        altura = lerValorRealPositivo("Altura? ")
        imc_valor = imc(altura, peso)
        print("Adulto com um IMC de {:.1f}\n".format(imc_valor))
        classificacao(imc_valor)
        soma += imc_valor
        count +=1
        menu()
    elif opcao == 2:
        print("Estatísticas atuais:\n")
        if count==0:
            print("Ainda não foram efetuados cálculos!\n")
        else:
            media = soma/count
            print("Valor médio do IMC para {} adultos: {:.1f}\n".format(count, media))
        menu()
        
    elif opcao==0:
        print("FIM\nAté breve\n")
    else:
        print("Opção inválida!\n")
        menu()
 
 
print("Bem vindo(a) à calculadora do IMC\n")
menu()