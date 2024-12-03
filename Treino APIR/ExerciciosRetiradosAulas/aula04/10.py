def isPrime(n):
    for a in range(2, n):
        if a!=n and a!=1:
            v = n%a
            if v==0:
                return False
    return True

c = isPrime(6)
print(c)
