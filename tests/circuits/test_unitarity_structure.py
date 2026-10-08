import numpy as np
import cirq


def ansatz(qubits, params):
    c = cirq.Circuit()
    n = len(qubits)
    for i, q in enumerate(qubits):
        c.append(cirq.ry(float(params[i]))(q))
    for i in range(n - 1):
        c.append(cirq.CNOT(qubits[i], qubits[i + 1]))
    for i, q in enumerate(qubits):
        c.append(cirq.rz(float(params[n + i]))(q))
    return c


def test_ansatz_unitary():
    q = cirq.LineQubit.range(2)
    c = ansatz(q, [0.1, 0.2, 0.3, 0.4])
    U = cirq.unitary(c)
    np.testing.assert_allclose(U.conj().T @ U, np.eye(4), atol=1e-10)


def test_structure_and_parameter_count():
    q = cirq.LineQubit.range(3)
    c = ansatz(q, np.zeros(6))
    assert len(c.all_qubits()) == 3

    operations = list(c.all_operations())
    assert sum(isinstance(op.gate, cirq.ops.common_gates.Ry) for op in operations) == 3
    assert sum(isinstance(op.gate, cirq.ops.common_gates.Rz) for op in operations) == 3
    assert sum(isinstance(op.gate, cirq.CNotPowGate) for op in operations) == 2

    # Cirq is free to schedule non-overlapping operations into the same
    # moment; therefore moment count is intentionally not asserted.
    assert len(operations) == 8
