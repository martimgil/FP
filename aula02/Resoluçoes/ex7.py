altura = float(input("Altura (m)? "))
peso = float(input("Peso (kg)? "))

imc = peso/(altura**2)

if imc < 18.5:
    print("Magro")
elif imc < 25 and imc>=18.5:
    print("Saudável")
elif imc>=25 and imc<30:
    print("Forte")
else:
    print("Obeso")
