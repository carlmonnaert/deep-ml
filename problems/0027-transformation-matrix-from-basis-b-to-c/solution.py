def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	import numpy as np
	return np.linalg.inv(C)@B