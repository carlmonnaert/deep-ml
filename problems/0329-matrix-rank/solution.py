import numpy as np
def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    m,n = A.shape
    if m < n:
        A = A.T
        m,n = n,m
    for j in range(n):
        i = j
        while i < m and np.isclose(A[i,j],0, tol):
            i+=1
        if i < n:
            A[i,:], A[j,:] = A[j,:], A[i,:]
            for i in range(j+1, min(n,m)):
                A[i, :] = A[i, :] - A[i,j]/A[j,j] * A[j, :]
    rank = sum([1 if np.isclose(A[i,i],0,tol) == False else 0 for i in range(min(n,m))])
    return rank