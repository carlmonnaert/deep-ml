import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	n , m = new_shape
	if n*m != len(a[0])*len(a):
		return []
	try:
		flattened = [ a[ i // len(a[0]) ][i % len(a[0])] for i in range(len(a) * len(a[0])) ]
		m = [ [flattened[i*m + j] for j in range(m)] for i in range(n) ]
	except IndexError :
		m = []
	return m