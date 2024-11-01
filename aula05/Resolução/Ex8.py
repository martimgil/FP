def evenThenOdd(s):
    new_s=""
    for letter in s[::2]:
        new_s+=letter
    for letter in s[1::2]:
        new_s+=letter
    return new_s

def removeAdjacentDuplicates(s):
    previous_letter=s[0]
    new_s = previous_letter
    for next_letter in s[1::]:
        if previous_letter == next_letter:
            previous_letter = next_letter
            continue
        else:
            new_s += next_letter
            previous_letter = next_letter
    return new_s

def repeatNumTimes(n):
    resultado = []
    for n_order in range(1, n+1):
        for n_times in range(n_order):
            resultado.append(n_order)
    return resultado

def minmax(lst):
    max_element = lst[0]
    element_index = 0
    for next_element in lst[1::]:
        if next_element>max_element:
            max_element=next_element
            element_index +=1
        else:
            continue
    return element_index

def main():
    s=str(input("Insira uma frase: "))
    print(evenThenOdd(s))
    s=str(input("Insira uma frase: "))
    print(removeAdjacentDuplicates(s))
    n = int(input("Insira um número: "))
    print(repeatNumTimes(n))

main()
