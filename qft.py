from qiskit import QuantumCircuit
import numpy as np

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

