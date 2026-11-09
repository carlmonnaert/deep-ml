import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    # Compute U by diagonalising A@A.T
    AAT = A @ A.T
    d = np.linalg.det(AAT)
    t = np.trace(AAT)
    b, c = -t, d
    delta = b**2 - 4*c

    # Computing the singular values
    l1, l2 = 0.5*(-b-np.sqrt(delta)), 0.5*(-b+np.sqrt(delta))
    s = np.asarray([l1, l2])

    # Solving for left singular vectors
    a, b = AAT[0]
    c, d = AAT[1]
    u1= np.asarray([b, l1 - a])
    u2= np.asarray([l2 - d, c])

    # Building U orthogonal
    u1 = u1/np.linalg.norm(u1)
    u2 = np.asarray([-u1[1], u1[0]])
    U = np.stack((u1,u2)).T

    # Solving for right singular vectors
    s = np.sqrt(s)
    v1 = A.T @ u1 / s[0]
    v2 = A.T @ u2 / s[1]
    V = np.stack((v1, v2))

    return U, s, V

    