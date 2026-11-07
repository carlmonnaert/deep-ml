def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	return [x + y for x,y in zip(a,b)] if len(a)==len(b) else -1