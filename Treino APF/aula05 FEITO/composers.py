# jmr 2024 o programa


# Add auxiliary functions here.


def load_lifetimes_file(file_name):
    lst=[]

    with open(file_name, "r", encoding="utf-8") as f:
        for i in range(5):
            f.readline()
        for line in f:
            line = line.strip().split("\t")
            date1 = line[0].split("/")
            date1 = date1[::-1]
            date2 = line[1].split("/")
            date2 = date2[::-1]
            lst.append((date1,date2, line[2]))

    return lst


def main():
    file_name = 'composers.txt'  # Replace with your file name
    lifes = load_lifetimes_file(file_name)

    print("THE DEAD COMPOSERS SOCIETY")
    print("==========================")
    print("{:<60s} {:<4s} {:>15s}".format("Nome", "Idade", "Data da Morte"))
    for info in lifes:

        idade = int(info[1][0]) - int(info[0][0])
        print("{:<60s} {:<4d} {:>15s}".format(info[2], idade, "/".join(info[1])))
    print("---------------------------------------------------------------------------------------")


    for info in lifes:
        if int(info[0][0])<1800:
            idade = int(info[1][0]) - int(info[0][0])
            print("{:<60s} {:<4d} {:>15s}".format(info[2], idade, "/".join(info[1])))



if __name__ == "__main__":
    main()

