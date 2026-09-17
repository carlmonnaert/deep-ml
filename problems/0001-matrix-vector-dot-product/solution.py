def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if a and a[0] :
		n,m = len(a), len(a[0])
	k = len(b)
	if m != k:
		return -1
	else:
		return [ sum([ a[i][j] * b[j] for j in range(m)]) for i in range(n)]