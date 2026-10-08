"""Fast pre-pytest smoke test used to diagnose CI environment failures."""
import importlib

MODULES = [
    "cirq",
    "numpy",
    "scipy",
    "sklearn",
    "qml_ci",
    "qml_ci.algorithms",
    "qml_ci.data",
    "qml_ci.encoding",
    "qml_ci.mitigation",
    "qml_ci.observables",
    "qml_ci.resources",
    "qml_ci.serialization",
    "qml_ci.statistics",
    "qml_ci.topology",
]

for name in MODULES:
    importlib.import_module(name)
    print(f"OK: {name}")
