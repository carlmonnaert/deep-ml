import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    d_g, d_h = len(g_coeffs), len(h_coeffs)
    g_x = sum( [x**(d_g-1-i) * g_coeffs[i] for i in range(d_g)] )
    h_x = sum( [x**(d_h-1-i) * h_coeffs[i] for i in range(d_h)] )
    gp_x = sum( [(d_g-1-i) * x**(d_g-2-i) * g_coeffs[i] for i in range(d_g-1)] )
    hp_x = sum( [(d_h-1-i) * x**(d_h-2-i) * h_coeffs[i] for i in range(d_h-1)] )
    return (gp_x * h_x - g_x * hp_x) / (h_x ** 2)
