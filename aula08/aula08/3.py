def primesUpTo(n):
    lst = [a for a in range(2, n)]
    for b in lst:
        for a in lst:
            if a%b==0 and a>b:
                lst.remove(a)
    print(lst)

primesUpTo(10)