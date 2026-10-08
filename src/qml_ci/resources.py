import cirq

def circuit_metrics(circuit):
    return {
        "qubits": len(circuit.all_qubits()),
        "moments": len(circuit),
        "operations": sum(1 for _ in circuit.all_operations()),
        "depth": len(circuit),
    }

def assert_resource_budget(circuit, max_qubits=8, max_moments=100, max_operations=500):
    m = circuit_metrics(circuit)
    assert m["qubits"] <= max_qubits
    assert m["moments"] <= max_moments
    assert m["operations"] <= max_operations
