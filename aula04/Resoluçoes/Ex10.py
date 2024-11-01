def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    for num in range(1, 101):
        if isPrime(num):
            print(f"{num} é primo")
        else:
            print(f"{num} não é primo")

main()


