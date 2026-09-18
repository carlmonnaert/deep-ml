import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	d = np.diag(A)
	D = np.diag(d)
	M = A - D
	D_inv = np.linalg.inv(D)
	x = np.zeros_like(b)
	for i in range(n):
		x = D_inv @ (b - M @ x)
	return x