def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    import numpy as np
    matrix = np.asarray(matrix)
    t = np.trace(matrix)
    d = np.linalg.det(matrix)
    # Eighenvalues are solutions to X^2 - tX + d = 0
    delta = t**2 - 4*d
    if delta > 0:
        l1 = 0.5*(t + np.sqrt(delta))
        l2 = 0.5*(t - np.sqrt(delta))
    else:
        l1 = 0.5*(t + (0+1.j)* np.sqrt(delta))
        l2 = 0.5*(t - (0+1.j)*np.sqrt(delta))
    return [l1, l2]