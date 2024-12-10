#Função que transforma a maiúsculas em minúsculas e os espaços em "_"
def novaFrase(s):
    a = ""
    s = s.lower()
    for l in s:
        if l==" ":
            a+="_"
        else:
            a+=l

    return a

def main():
    assert(novaFrase("Hello World") == "hello_world")
    assert(novaFrase("Fundamentos DE Programação") == "fundamentos_de_programação")
    print("All tests passed!")

if __name__ == "__main__":
    main()