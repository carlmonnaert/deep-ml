import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    A = np.asarray(A).astype(float)
    # Compute the positive matrix
    B = A.T @ A

    # Find rotation matrix
    theta = np.pi/4 if np.isclose(B[1,1], B[0,0]) else 0.5*np.arctan(2*B[0,1]/(B[0,0]-B[1,1]))
    R = np.array(
        [ [np.cos(theta), -np.sin(theta)],
          [np.sin(theta), np.cos(theta)] ])

    # Extract singular singular values
    D = R.T@A.T@A@R
    d = np.sqrt(np.diag(D))
    idx = np.argsort(d)[::-1]
    s, R = d[idx], R[:, idx]

    # Computing U
    U = A@R@np.diag(1/s)

    return U, s , R.T
