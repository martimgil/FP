def inputFloatList():
    lst = []
    while True:
        n = (input("Insira número: "))

        if n == "":
            break
        else:
           n = int(n)
           lst.append(n)
    return lst

def countLower(lst,v):
    count = 0
    for element in lst:
        if element<v:
            count += 1
    return count

def minmax(lst):
    max = lst[0]
    min = lst[0]
    for element in lst:
        if element>max:
            max = element
        elif element<min:
            min = element
    return max, min

def main():
    lst = inputFloatList()
    max, min = minmax(lst)
    media = (max+min)/2
    count = countLower(lst,media)

main()
