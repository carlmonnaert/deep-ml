import numpy as np

def cross_product(a, b):
    c = np.array([a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1) % 3] for i in range(3)])
    return c