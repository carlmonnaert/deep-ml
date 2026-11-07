import numpy as np
def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	values = np.asarray([i for i in range(1, n+1)])
	probs = np.asarray([1/n for i in range(n)])
	mu = np.sum(values*probs)
	sigma2 = np.sum((values**2) * probs) - mu**2
	return mu, sigma2