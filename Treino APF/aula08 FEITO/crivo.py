def primesUpTo(n):
    c = set(range(2,n+1))
    for i in range(2, n+1):
        a=2
        d = i*a
        while d<=n:
            if d in c:
                c.remove(d)
            d = i*a
            a+=1

    return c


def main():
    n = int(input(""))
    print(primesUpTo(n))

main()