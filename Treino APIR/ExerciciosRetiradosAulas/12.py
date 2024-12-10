def siglas(s):
    s1 = ""
    for l in s:
        if l.isupper()==True:
            s1+=l

    return s1


print(siglas("Universidade de Aveiro"))