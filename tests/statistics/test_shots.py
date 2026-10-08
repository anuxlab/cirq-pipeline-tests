import numpy as np
import cirq

def test_hadamard_shot_probability():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.H(q), cirq.measure(q,key="m"))
    r = cirq.Simulator().run(c,repetitions=10000,seed=8)
    p1 = np.mean(r.measurements["m"][:,0])
    assert abs(p1-0.5) < 0.03

def test_shot_convergence():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.ry(0.4)(q), cirq.measure(q,key="m"))
    r1 = cirq.Simulator().run(c,repetitions=100,seed=9)
    r2 = cirq.Simulator().run(c,repetitions=10000,seed=10)
    p = (1-np.cos(0.4))/2
    assert abs(np.mean(r2.measurements["m"])-p) < 0.03
