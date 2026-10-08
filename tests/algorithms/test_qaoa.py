import numpy as np
from qml_ci.algorithms import qaoa_maxcut_expectation

def test_qaoa_objective_is_valid_probability():
    value = qaoa_maxcut_expectation(0.3, 0.2)
    assert 0.0 <= value <= 1.0

def test_qaoa_can_find_nontrivial_cut():
    grid = np.linspace(0, np.pi, 12)
    best = max(qaoa_maxcut_expectation(g,b) for g in grid for b in grid)
    assert best > 0.5
