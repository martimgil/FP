def findRise(lst):
    a = []
    for i in range(len(lst)):
        if lst[i]>lst[i-1]:
            a.append(i)
    return a

print(findRise([1,3,2,4,5]))