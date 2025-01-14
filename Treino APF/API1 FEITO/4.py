#Escreva um programa que calcule e exiba o fatorial de um número inteiro positivo n, com base nas seguintes regras:

#Se o número n for negativo, exiba uma mensagem de erro informando que n não deve ser negativo.
#Caso contrário, calcule o fatorial de n de forma iterativa.
#O programa deve também exibir o cálculo completo na forma de uma fórmula, mostrando todos os números multiplicados no processo.

def factorial(n):
    if n<0:
        print("N should not be negative!")

    s="{}!=".format(n)
    conta = 1
    for a in range(n,0,-1):
        conta*=a
        s+=str(a)
        if a==1:
            s+=("={}".format(conta))
        else:
            s+="x"

    print(s)

factorial(20)
