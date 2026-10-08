import cirq
from qml_ci.resources import circuit_metrics, assert_resource_budget

def test_resource_metrics():
    q = cirq.LineQubit.range(3)
    c = cirq.Circuit(cirq.H.on_each(*q))
    m = circuit_metrics(c)
    assert m["qubits"] == 3
    assert m["operations"] == 3

def test_resource_budget():
    q = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H.on_each(*q))
    assert_resource_budget(c, max_qubits=2)
