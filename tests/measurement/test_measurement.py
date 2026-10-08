import numpy as np
import cirq

def test_deterministic_zero_measurement():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.measure(q, key="m"))
    counts = cirq.Simulator().run(c, repetitions=200, seed=3).histogram(key="m")
    assert counts.get(0,0) == 200

def test_bell_measurements_are_correlated():
    q0,q1 = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H(q0), cirq.CNOT(q0,q1), cirq.measure(q0,q1,key="m"))
    samples = cirq.Simulator().run(c, repetitions=2000, seed=4).measurements["m"]
    assert np.all(samples[:,0] == samples[:,1])
