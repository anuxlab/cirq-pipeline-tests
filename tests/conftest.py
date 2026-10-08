import numpy as np
import pytest
import cirq

@pytest.fixture
def simulator():
    return cirq.Simulator()

@pytest.fixture
def seeded_rng():
    return np.random.default_rng(42)

@pytest.fixture
def two_qubits():
    return cirq.LineQubit.range(2)
