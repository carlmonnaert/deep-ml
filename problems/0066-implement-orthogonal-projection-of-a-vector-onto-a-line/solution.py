
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	import numpy as np
	v, L = np.asarray(v), np.asarray(L)
	return np.dot(v,L)/np.dot(L,L) * L
