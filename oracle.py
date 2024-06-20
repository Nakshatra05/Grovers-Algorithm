from qiskit import QuantumCircuit
import numpy as np

def multiplication_oracle(n, N):
    """Constructs the oracle for the multiplication by N."""
    num_qubits = int(np.ceil(np.log2(N))) + 1
    qc = QuantumCircuit(3 * num_qubits)
    
    # Apply QFT
    qc.append(qft(num_qubits), range(num_qubits, 2*num_qubits))
    
    # Controlled multiplication
    for i in range(num_qubits):
        qc.cx(i, num_qubits + i)
    
    # Apply inverse QFT
    qc.append(qft_dagger(num_qubits), range(num_qubits, 2*num_qubits))
    
    return qc

def qft(n):
    """Creates an n-qubit Quantum Fourier Transform (QFT) circuit."""
    qc = QuantumCircuit(n)
    for qubit in range(n):
        for j in range(qubit):
            qc.cp(np.pi/float(2**(qubit-j)), j, qubit)
        qc.h(qubit)
    return qc

def qft_dagger(n):
    """Creates an n-qubit inverse Quantum Fourier Transform (QFT†) circuit."""
    qc = QuantumCircuit(n)
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi/float(2**(j-m)), m, j)
        qc.h(j)
    return qc

