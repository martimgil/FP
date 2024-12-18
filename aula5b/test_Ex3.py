def matzeros(m, n):
    M = n * [0]
    M1=[]
    for i in  range(m):
        M1.append(M)
    M = M1
    return M
print(matzeros(2,5))