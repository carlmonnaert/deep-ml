def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	n,m = len(f(x)), len(x)
	res = [[0 for j in range(m)] for i in range(n)]
	f_x = f(x)
	for j in range(m):
		x_p_h = [x[k] + (h if k == j else float(0)) for k in range(m)]
		f_x_p_dx = f(x_p_h)
		for i in range(n):
			res[i][j] = (f_x_p_dx[i]-f_x[i])/h
	return res
