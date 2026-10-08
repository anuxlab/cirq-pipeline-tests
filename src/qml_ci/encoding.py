import numpy as np
import cirq

def validate_features(x, expected_dim=None):
    x = np.asarray(x, dtype=float)
    if x.ndim != 1:
        raise ValueError("features must be one-dimensional")
    if not np.all(np.isfinite(x)):
        raise ValueError("features must be finite")
    if expected_dim is not None and len(x) != expected_dim:
        raise ValueError("feature dimension mismatch")
    return x

def angle_encoding(x, qubits):
    x = validate_features(x, len(qubits))
    return cirq.Circuit(cirq.ry(float(v))(q) for v, q in zip(x, qubits))

def amplitude_encoding(x, qubits):
    x = validate_features(x)
    n = 2 ** len(qubits)
    if len(x) != n:
        raise ValueError(f"amplitude vector must have length {n}")
    norm = np.linalg.norm(x)
    if norm == 0:
        raise ValueError("zero vector cannot be amplitude encoded")
    state = x / norm
    return cirq.StatePreparationChannel(state).on(*qubits)

def z_feature_map(x, qubits):
    x = validate_features(x, len(qubits))
    c = cirq.Circuit()
    for v, q in zip(x, qubits):
        c.append(cirq.H(q))
        c.append(cirq.rz(float(v))(q))
    return c
