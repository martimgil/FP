def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def main():
    for a in range(1,100):
        print(a, isPrime(a))
main()