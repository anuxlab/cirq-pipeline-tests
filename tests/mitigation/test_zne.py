import numpy as np
from qml_ci.mitigation import zero_noise_extrapolation

def test_zero_noise_extrapolation_recovers_intercept():
    noise = np.array([0.0,0.5,1.0])
    values = 0.8 - 0.2*noise
    np.testing.assert_allclose(zero_noise_extrapolation(noise,values),0.8,atol=1e-10)

def test_zne_linear_model():
    noise = np.array([1,2,3],float)
    values = 1.0 + 0.5*noise
    np.testing.assert_allclose(zero_noise_extrapolation(noise,values),1.0,atol=1e-10)
