import numpy as np
import cirq

def test_multi_seed_mean_is_stable():
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.ry(0.6)(q), cirq.measure(q,key="m"))
    p = (1-np.cos(0.6))/2
    means = []
    for seed in range(5):
        r = cirq.Simulator().run(c,repetitions=2000,seed=seed)
        means.append(np.mean(r.measurements["m"]))
    assert abs(np.mean(means)-p) < 0.02
    assert np.std(means) < 0.02
