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
