def Fibonnaci(n):
    lst=[0,1]
    for i in range(2,n):
        lst.append(lst[i-2]+lst[i-1])
    return lst[len(lst)-1]

print(Fibonnaci(10))