def fibonacci(n):
    f1 = 0
    f2 = 1
    for i in range(2,n):
        f = f1 + f2
        f1 = f2
        f2 = f

    return f2

print(fibonacci(5))