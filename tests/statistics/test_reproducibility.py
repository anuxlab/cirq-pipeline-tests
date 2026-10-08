import numpy as np
import cirq

def test_seed_reproducibility():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.H(q), cirq.measure(q,key="m"))
    a = cirq.Simulator().run(c,repetitions=1000,seed=42).measurements["m"]
    b = cirq.Simulator().run(c,repetitions=1000,seed=42).measurements["m"]
    np.testing.assert_array_equal(a,b)
