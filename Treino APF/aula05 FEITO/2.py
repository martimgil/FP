def inputFloatList():
    lst = []
    while True:
        val = input("Valor? ")
        if val == "":
            break
        else:
            lst.append(float(val))
    return lst

def countLower(lst, v):
    count = 0
    for number in lst:
        if number < v:
            count += 1
    return count

def minmax(lst):
    max_val = lst[0]
    min_val = lst[0]
    for number in lst:
        if number > max_val:
            max_val = number
        if number < min_val:
            min_val = number
    return min_val, max_val

def main():
    lst = inputFloatList()
    if lst:
        min_val, max_val = minmax(lst)
        media = (min_val + max_val) / 2
        print(countLower(lst, media))
    else:
        print("A lista está vazia.")

main()