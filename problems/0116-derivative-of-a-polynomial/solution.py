def poly_term_derivative(c: float, x: float, n: float) -> float:
    return n * c * x**(n-1) if n > 0 else 0