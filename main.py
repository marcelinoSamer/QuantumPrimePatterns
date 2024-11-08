from qiskit import QuantumCircuit, Aer, execute
from sympy import isprime

#Main quantum function creating the true random numbers
def generate_random_8bit_number():
    qc = QuantumCircuit(8)
    qc.h(range(8)) #applying hadamard gate so its 50-50 chance to be 0 or 1
    qc.measure_all() #measure so it collapse to a value

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1)
    result = job.result()
    counts = result.get_counts()
    binary_number = list(counts.keys())[0]
    return int(binary_number, 2) #returning values as decimals


def main():
    N = int(input("Enter the number of iterations (N): "))
    numbers_list = []

    for _ in range(N):
        number = generate_random_8bit_number()
        numbers_list.append(number)

    prime_count = sum(1 for number in numbers_list if isprime(number))
    prime_ratio = prime_count / N

    print("Generated numbers:", numbers_list)
    print("Number of prime numbers:", prime_count)
    print("Total numbers:", N)
    print("Ratio of prime numbers:", prime_ratio)


main()
