import numpy as np
import cirq

def test_state_normalization():
    q = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H.on_each(*q), cirq.CNOT(*q))
    state = cirq.Simulator().simulate(c).final_state_vector
    np.testing.assert_allclose(np.vdot(state,state), 1.0, atol=1e-10)

def test_density_matrix_trace_and_hermiticity():
    q = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H(q[0]), cirq.CNOT(*q))
    rho = cirq.DensityMatrixSimulator().simulate(c).final_density_matrix
    np.testing.assert_allclose(np.trace(rho), 1.0, atol=1e-10)
    np.testing.assert_allclose(rho, rho.conj().T, atol=1e-10)
    assert np.min(np.linalg.eigvalsh(rho)) > -1e-10
