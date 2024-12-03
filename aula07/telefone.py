# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^25s} : {:<10s}".format("Numero", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^25s} :{:<10s}".format(num, dic[num][0], dic[num][1]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    result={}
    for contacts, name in contacts.items():
        if partName.lower()in name[0].lower():
            result[contacts]=name
    return result


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op

def addContact(contactos):
    nome = str(input("Indique nome: "))
    numero = str(input("Indique número: "))
    morada = str(input("Indique morada: "))
    contactos[numero]=(nome, morada)


def removeContact(contactos):
    numero = str(input("Indique o número que prentende eliminar: "))
    contactos.pop(numero)
    print("Removido com sucesso!")

def searchContact(contactos):
    numero = str(input("Indique o número"))

    if numero in contactos:
        print(contactos.get(numero))
    else:
        print(numero)



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

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op=="A":
            addContact(contactos)
        elif op=="R":
            removeContact(contactos)
        elif op=="N":
            searchContact(contactos)
        elif op=="P":
            partName = str(input("Indique o nome: "))
            a = filterPartName(contactos, partName)
            print(a)
        else:
            print("Não implementado!")


# O programa começa aqui
main()

