import cirq
from qml_ci.serialization import roundtrip_circuit

def test_circuit_json_roundtrip():
    q = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H(q[0]), cirq.CNOT(q[0], q[1]))
    restored = roundtrip_circuit(c)
    cirq.testing.assert_allclose_up_to_global_phase(
        cirq.unitary(c), cirq.unitary(restored), atol=1e-10
    )
