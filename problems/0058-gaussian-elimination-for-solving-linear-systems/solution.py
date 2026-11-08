import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	U = A.astype(float).copy()
	n = U.shape[0]
	L = np.eye(n)
	for j in range(n):
		i = j
		while i < n and np.isclose(U[i,j],0):
			i+=1
		if i < n:
			U[[i, j]] = U[[j, i]]
			L[[i, j]] = L[[j, i]]
			U[j,:], L[j,:] = U[j,:]/U[j,j], L[j,:]/U[j,j]
			for i in range(j+1, n):
				f = U[i, j]
				U[i] -= f * U[j]
				L[i] -= f * L[j]
	x = np.zeros(n)
	V = U-np.eye(n)
	# SOLVE Ux = Lb with U upper and L lower triangular.
	# Notice that U has ones on diagonal
	# We solve (V+I)x = Lb <=> x = Lb - Vx
	# Where V is stricly upper triangular 
	for i in range(n-1, -1, -1):
		x[i] = (L@b - V@x)[i]
	return x