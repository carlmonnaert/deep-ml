import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	sigmoid = lambda x: 1/(1+np.exp(-x))
	w = initial_weights
	b = initial_bias
	mse_values = []
	for epoch in range(epochs):
		z = features @ w + b
		y_pred = sigmoid(z)
		mse = np.round(np.mean((y_pred - labels)**2),4)
		mse_values.append(mse)
		dL_dy_pred = 2.*(y_pred-labels)
		dy_pred_dz = y_pred*(1-y_pred)
		dz_dw = features.T
		dz_db = 1.
		dL_dw = dz_dw * dy_pred_dz * dL_dy_pred
		dL_db = dz_db * dy_pred_dz * dL_dy_pred
		w -= learning_rate * np.mean(dL_dw, axis=1)
		b -= learning_rate * np.mean(dL_db)

	return np.round(w,4), np.round(b,4), mse_values