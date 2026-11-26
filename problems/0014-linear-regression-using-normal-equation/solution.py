import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    Xt = X.T

    theta = np.linalg.solve(Xt @ X, Xt @ y)

    return np.round(theta, 4).tolist()