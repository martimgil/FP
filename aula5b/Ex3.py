def matrows(M):
    return len(M)

# Complete para devolver o número de colunas da matriz M.
def matcols(M):
    return len(M[0])

# Complete a função para devolver uma matriz com m×n zeros.
def matzeros(m, n):
    M = n * [0]
    M1=[]
    for i in  range(m):
        M1.append(M)
        M = M1
    return M

def matzerosTEST(m, n):
    M = matzeros(m, n)
    M[0][1] = 1   # should change just 1 element!
    return M

# Complete a função para multiplicar a matriz A pela matriz B.
def matmult(A, B):
    assert matcols(A) == matrows(B)
    C = matzeros(matrows(A), matcols(B))
    for i in range(matrows(A)):
        for j in range(matcols(B)):
            for k in range(matcols(A)):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matmultTEST(A, B):
    C = matmult(A, B)
    return A, B, C

def matmultTEST(A, B):
    C = matmult(A, B)
    return A, B, C


A, B, C = matmultTEST([[1, 0], [2, 3]], [[4, 5], [0, 6]])
print("Matriz A:", A)
print("Matriz B:", B)
print("Resultado (A x B):", C)