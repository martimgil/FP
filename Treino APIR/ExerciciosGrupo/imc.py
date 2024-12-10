peso = float(input("Peso (kg)? "))
altura = float(input("Altura (m)?"))

imc = peso/altura**2
print("O adulto tem um IMC de {:.1f}".format(imc))

if imc<18.5:
    print("Baixo peso")
elif imc<25:
    print("Normal")
else:
    print("Obesidade")