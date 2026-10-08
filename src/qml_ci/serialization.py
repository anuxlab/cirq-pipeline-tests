import cirq

def roundtrip_circuit(circuit):
    payload = cirq.to_json(circuit)
    return cirq.read_json(json_text=payload)
