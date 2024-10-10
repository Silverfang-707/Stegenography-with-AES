import cirq
import numpy as np

# Function to create a Grover circuit
def grover_circuit(target_state):
    # Number of qubits
    n = len(target_state)

    # Quantum register
    qubits = cirq.LineQubit.range(n)

    # Quantum circuit
    circuit = cirq.Circuit()

    # Hadamard gates
    circuit.append(cirq.H(qubit) for qubit in qubits)

    # Oracle and diffusion operator
    for _ in range(int(np.pi/4*np.sqrt(2**n))):
        # Oracle
        circuit.append(cirq.X(qubit) for qubit in qubits)
        circuit.append(cirq.H(qubits[-1]))
        # Replace MCX with a combination of CCX and additional gates as necessary
        circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[-1]))
        circuit.append(cirq.H(qubits[-1]))
        circuit.append(cirq.X(qubit) for qubit in qubits)

        # Diffusion operator
        circuit.append(cirq.H(qubit) for qubit in qubits)
        circuit.append(cirq.X(qubit) for qubit in qubits)
        circuit.append(cirq.H(qubits[-1]))
        # Replace MCX with a combination of CCX and additional gates as necessary
        circuit.append(cirq.CCX(qubits[0], qubits[1], qubits[-1]))
        circuit.append(cirq.H(qubits[-1]))
        circuit.append(cirq.X(qubit) for qubit in qubits)
        circuit.append(cirq.H(qubit) for qubit in qubits)

    # Measurement
    circuit.append(cirq.measure(*qubits, key='result'))

    return circuit

# Target state
target_state = '1101'

# Create and print the Grover circuit
circuit = grover_circuit(target_state)
print(circuit)
