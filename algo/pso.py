import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    "Objective function"
    return (x - 3.19) ** 2 + (y - 0.9) ** 2 + np.sin(3 * x + 1.6) + np.sin(4 * y - 1.3)


def update(V, X, pbest, pbest_obj, gbest, gbest_obj, c1, c2, w):
    "Function to do one iteration of particle swarm optimization"
    # Update params
    r1, r2 = np.random.rand(2)
    V = w * V + c1 * r1 * (pbest - X) + c2 * r2 * (gbest.reshape(-1, 1) - X)
    X = X + V
    obj = f(X[0], X[1])
    pbest[:, (pbest_obj >= obj)] = X[:, (pbest_obj >= obj)]
    pbest_obj = np.array([pbest_obj, obj]).min(axis=0)
    gbest = pbest[:, pbest_obj.argmin()]
    gbest_obj = pbest_obj.min()
    return V, X, pbest, pbest_obj, gbest, gbest_obj
