from qiskit_aer import Aer
from qiskit import QuantumCircuit,transpile
from sympy import isprime
import math

#Main quantum function creating the true random numbers
def generate_random_8bit_number(nOfBits):
    qc = QuantumCircuit(nOfBits)
    qc.h(range(nOfBits)) #applying hadamard gate so its 50-50 chance to be 0 or 1
    qc.measure_all() #measure so it collapse to a value

    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=1)
    result = job.result()
    counts = result.get_counts()
    binary_number = list(counts.keys())[0]
    #print(i)
    return int(binary_number, 2) #returning values as decimals


def main():
    N = int(input("Enter the number of iterations (N): "))
    X = int(input("Enter Max Value of randomely generated number: "))
    Y = math.ceil(math.log2(X+1))
    numbers_list = []

    for i in range(N):
      while True:
          number = generate_random_8bit_number(Y)
          if number <= X and number!=0:
            numbers_list.append(number)
            break

    prime_count = sum(1 for number in numbers_list if isprime(number))
    prime_ratio = prime_count / N

    print("Generated numbers:", numbers_list)
    print("Largest value: ", X)
    print("Number of prime numbers:", prime_count)
    print("Total numbers:", N)
    print("Ratio of prime numbers:", prime_ratio)
    print("Expected ratio: ", 1/(math.log(X)))


main()
