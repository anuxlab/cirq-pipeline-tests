import numpy as np
import cirq
import pytest
from qml_ci.encoding import angle_encoding, amplitude_encoding, z_feature_map


def test_angle_encoding_uses_all_features():
    q = cirq.LineQubit.range(3)
    c = angle_encoding([.1, .2, .3], q)
    assert len(list(c.all_operations())) == 3


def test_amplitude_encoding_normalizes():
    q = cirq.LineQubit.range(2)
    c = amplitude_encoding([1, 2, 3, 4], q)
    rho = cirq.DensityMatrixSimulator().simulate(c).final_density_matrix
    np.testing.assert_allclose(np.trace(rho), 1.0, atol=1e-10)
    expected = np.outer(
        np.array([1, 2, 3, 4], dtype=complex) / np.sqrt(30),
        np.array([1, 2, 3, 4], dtype=complex).conj() / np.sqrt(30),
    )
    np.testing.assert_allclose(rho, expected, atol=1e-8)


def test_feature_map_is_unitary():
    q = cirq.LineQubit.range(2)
    c = z_feature_map([.2, .4], q)
    assert cirq.has_unitary(c)


@pytest.mark.parametrize("bad", [[np.nan], [np.inf]])
def test_encoding_rejects_nonfinite(bad):
    with pytest.raises(ValueError):
        angle_encoding(bad, cirq.LineQubit.range(len(bad)))


def test_amplitude_dimension_validation():
    with pytest.raises(ValueError):
        amplitude_encoding([1, 2, 3], cirq.LineQubit.range(2))
