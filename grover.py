from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
import numpy as np

# Function to create a Quantum Fourier Transform (QFT) circuit
def qft(n):
    """Creates an n-qubit QFT circuit."""
    qc = QuantumCircuit(n)
    for qubit in range(n):
        for j in range(qubit):
            qc.cp(np.pi/float(2**(qubit-j)), j, qubit)
        qc.h(qubit)
    return qc

# Function to create an inverse QFT circuit
def qft_dagger(n):
    """Creates an n-qubit QFT† circuit."""
    qc = QuantumCircuit(n)
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi/float(2**(j-m)), m, j)
        qc.h(j)
    return qc

# Function to create the multiplication oracle
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

# Function to construct Grover's algorithm circuit
def grovers_algorithm(N):
    """Constructs Grover's algorithm for factorizing N."""
    num_qubits = int(np.ceil(np.log2(N))) + 1
    grover_circuit = QuantumCircuit(3 * num_qubits, num_qubits)
    
    # Initialize the registers in superposition
    grover_circuit.h(range(num_qubits))
    grover_circuit.h(range(num_qubits, 2*num_qubits))
    
    # Apply the oracle
    grover_circuit.append(multiplication_oracle(num_qubits, N), range(3 * num_qubits))
    
    # Apply Grover's diffusion operator
    for qubit in range(num_qubits):
        grover_circuit.h(qubit)
        grover_circuit.x(qubit)
    
    grover_circuit.h(num_qubits-1)
    grover_circuit.mct(list(range(num_qubits-1)), num_qubits-1)
    grover_circuit.h(num_qubits-1)
    
    for qubit in range(num_qubits):
        grover_circuit.x(qubit)
        grover_circuit.h(qubit)
    
    # Measure the output
    grover_circuit.measure(range(num_qubits), range(num_qubits))
    
    return grover_circuit

# Function to run Grover's algorithm on a simulator
def run_grover(N):
    """Runs Grover's algorithm on a simulator and returns the counts."""
    grover_circuit = grovers_algorithm(N)
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = transpile(grover_circuit, simulator)
    qobj = assemble(compiled_circuit)
    result = execute(compiled_circuit, simulator).result()
    counts = result.get_counts()
    return counts

