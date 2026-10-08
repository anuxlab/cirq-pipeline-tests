import numpy as np
import cirq

def test_bell_state():
    q0,q1 = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H(q0), cirq.CNOT(q0,q1))
    r = cirq.Simulator().simulate(c)
    expected = np.array([1,0,0,1], complex)/np.sqrt(2)
    np.testing.assert_allclose(r.final_state_vector, expected, atol=1e-10)

def test_ghz_state():
    q = cirq.LineQubit.range(3)
    c = cirq.Circuit(cirq.H(q[0]), cirq.CNOT(q[0],q[1]), cirq.CNOT(q[1],q[2]))
    r = cirq.Simulator().simulate(c)
    expected = np.zeros(8, complex); expected[0]=1/np.sqrt(2); expected[7]=1/np.sqrt(2)
    np.testing.assert_allclose(r.final_state_vector, expected, atol=1e-10)
