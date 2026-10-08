import numpy as np
import pytest
from qml_ci.data import validate_dataset, assert_no_overlap

def test_dataset_validation():
    X = np.array([[0],[1],[2],[3]])
    y = np.array([0,0,1,1])
    X2,y2 = validate_dataset(X,y)
    assert X2.shape == (4,1)

def test_dataset_rejects_nan():
    with pytest.raises(ValueError):
        validate_dataset(np.array([[np.nan],[1]]), np.array([0,1]))

def test_leakage_detection():
    with pytest.raises(AssertionError):
        assert_no_overlap([1,2,3],[3,4])
