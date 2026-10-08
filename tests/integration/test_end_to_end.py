import numpy as np
from qml_ci.algorithms import train_vqc

def test_end_to_end_hybrid_qml_pipeline():
    X = np.array([[-1.0],[-0.5],[0.5],[1.0]])
    y = np.array([0,0,1,1])
    result, initial, final = train_vqc(X,y,steps=60,seed=11)
    assert result.success or np.isfinite(result.fun)
    assert final < initial
