def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    if len(a) == 0:
        return []
    m,n = len(a), len(a[0])
    return [[a[i][j] for i in range(m)] for j in range(n)]