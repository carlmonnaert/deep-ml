from math import sqrt
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
	x1, x2 = 1/2 * (trace + sqrt(trace**2 - 4 * det)), 1/2 * (trace - sqrt(trace**2 - 4 * det))
	return [x1, x2]