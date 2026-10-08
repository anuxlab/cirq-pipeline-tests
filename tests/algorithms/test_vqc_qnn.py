import numpy as np
from qml_ci.algorithms import train_vqc, qnn_forward

def test_vqc_training_improves_loss():
    X = np.array([[-1.0],[-0.8],[0.8],[1.0]])
    y = np.array([0,0,1,1])
    result, initial, final = train_vqc(X,y,steps=50,seed=2)
    assert np.isfinite(final)
    assert final < initial

def test_qnn_output_is_bounded():
    out = qnn_forward(0.4, 0.7)
    assert -1.0 - 1e-10 <= out <= 1.0 + 1e-10
