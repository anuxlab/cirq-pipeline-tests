import numpy as np
import pytest
from qml_ci.algorithms import run_vqe

@pytest.mark.slow
def test_vqe_reaches_known_ground_energy():
    result = run_vqe(initial=1.0)
    assert result.fun < -0.999
