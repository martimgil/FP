def mdc(a,b):
    r = a%b
    if r==0:
        return b
    else:
        mdc(b,r)