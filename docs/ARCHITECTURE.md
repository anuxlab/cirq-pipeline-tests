# Architecture

```text
                    Classical Data
                         |
                Validation / Splits
                         |
                  Feature Encoding
                         |
                 Quantum Circuit
                  /      |       \
             Exact     Noisy     Hardware*
                |         |          |
                +---------+----------+
                          |
                    Measurement
                          |
                     Observable
                          |
                 Loss / Kernel / Cost
                          |
                Gradient / Optimizer
                          |
                    QML Training
                          |
               Metrics / Statistics
                          |
                Regression / CI Gate

* hardware is intentionally isolated from ordinary PR CI.
```

The suite tests each boundary independently and then validates the complete path with
integration tests. This makes failures localizable rather than reporting only that the
final model accuracy changed.
