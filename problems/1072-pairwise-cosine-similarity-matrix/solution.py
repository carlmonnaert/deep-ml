import numpy as np

def pairwise_cosine_similarity(X):
    X = np.asarray(X)
    X = X/np.sqrt(np.sum(X**2, axis=1, keepdims=True)+1e-12)
    return X@X.T