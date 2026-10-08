import numpy as np
import cirq

def purity(rho):
    return np.real(np.trace(rho @ rho))

def test_bell_reduced_state_is_mixed():
    q0,q1 = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H(q0), cirq.CNOT(q0,q1))
    rho = cirq.DensityMatrixSimulator().simulate(c).final_density_matrix
    # Partial trace q1 for 2-qubit density matrix.
    reduced = np.trace(rho.reshape(2,2,2,2), axis1=1, axis2=3)
    np.testing.assert_allclose(reduced, np.eye(2)/2, atol=1e-10)
    np.testing.assert_allclose(purity(reduced), 0.5, atol=1e-10)
