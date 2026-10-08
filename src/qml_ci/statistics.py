import numpy as np

def bitstring_counts(simulator, circuit, repetitions=1000, seed=7):
    result = simulator.run(circuit, repetitions=repetitions, seed=seed)
    return result.histogram(key="m")

def sample_mean_and_std(values):
    values = np.asarray(values, dtype=float)
    return float(np.mean(values)), float(np.std(values, ddof=1))

def confidence_interval_mean(values, z=1.96):
    values = np.asarray(values, dtype=float)
    mean = np.mean(values)
    se = np.std(values, ddof=1) / np.sqrt(len(values))
    return float(mean - z*se), float(mean + z*se)

def gradient_statistics(values):
    values = np.asarray(values, dtype=float)
    return {"mean": float(np.mean(values)), "variance": float(np.var(values))}
