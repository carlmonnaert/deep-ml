import numpy as np

def check_positive_definite(matrix: list) -> dict:
    """
    Check if a matrix is positive definite and compute its eigenvalues.
    
    Args:
        matrix: A 2D list representing a square matrix
        
    Returns:
        dict with 'is_positive_definite' (bool) and 'eigenvalues' (list of floats sorted ascending)
    """
    matrix = np.asarray(matrix)
    s = np.linalg.eigvals(matrix).real.round(4)
    return {
        'is_positive_definite': bool((s > 1e-10).all()),
        'eigenvalues': sorted(list(s))
    }