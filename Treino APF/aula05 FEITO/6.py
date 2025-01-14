def abreviar(s):
    st = ""
    for l in s:
        if l.isupper():
            st+=l
    return st

def main():
    print(abreviar("Universidade de Aveiro"))
    print(abreviar("United Nation Organization"))

main()
