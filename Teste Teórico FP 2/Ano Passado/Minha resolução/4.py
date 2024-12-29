lst = ["ola", "bem", "mau", "ja", "nao", "mais", "menos"]

a = (lambda lst: [word.upper() for word in lst[:-1]])(lst)
print(a)