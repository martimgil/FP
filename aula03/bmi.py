def bodyMassIndex(height, weight):
    bmi = (weight/(height)**2)
    return bmi


def bmiCategory(bmi):
    assert bmi>0
    if bmi<18.5:
        cat = "Abaixo do peso"
    elif 18.5<=bmi<25:
        cat = "Peso normal"
    elif 25<=bmi<30:
        cat = "Sobrepeso"
    else:
        cat = "Obesidade"
    return cat

def main():
    print("Índice de Massa Corporal")
    
    altura = float(input("Altura (m)? "))
    if altura < 0:
        print("ERRO: altura inválida!")
        exit(1)

    peso = float(input("Peso (kg)? "))
    if peso < 0:
        print("ERRO: peso inválido!")
        exit(1)

    # Complete the function calls...
    imc = bodyMassIndex(altura,peso)
    cat = bmiCategory(imc)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)
main()

