import numpy as np
import cirq
from qml_ci.observables import expectation_z

def test_z_expectation_zero():
    q = cirq.LineQubit(0)
    state = cirq.Simulator().simulate(cirq.Circuit(cirq.X(q))).final_state_vector
    np.testing.assert_allclose(expectation_z(state), -1.0, atol=1e-10)

def test_z_expectation_plus_state():
    q = cirq.LineQubit(0)
    state = cirq.Simulator().simulate(cirq.Circuit(cirq.H(q))).final_state_vector
    np.testing.assert_allclose(expectation_z(state), 0.0, atol=1e-10)
