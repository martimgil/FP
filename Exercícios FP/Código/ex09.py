#Função que transforma a maiúsculas em minúsculas e os espaços em "_"
def novaFrase(frase):
    nova = frase.lower().replace(" ", "_")
    return nova

def main():
    assert(novaFrase("Hello World") == "hello_world")
    assert(novaFrase("Fundamentos DE Programação") == "fundamentos_de_programação")
    print("All tests passed!")

if __name__ == "__main__":
    main()