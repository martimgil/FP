def factorial(n):
    assert isinstance(n, int), "n should be an int"
    assert n >= 0            , "n should not be negative"
    # Complete aqui
    s=("{}! = ".format(n))
    c=1
    for a in range(n,0,-1):
        s+=" {}".format(a)
        c=c*a
        if a==1:
            s+=" = {}".format(c)
        else:
            s+=" x"
    print(s)
    return c
factorial(1)