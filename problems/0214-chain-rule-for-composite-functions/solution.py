import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	name_fun_map = {'sin': lambda u: np.sin(u),
					'square': lambda u: u**2,
					'exp': lambda u: np.exp(u),
					'log': lambda u: np.log(u)}
	name_deriv_map = {'sin': lambda u: np.cos(u),
					'square': lambda u: 2*u,
					'exp': lambda u: np.exp(u),
					'log': lambda u: 1/u}
	res = 1
	y=x
	for f in functions[::-1]:
		fx = name_fun_map[f](y)
		fpx = name_deriv_map[f](y)
		res = res*fpx
		y = fx
	return res

		