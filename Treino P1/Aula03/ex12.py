def countdown(n):
    if n>= 0:
        print(n)
        n-=1
    return countdown(n)
n=30
countdown(n)