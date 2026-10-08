import time
import cirq

def benchmark():
    q = cirq.LineQubit.range(6)
    c = cirq.Circuit()
    for _ in range(10):
        c.append(cirq.H.on_each(*q))
        c.append(cirq.CNOT(q[0],q[1]))
        c.append(cirq.CNOT(q[1],q[2]))
        c.append(cirq.CNOT(q[2],q[3]))
        c.append(cirq.CNOT(q[3],q[4]))
        c.append(cirq.CNOT(q[4],q[5]))
    start=time.perf_counter()
    cirq.Simulator().simulate(c)
    return {"seconds": time.perf_counter()-start, "moments": len(c)}

if __name__ == "__main__":
    print(benchmark())
