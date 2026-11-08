import numpy as np

def calculate_correlation_matrix(X, Y=None):
	X = np.asarray(X).astype(float)
	X = X - np.mean(X, axis=0, keepdims=True)
	cxx = X.T@X / float(len(X))
	dx = np.diag(cxx)
	if Y is not None:
		Y = np.asarray(Y).astype(float)
		Y = Y - np.mean(Y, axis=0, keepdims=True)
		cyy = Y.T@Y / float(len(Y))
		dy = np.diag(cyy)

		cxy = X.T@Y / float(len(X))
		return cxy/np.sqrt(dx[:,None]@dy[None,:])
	return cxx / np.sqrt(dx[:,None]@dx[None,:])