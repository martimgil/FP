# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.

# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json


def main():
    # Abre o ficheiro e descodifica-o criando o objeto twits.
    with open("twitter.json", encoding="utf8") as f:
        twits = json.load(f)

    lst = []
    for i in range(895):
        texto = twits[i]["text"]
        texto = texto.strip().split(" ")
        for word in texto:
            lst.append(word)
    lst = sorted(lst,key = lambda a: lst.count(a) )

    hashtags = [word for word in lst if word.startswith("#")]
    hashtags = sorted(hashtags, key=lambda a: hashtags.count(a), reverse=True)

    hashtags2=[]
    for a in hashtags:
        if a not in hashtags2 and len(hashtags2)<=10:
            hashtags2.append(a)

    mais_popular = hashtags2[0]
    n_mais_popular = hashtags.count(mais_popular)
    for i in hashtags2:
        s=""
        n = hashtags.count(i)
        x = (n*18/n_mais_popular)
        x = int(round(x, 0))
        per = (n*100/n_mais_popular)
        for h in range(x):
            s+="+"

        print("{:<10s}({:>3.0f}){}".format(i, per, s))







if __name__ == "__main__":
    main()

