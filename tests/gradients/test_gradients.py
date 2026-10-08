import numpy as np
from qml_ci.algorithms import qnn_forward, finite_difference, parameter_shift

def test_parameter_shift_matches_finite_difference():
    fn = lambda x: qnn_forward(x, 0.37)
    ps = parameter_shift(fn, 0.21)
    fd = finite_difference(fn, 0.21, 1e-5)
    np.testing.assert_allclose(ps, fd, atol=1e-4)

def test_gradient_is_finite():
    fn = lambda x: qnn_forward(x, 0.37)
    assert np.isfinite(parameter_shift(fn, 0.21))
