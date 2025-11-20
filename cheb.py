import numpy as np

def chebyshev(degree, domain):
    a,b = (domain[0] + domain[1]) / 2, (domain[1] - domain[0]) / 2
    chebyshev_nodes = [a + b * np.cos((2*k + 1) * np.pi / (2 * (degree + 1))) for k in range(degree + 1)]
    return chebyshev_nodes