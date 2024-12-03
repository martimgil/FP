def isPrime(n):
    for i in range(2,100):
        v = n%i
        if v==0:
            if n==i:
                continue
            else:
                return False
        else:
            return True

print(isPrime(7))