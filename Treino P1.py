# Devolve o número de linhas da matriz M.
def matrows(M):
    return len(M)

# Complete para devolver o número de colunas da matriz M.
def matcols(M):
    return len(M[0])

# Complete a função para devolver uma matriz com m×n zeros.
def matzeros(m, n):
    lst = []
    for a in range(m):
        b = []
        for d in range(n):
            b.append(0)
        lst.append(b)
    return lst

def matzerosTEST(m, n):
    M = matzeros(m, n)
    M[0][1] = 1   # should change just 1 element!
    return M

# Complete a função para multiplicar a matriz A pela matriz B.
def matmult(A, B):
    assert matcols(A) == matrows(B)
    C = matzeros(matrows(A), matcols(B))

    for line1 in range(matrows(A)):
        for col1 in range(matcols(B)):
            for col2 in range(matcols(A)):
                C[line1][col1]+=A[line1][col2]*B[col2][col1]



    return C

def matmultTEST(A, B):
    C = matmult(A, B)
    return A, B, C