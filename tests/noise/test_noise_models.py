import numpy as np
import cirq

def test_depolarizing_moves_state_toward_mixed():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.X(q), cirq.depolarize(0.8).on(q))
    rho = cirq.DensityMatrixSimulator().simulate(c).final_density_matrix
    assert np.trace(rho @ rho).real < 1.0

def test_bit_flip_changes_zero_state():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.bit_flip(1.0).on(q))
    state = cirq.DensityMatrixSimulator().simulate(c).final_density_matrix
    expected = np.array([[0,0],[0,1]], complex)
    np.testing.assert_allclose(state, expected, atol=1e-10)

def test_phase_flip_preserves_measurement_probabilities():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.H(q), cirq.phase_flip(1.0).on(q))
    state = cirq.DensityMatrixSimulator().simulate(c).final_density_matrix
    np.testing.assert_allclose(np.real(np.diag(state)), [0.5,0.5], atol=1e-10)

def test_amplitude_damping_drives_one_to_zero():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.X(q), cirq.amplitude_damp(1.0).on(q))
    rho = cirq.DensityMatrixSimulator().simulate(c).final_density_matrix
    np.testing.assert_allclose(rho, np.array([[1,0],[0,0]], complex), atol=1e-10)
