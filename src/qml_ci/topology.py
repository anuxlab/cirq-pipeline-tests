import cirq

def assert_two_qubit_connectivity(circuit, allowed_pairs):
    allowed = {frozenset(p) for p in allowed_pairs}
    for op in circuit.all_operations():
        if len(op.qubits) == 2:
            pair = frozenset(op.qubits)
            if pair not in allowed:
                raise AssertionError(f"unsupported edge: {pair}")

def linear_device(n):
    qubits = cirq.LineQubit.range(n)
    return qubits, {(qubits[i], qubits[i+1]) for i in range(n-1)}
