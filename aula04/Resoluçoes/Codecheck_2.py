def inputTotal():
    tot = 0.0
    while True:
        valor = input("valor? ")
        if valor == "":
            break
        else:
            valor = float(valor)
            tot += valor
    return tot

# MAIN PROGRAM
def main():
    tot = inputTotal()
    print(tot)

if __name__ == "__main__":
    main()