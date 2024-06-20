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
git clone https://github.com/yourusername/Grovers_Factorization_Project.git
cd Grovers_Factorization_Project
```

2. Install the dependencies

```
pip install -r requirements.txt
```

## Usage

1. Open the Jupyter Notebook:

```
jupyter notebook Grovers_Factorization.ipynb
```

2. Execute each cell in the notebook sequentially to run the code.

3. Follow the instructions and explanations provided in the notebook.

## File Descriptions

Grovers_Factorization.ipynb: Jupyter Notebook containing the implementation of Grover's algorithm for factorization.
grover.py: Python script defining functions to construct and run Grover's algorithm.
oracle.py: Python script defining the multiplication oracle used in Grover's algorithm.
qft.py: Python script defining Quantum Fourier Transform (QFT) functions.
utils.py: Python script containing utility functions.
requirements.txt: List of dependencies for easy installation.

## Approach


Certainly! Here's a final version of your README.md file for the Grover’s Algorithm project on factorization of bi-primes using Qiskit:

markdown
Copy code
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

Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Grovers_Factorization_Project.git
cd Grovers_Factorization_Project
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Open the Jupyter Notebook:

bash
Copy code
jupyter notebook Grovers_Factorization.ipynb
Execute each cell in the notebook sequentially to run the code.

Follow the instructions and explanations provided in the notebook.

File Descriptions
Grovers_Factorization.ipynb: Jupyter Notebook containing the implementation of Grover's algorithm for factorization.
grover.py: Python script defining functions to construct and run Grover's algorithm.
oracle.py: Python script defining the multiplication oracle used in Grover's algorithm.
qft.py: Python script defining Quantum Fourier Transform (QFT) functions.
utils.py: Python script containing utility functions.
requirements.txt: List of dependencies for easy installation.
Approach
Quantum Circuit Components
Quantum Fourier Transform (QFT):
Implemented using controlled-phase gates and Hadamard gates.
QFT and its inverse (QFT†) are crucial components in the oracle and Grover's algorithm.

Multiplication Oracle:
Constructed using controlled operations and QFT to check if the product of two numbers equals 
𝑁
N.

Grover's Algorithm:

Initializes quantum registers in superposition.
Applies the multiplication oracle to search for factors of 
𝑁
N.
Implements Grover's diffusion operator to amplify the correct solution.
Execution
The project utilizes Qiskit's simulation capabilities (QASM simulator) to run Grover's algorithm.
Measurement results are collected and analyzed to determine the prime factors of bi-prime numbers such as 35, 115, and 893.
References
Quantum Factoring Algorithm using Grover Search (S. Whitlock and T. D. Kieu)
Quantum arithmetic with the Quantum Fourier Transform (Lidia Ruiz-Perez and Juan Carlos Garcia-Escartin)
Basic arithmetic with the quantum fourier transform (QFT) (Pennylane Tutorial)
Conclusion
This project demonstrates the practical application of quantum computing principles, specifically Grover's algorithm, in solving complex mathematical problems like integer factorization. By leveraging quantum parallelism and interference effects, Grover's algorithm offers a promising approach to addressing computationally intensive tasks traditionally reserved for classical algorithms.

For further exploration and improvement, consider experimenting with larger bi-prime numbers and optimizing quantum circuit implementations.
