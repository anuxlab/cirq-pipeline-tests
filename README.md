# Comprehensive QML CI/CD Test Framework

A simulator-first, research-oriented CI/CD test suite for Quantum Machine Learning (QML).
It is designed to test the complete classical-to-quantum-to-classical pipeline without
requiring a paid quantum backend in normal pull-request CI.

## Coverage

- Circuit correctness: unitarity, structure, parameterization, algebraic invariants
- State preparation: Bell/GHZ, normalization, density matrices, entanglement
- Measurement: deterministic measurements and shot-based statistics
- Feature encoding: angle and amplitude encoding, feature maps, invalid inputs
- Observables: expectation values and Hermiticity
- Gradients: parameter-shift and central finite-difference consistency
- Optimization: objective improvement and convergence
- VQE: known ground-state benchmark
- QAOA: small MaxCut instance and objective improvement
- VQC: binary classification and training improvement
- QNN: forward/backward shape and training behavior
- Quantum kernels: symmetry, diagonal, PSD and classical SVM integration
- Noise: depolarizing, bit-flip, phase-flip, amplitude damping
- Shot-vs-exact statistical convergence
- Reproducibility and multi-seed statistics
- Barren-plateau monitoring (diagnostic, not a forced failure)
- Data validation and leakage checks
- Resource/performance regression
- Circuit serialization
- Device topology and transpilation-facing constraints
- Error-mitigation primitive: zero-noise extrapolation
- End-to-end hybrid QML training
- Optional hardware-test boundary

## Run

```bash
python -m pip install -U pip
pip install -e ".[dev]"
pytest
```

Coverage:

```bash
pytest --cov=qml_ci --cov-report=term-missing --cov-report=xml
```

Extended tests:

```bash
pytest -m "slow or nightly"
```

Optional hardware/specialized simulation:

```bash
pip install -e ".[dev,hardware]"
pytest -m hardware
```

## CI philosophy

PR CI should remain deterministic, inexpensive and simulator-only. Real QPU tests are
marked separately because queue time, credentials, calibration drift, backend availability
and cost make them unsuitable for every commit.

The suite deliberately uses mathematical invariants and small known instances wherever
possible. Stochastic tests use fixed seeds and statistical tolerances instead of expecting
bit-for-bit equality from shot sampling.

## Repository layout

```text
qml-ci-complete/
├── .github/workflows/
├── benchmarks/
├── docs/
├── src/qml_ci/
└── tests/
    ├── algorithms/
    ├── circuits/
    ├── encoding/
    ├── gradients/
    ├── hardware/
    ├── integration/
    ├── noise/
    ├── optimization/
    ├── physics/
    ├── regression/
    ├── statistics/
    └── validation/
```
