def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	def mean(l):
		if l:
			acc = 0
			for x in l:
				acc += x
			return acc/len(l)
		else:
			return 0

	if mode == 'row':
		return [ mean(l) for l in matrix ]
	elif mode == 'column':
		m_T = [ [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
		return [ mean(l) for l in m_T ]
	else:
		return []