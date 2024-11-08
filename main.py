from qiskit import Aer, QuantumCircuit, execute
import numpy as np
from sympy import isprime


# Function to generate an 8-qubit random number
def generate_random_8qubit_number():
    qc = QuantumCircuit(8)
    qc.h(range(8))  # Apply Hadamard gate to each qubit to create superposition
    qc.measure_all()  # Measure all qubits

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1)
    result = job.result()
    counts = result.get_counts()
    binary_number = list(counts.keys())[0]  # Get the binary result as a string
    return int(binary_number, 2)  # Convert binary to decimal


# Main program
def main():
    N = int(input("Enter the number of iterations (N): "))
    numbers_list = []

    for _ in range(N):
        number = generate_random_8qubit_number()
        numbers_list.append(number)

    # Count prime numbers in the list
    prime_count = sum(1 for number in numbers_list if isprime(number))
    prime_ratio = prime_count / N

    print("Generated numbers:", numbers_list)
    print("Number of prime numbers:", prime_count)
    print("Total numbers:", N)
    print("Ratio of prime numbers:", prime_ratio)


if __name__ == "__main__":
    main()
