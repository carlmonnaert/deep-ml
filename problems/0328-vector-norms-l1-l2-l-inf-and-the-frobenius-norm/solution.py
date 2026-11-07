import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    arr = np.asarray(arr)
    d = arr.ndim
    if norm_type in ["l1", "l2", "linf"] and d in [1,2]:
        a = abs(arr)
        if norm_type == "l1":
            return float(np.sum(abs(a)))
        if norm_type == "l2":
            return float(np.sqrt(np.sum(a**2)))
        if norm_type == "linf":
            return float(np.max(a)) 
    
    if norm_type == "frobenius" and d == 2:
        return float(np.sqrt(np.trace(arr.T @ arr)))
    
    raise ValueError('ValueError')