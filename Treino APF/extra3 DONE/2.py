def a(n,k):
    if k==0:
        return 1
    elif 0<k<=n:
        return n*a(n-1,k-1)

print(a(2,1))
print(a(5,2))
print(a(5,3))
print(a(10,3))
