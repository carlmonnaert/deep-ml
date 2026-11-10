import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.
    
    Args:
        A: Square matrix as a list of lists
    
    Returns:
        tuple: (L, U) where L is lower triangular with 1s on diagonal,
               U is upper triangular, and A = L @ U
    """
    A = np.asarray(A).astype(float)
    n = A.shape[0]
    U = np.zeros_like(A)
    L = np.eye(n)
    for i in range(n):
        for k in range(i):
            L[i,k] = 1/U[k,k] * (A[i,k] - np.dot(L[i,:k], U[:k,k]))
        for j in range(i,n):
            U[i,j] = A[i,j] - np.dot(L[i,:i], U[:i,j])
    
    return L, U