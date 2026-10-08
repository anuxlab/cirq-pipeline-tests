# QML Test Matrix

| Domain | Tests | Failure meaning |
|---|---|---|
| Circuit | unitary/structure/algebra | invalid circuit construction |
| State | Bell/GHZ/normalization | state preparation regression |
| Physics | density trace/hermiticity/PSD | invalid density matrix |
| Encoding | angle/amplitude/feature map | classical-to-quantum boundary bug |
| Measurement | deterministic/correlation | measurement mapping bug |
| Observable | Pauli expectation | expectation implementation bug |
| Gradients | parameter shift/finite diff | differentiation bug |
| Optimization | objective improvement | training loop bug |
| VQE | known ground state | variational algorithm regression |
| QAOA | MaxCut | combinatorial objective regression |
| VQC | classification loss | supervised QML regression |
| QNN | output/optimization | neural quantum model regression |
| Kernel | symmetry/PSD/SVM | kernel feature-map regression |
| Noise | four channels | noisy simulation regression |
| Statistics | shots/seeds | stochastic behavior regression |
| Barren plateau | variance diagnostic | optimization landscape monitoring |
| Validation | NaN/leakage | classical data pipeline bug |
| Hardware | topology | backend constraint violation |
| Mitigation | ZNE | mitigation implementation regression |
| Serialization | JSON roundtrip | persistence regression |
| Performance | runtime/resources | computational regression |
| Integration | end-to-end | full hybrid pipeline failure |
