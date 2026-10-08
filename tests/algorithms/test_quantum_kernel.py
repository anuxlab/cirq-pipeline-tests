import numpy as np
from qml_ci.algorithms import quantum_kernel_matrix, train_quantum_kernel_svm

def test_kernel_symmetry_diagonal_psd():
    X = np.array([[-1.0],[-0.2],[0.5],[1.0]])
    K = quantum_kernel_matrix(X)
    np.testing.assert_allclose(K, K.T, atol=1e-12)
    np.testing.assert_allclose(np.diag(K), 1.0, atol=1e-12)
    assert np.min(np.linalg.eigvalsh(K)) > -1e-10

def test_kernel_svm():
    X = np.array([[-1.0],[-0.7],[0.7],[1.0]])
    y = np.array([0,0,1,1])
    pred = train_quantum_kernel_svm(X,y,X)
    assert np.mean(pred == y) >= 0.75
