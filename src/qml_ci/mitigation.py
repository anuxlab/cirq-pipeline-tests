import numpy as np

def zero_noise_extrapolation(noise_levels, values, degree=1):
    """Polynomial Richardson-style extrapolation to noise level 0."""
    noise_levels = np.asarray(noise_levels, dtype=float)
    values = np.asarray(values, dtype=float)
    if len(noise_levels) != len(values) or len(values) < degree + 1:
        raise ValueError("insufficient extrapolation points")
    coef = np.polyfit(noise_levels, values, degree)
    return float(np.polyval(coef, 0.0))
