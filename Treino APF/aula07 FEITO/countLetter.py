import sys

def countLetters(fileName):
    dic={}
    with open(fileName, "r", encoding="utf-8") as f:
        for line in f:
            words = line.strip().split(" ")
            for word in words:
                for letter in word:
                    if letter in dic:
                        dic[letter] += 1
                    else:
                        dic[letter] = 1

    print(dic)

countLetters("lusiadas.txt")





