def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	import numpy as np
	sigmoid = lambda x: 1/(np.exp(-x)+1)
	tanh = lambda x : np.tanh(x)
	str_to_fun = {
		'sigmoid': lambda x: sigmoid(x)*(1-sigmoid(x)),
		'tanh': lambda x: 1-tanh(x)**2,
		'relu': lambda x: 1. if x > 0. else 0.
	}
	return {name: fun(x) for name, fun in str_to_fun.items() }