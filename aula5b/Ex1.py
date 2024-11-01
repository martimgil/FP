def getFibonacci(n):
    assert n>=2
    s=[0,1]
    for i in range(2,n):
        a = (s[(i-2)] + s[(i-1)])
        s.append(a)
    return s
print(getFibonacci(3))