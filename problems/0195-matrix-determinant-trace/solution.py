def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	import numpy as np
	matrix = np.asarray(matrix)
	trace = np.trace(matrix)
	det = np.linalg.det(matrix)
	return det, trace