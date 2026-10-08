import pytest
import cirq
from qml_ci.topology import assert_two_qubit_connectivity, linear_device

def test_linear_topology_accepts_adjacent_cnot():
    q, edges = linear_device(3)
    c = cirq.Circuit(cirq.CNOT(q[0],q[1]), cirq.CNOT(q[1],q[2]))
    assert_two_qubit_connectivity(c, edges)

def test_linear_topology_rejects_nonadjacent_cnot():
    q, edges = linear_device(3)
    c = cirq.Circuit(cirq.CNOT(q[0],q[2]))
    with pytest.raises(AssertionError):
        assert_two_qubit_connectivity(c, edges)

@pytest.mark.hardware
def test_hardware_placeholder():
    # Real backend credentials and backend selection belong here in deployment-specific code.
    assert True
