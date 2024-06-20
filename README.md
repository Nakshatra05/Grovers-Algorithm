# Using Grover’s Algorithm for Factorization of Bi-primes

## Introduction

Factoring large composite numbers into their prime factors is a computationally challenging problem with significant implications for cryptography and information security. Traditional algorithms such as RSA encryption rely on the difficulty of factoring large numbers into their primes for their security.

Grover's algorithm, a quantum search algorithm, offers a quadratic speedup over classical algorithms for unstructured search problems. While primarily known for its application in database search, Grover's algorithm has been adapted to address the problem of integer factorization, particularly for bi-prime numbers.

This project demonstrates the implementation of Grover's algorithm using Qiskit, a quantum computing SDK for Python, to factorize bi-prime numbers into their prime components.

## Requirements

To run this project, you need:
- Python 3.7 or higher
- Qiskit (version 0.32.0 or later)
- numpy
- matplotlib

You can install Qiskit and other dependencies using pip:
```bash
pip install qiskit numpy matplotlib
```

## Setup

1. Clone the repository:

```
git clone https://github.com/Nakshatra05/Grovers-Algorithm.git
cd Grovers_Factorization_Project
```

2. Install the dependencies

```
pip install -r requirements.txt
```

## Usage

- Open the Jupyter Notebook:

```
jupyter notebook Grovers_Factorization.ipynb
```

- Execute each cell in the notebook sequentially to run the code.

- Follow the instructions and explanations provided in the notebook.

## File Descriptions

- **Grovers_Factorization.ipynb**: This Jupyter Notebook contains the implementation of Grover's algorithm specifically tailored for factorizing bi-prime numbers into their prime components using quantum computing principles with Qiskit.

- **qft.py**: This Python script defines functions related to the Quantum Fourier Transform (QFT), which is a crucial component in Grover's algorithm. It includes functions for both the QFT and its inverse (QFT†), implemented using Qiskit for quantum circuit simulations.

- **oracle.py**: This Python script defines the multiplication oracle used within Grover's algorithm. The oracle is constructed using controlled operations and Quantum Fourier Transform (QFT) techniques to verify whether the product of two numbers equals a given bi-prime number \( N \).

- **grover.py**: This Python script defines functions that are essential for constructing and executing Grover's algorithm. It includes functions for initializing quantum registers, applying the multiplication oracle, implementing Grover's diffusion operator, and running the algorithm on Qiskit's quantum simulators.

- **utils.py**: This Python script contains utility functions that support various tasks within the project. Utility functions include checking for prime numbers, finding factors of numbers, and verifying factorization results, aiding in the validation and verification steps of the algorithm's output.

- **requirements.txt**: This file lists the Python dependencies required to run the project, ensuring compatibility with the specified versions of Qiskit, numpy, and matplotlib. It simplifies the installation process by allowing users to install all necessary packages using `pip install -r requirements.txt`.

# Using Grover’s Algorithm for Factorization of Bi-primes

## Approach

### Quantum Circuit Components

#### Quantum Fourier Transform (QFT):
- Implemented using controlled-phase gates and Hadamard gates.
- QFT and its inverse (QFT†) are crucial components in the oracle and Grover's algorithm.

#### Multiplication Oracle:
- Constructed using controlled operations and QFT to check if the product of two numbers equals \( N \).

#### Grover's Algorithm:
- Initializes quantum registers in superposition.
- Applies the multiplication oracle to search for factors of \( N \).
- Implements Grover's diffusion operator to amplify the correct solution.

## Execution

- The project utilizes Qiskit's simulation capabilities (QASM simulator) to run Grover's algorithm.
- Measurement results are collected and analyzed to determine the prime factors of bi-prime numbers such as 35, 115, and 893.

## References

- [Quantum Factoring Algorithm using Grover Search](https://arxiv.org/abs/2312.10054) (S. Whitlock and T. D. Kieu)
- [Quantum arithmetic with the Quantum Fourier Transform](https://arxiv.org/abs/1411.5949) (Lidia Ruiz-Perez and Juan Carlos Garcia-Escartin)
- [Basic arithmetic with the quantum Fourier transform (QFT)](https://pennylane.ai/qml/demos/tutorial_qft_arithmetics/) (Pennylane Tutorial)

## Conclusion

This project demonstrates the practical application of quantum computing principles, specifically Grover's algorithm, in solving complex mathematical problems like integer factorization. By leveraging quantum parallelism and interference effects, Grover's algorithm offers a promising approach to addressing computationally intensive tasks traditionally reserved for classical algorithms.
