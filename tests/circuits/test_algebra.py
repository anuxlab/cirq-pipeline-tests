import cirq

def test_h_squared_is_identity():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.H(q), cirq.H(q))
    assert cirq.has_unitary(c)
    assert cirq.equal_up_to_global_phase(cirq.unitary(c), cirq.unitary(cirq.I(q)))

def test_x_squared_is_identity():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.X(q), cirq.X(q))
    assert cirq.equal_up_to_global_phase(cirq.unitary(c), cirq.unitary(cirq.I(q)))
