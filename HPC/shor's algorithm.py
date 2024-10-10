import cirq
import math

# Number to factor
N = 15

# Quantum register
qubits = cirq.LineQubit.range(8)

# Quantum circuit
circuit = cirq.Circuit()

# Hadamard gates
for i in range(4):
    circuit.append(cirq.H(qubits[i]))

# Controlled-U gates
for control in range(4):
    for k in range(2**control):
        circuit.append(cirq.CNOT(qubits[control], qubits[4]))
        circuit.append(cirq.CNOT(qubits[control], qubits[5]))
        circuit.append(cirq.CNOT(qubits[control], qubits[7]))

# Inverse QFT
for i in range(4):
    for j in range(i):
        circuit.append(cirq.CZPowGate(exponent=-0.5/(2**(i-j))).on(qubits[j], qubits[i]))
    circuit.append(cirq.H(qubits[i]))

# Measurement
circuit.append(cirq.measure(*qubits[:4], key='result'))

# Display the circuit
print(circuit)
