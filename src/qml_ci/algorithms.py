import numpy as np
import cirq
from scipy.optimize import minimize
from sklearn.svm import SVC
from .encoding import angle_encoding
from .observables import expectation_z

def single_qubit_variational_state(theta):
    q = cirq.LineQubit(0)
    return cirq.Circuit(cirq.ry(float(theta))(q)), q

def vqe_energy(theta, simulator=None):
    simulator = simulator or cirq.Simulator()
    c, q = single_qubit_variational_state(theta)
    r = simulator.simulate(c)
    # H = Z. Ground energy is -1.
    return expectation_z(r.final_state_vector, 0)

def run_vqe(initial=1.2):
    result = minimize(lambda x: vqe_energy(float(x[0])), [initial], method="BFGS")
    return result

def qaoa_maxcut_expectation(gamma, beta, simulator=None):
    """One-layer QAOA for a 2-node graph with one edge."""
    simulator = simulator or cirq.Simulator()
    q0, q1 = cirq.LineQubit.range(2)
    c = cirq.Circuit(cirq.H(q0), cirq.H(q1))
    c.append(cirq.CNOT(q0, q1))
    c.append(cirq.rz(-2 * float(gamma))(q1))
    c.append(cirq.CNOT(q0, q1))
    c.append([cirq.rx(2 * float(beta))(q0), cirq.rx(2 * float(beta))(q1)])
    r = simulator.simulate(c)
    probs = np.abs(r.final_state_vector)**2
    # MaxCut value for bitstring 01/10 is 1.
    return float(probs[1] + probs[2])

def train_vqc(X, y, steps=60, seed=7):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    rng = np.random.default_rng(seed)
    q = cirq.LineQubit(0)
    sim = cirq.Simulator()

    def score(theta, x):
        c = cirq.Circuit(cirq.ry(float(x[0]))(q), cirq.ry(float(theta[0]))(q))
        r = sim.simulate(c)
        return expectation_z(r.final_state_vector)

    def loss(theta):
        pred = np.array([(score(theta, x) + 1) / 2 for x in X])
        eps = 1e-8
        return float(-np.mean(y*np.log(pred+eps) + (1-y)*np.log(1-pred+eps)))

    initial = rng.normal(0, 0.1, 1)
    result = minimize(loss, initial, method="BFGS", options={"maxiter": steps})
    return result, loss(initial), loss(result.x)

def quantum_kernel_matrix(X):
    X = np.asarray(X, dtype=float)
    # Feature state |phi(x)> = Ry(x)|0>, fidelity squared.
    return np.array([
        [np.cos((a[0]-b[0])/2)**2 for b in X] for a in X
    ])

def train_quantum_kernel_svm(X_train, y_train, X_test):
    K = quantum_kernel_matrix(X_train)
    K_test = quantum_kernel_matrix(np.asarray(X_test))[:, :len(X_train)]
    clf = SVC(kernel="precomputed", C=1.0)
    clf.fit(K, y_train)
    return clf.predict(K_test)

def qnn_forward(theta, x):
    q = cirq.LineQubit(0)
    c = cirq.Circuit(cirq.ry(float(x))(q), cirq.ry(float(theta))(q))
    r = cirq.Simulator().simulate(c)
    return expectation_z(r.final_state_vector)

def finite_difference(fn, x, eps=1e-6):
    return (fn(x + eps) - fn(x - eps)) / (2*eps)

def parameter_shift(fn, x, shift=np.pi/2):
    return (fn(x + shift) - fn(x - shift)) / 2
