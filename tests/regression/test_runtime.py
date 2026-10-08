import time
import cirq

def test_small_simulation_runtime():
    q = cirq.LineQubit.range(4)
    c = cirq.Circuit(cirq.H.on_each(*q))
    start = time.perf_counter()
    cirq.Simulator().simulate(c)
    elapsed = time.perf_counter()-start
    assert elapsed < 2.0
