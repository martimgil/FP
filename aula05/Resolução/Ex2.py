a=[]
v=5

def inputFloatList():
    
    while True:
        n=(input("N: "))
        
        if n=="":
            print(a)
            break
        else:
            n=int(n)
            a.append(n)
def countLower():
    s=0
    v=5
    for i in range(len(a)):
        if a[i]<v:
            s+=1
    print(s)

def minmax(lst):
    max=lst[0]
    min=lst[0]
    for  num in lst:
        if num<=max:
            max = max
        elif num>max:
            max=num
        if num<=min:
            min=num
        elif num>min:
            continue
    return min, max


def final():
    inputFloatList()
    min, max = minmax(a)
    print(a)
    media = (min+max)/2
    count=0
    for number in a:
        if media>number:
            count+=1
        else:
            continue
    print(f"São maiores {count} elementos")

final()








valores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
minimo, maximo = minmax(valores)