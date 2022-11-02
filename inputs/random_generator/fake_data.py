import numpy as np

# Create particles
def create_particles():
    n_particles = 40
    np.random.seed(100)
    X = np.random.rand(2, n_particles) * 5
    V = np.random.randn(2, n_particles) * 0.1
    return X, V


# Hyper-parameter of the algorithm
def create_hyper_parameters():
    c1 = c2 = 0.1
    w = 0.2
    return c1, c2, w
