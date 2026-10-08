import cirq

def test_h_squared_is_identity():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.H(q), cirq.H(q))
    cirq.testing.assert_allclose_up_to_global_phase(
        cirq.unitary(c), cirq.unitary(cirq.I(q)), atol=1e-10
    )

def test_x_squared_is_identity():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.X(q), cirq.X(q))
    cirq.testing.assert_allclose_up_to_global_phase(
        cirq.unitary(c), cirq.unitary(cirq.I(q)), atol=1e-10
    )
