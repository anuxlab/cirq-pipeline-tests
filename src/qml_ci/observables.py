import numpy as np
import cirq

def expectation_z(state, qubit_index=0):
    state = np.asarray(state, dtype=complex).reshape(-1)
    n = int(np.log2(len(state)))
    if 2**n != len(state):
        raise ValueError("state length must be a power of two")
    result = 0.0
    for basis, amp in enumerate(state):
        bit = (basis >> (n - 1 - qubit_index)) & 1
        result += (1 if bit == 0 else -1) * abs(amp)**2
    return float(np.real(result))

def pauli_z_string(qubits, indices):
    op = cirq.I
    for i in indices:
        op = op * cirq.Z(qubits[i])
    return op
