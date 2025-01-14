# Complete este programa como pedido no guião da aula.
def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^25s} : {:<10s}".format("Numero", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^25s} :{:<10s}".format(num, dic[num][0], dic[num][1]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    results = {}
    partName = partName.lower()
    for number in contacts:
        name = contacts[number][0]
        name = name.lower()

        if partName in name:
            results[number] = name

    return results





def addConctact(contactos):
    name = str(input("Insira o nome: "))
    number = str(input("Insira o número"))
    morada = str(input("Insira a morada: "))
    contactos[name] = (number, morada)

  

def removeContact(contactos):
    number = str(input("Insira o número: "))
    contactos.pop(number)

    return contactos

def searchContact(contactos):
    number = str(input("Insira o número: "))

    if number in contactos:
        print(contactos[number])
    else:
        print("Número não encontrado")


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper() 
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro","Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro","Crasto, Aveiro"),
        "387719992": ("Maria Matos","Coimbra"),
        "887555987": ("Marta Maia", "Lisboa"),
        "876111333": ("Carlos Martins", "Porto"),
        "433162999": ("Ana Bacalhau", "Leiria")
        }
    print(contactos["234370200"][0])


    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addConctact(contactos)
        elif op=="R":
            removeContact(contactos)
        elif op=="N":
            searchContact(contactos)
        elif op =="P":
            partName= input("Insira o nome")
            print(filterPartName(contactos, partName))
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

