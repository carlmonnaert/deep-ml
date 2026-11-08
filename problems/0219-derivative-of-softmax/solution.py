def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	import numpy as np
	x = np.asarray(x)
	m = np.max(x)
	x -= m
	e = np.exp(x)
	s = np.sum(e)
	J = np.diag(e/s)- e[:,None] @ e[None,:] / s**2
	return J