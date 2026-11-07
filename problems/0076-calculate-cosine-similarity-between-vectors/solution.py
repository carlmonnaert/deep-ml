import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	v1v2 = np.dot(v1, v2)
	n1, n2 = np.linalg.norm(v1, ord=2), np.linalg.norm(v2, ord=2)
	return float(v1v2 / (n1 * n2))