def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fn1 = 1
    fn2 = 0
    for i in range(2, n + 1):
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn
    return fn

def main():
    n = int(input("n: "))
    print(fibonacci(n))

main()