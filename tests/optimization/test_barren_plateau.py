import numpy as np
import cirq
import pytest

@pytest.mark.nightly
def test_gradient_variance_is_measurable():
    q = cirq.LineQubit(0)
    sim = cirq.Simulator()
    vals = []
    for seed in range(20):
        rng = np.random.default_rng(seed)
        theta = rng.uniform(-np.pi,np.pi)
        def f(x):
            return np.cos(x)
        vals.append((f(theta+np.pi/2)-f(theta-np.pi/2))/2)
    stats = np.var(vals)
    assert np.isfinite(stats)
    # Diagnostic guard: a healthy one-qubit benchmark should not have exactly zero variance.
    assert stats > 1e-6
