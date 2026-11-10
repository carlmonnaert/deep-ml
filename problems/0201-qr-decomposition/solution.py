import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    """
    Perform QR decomposition using Gram-Schmidt process.
    
    Args:
        A: An m x n matrix represented as list of lists
    
    Returns:
        Tuple of (Q, R) where Q is orthogonal and R is upper triangular
    """
    A = np.asarray(A).astype(float)
    Q = A.copy()
    m,n = Q.shape
    V = np.zeros_like(A)
    for i in range(n):
        coefficients = np.asarray([np.dot(Q[:,i], Q[:,j]) for j in range(i)])
        vecs = np.asarray([Q[:,j] for j in range(i)])
        to_sub_q = coefficients @ vecs
        V[:,i] = Q[:,i] - to_sub_q
        Q[:,i] = V[:,i]/np.linalg.norm(V[:,i])

    R = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i < j:
                R[i,j] = np.dot(Q[:,i].T,A[:,j])
            elif i==j:
                R[i,j] = np.linalg.norm(V[:,i])
            else:
                R[i,j] = 0
    return Q,R