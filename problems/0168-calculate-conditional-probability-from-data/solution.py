def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    import numpy as np
    data = np.asarray(data)
    n = len(data)
    px = np.sum(data[:,0]==x)
    pxy = np.sum( (data[:,0]==x) & (data[:,1]==y) )
    return pxy/px if px else 0