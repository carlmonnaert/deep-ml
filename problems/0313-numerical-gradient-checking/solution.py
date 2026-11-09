import numpy as np
def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    dx = epsilon*np.eye(len(x))
    grad = np.asarray([(f(x+dx[:,i])-f(x))/epsilon for i in range(len(x))])
    return grad, np.linalg.norm(grad - analytical_grad) / (np.linalg.norm(grad) + np.linalg.norm(analytical_grad))