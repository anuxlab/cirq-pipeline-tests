import numpy as np
from scipy.optimize import minimize

def test_optimizer_improves_quadratic():
    f = lambda x: float((x[0]-2.0)**2)
    initial = f([5.0])
    result = minimize(f, [5.0], method="BFGS")
    assert result.fun < initial
    assert result.fun < 1e-8
