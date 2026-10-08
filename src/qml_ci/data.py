import numpy as np

def validate_dataset(X, y):
    X = np.asarray(X)
    y = np.asarray(y)
    if X.ndim != 2:
        raise ValueError("X must be 2D")
    if y.ndim != 1 or len(X) != len(y):
        raise ValueError("X/y shape mismatch")
    if not np.all(np.isfinite(X)):
        raise ValueError("X contains non-finite values")
    if len(np.unique(y)) < 2:
        raise ValueError("at least two classes are required")
    return X, y

def assert_no_overlap(train_ids, test_ids):
    if set(train_ids) & set(test_ids):
        raise AssertionError("train/test leakage detected")
