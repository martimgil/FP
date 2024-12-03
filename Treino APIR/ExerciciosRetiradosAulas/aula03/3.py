def max2(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2

def max3(n1,n2,n3):
    max1 = max2(n1,n2)
    max4 = max2(max1, n3)
    return max4