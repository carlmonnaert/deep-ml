def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	n, m = len(a), len(a[0])
	mb = len(b)
	if m != mb:
		return -1
	return [sum([a[i][k] * b[k] for k in range(m)]) for i in range(len(a))]
