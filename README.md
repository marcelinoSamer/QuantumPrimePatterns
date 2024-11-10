# QuantumProject
  This project aims to find the probability of finding a Prime number inside a given set of numebrs. This helps in understanding the pattern of prime numbers in Mathematics, demonstrating Riemann's conjecture. This is very important to many computing fields specifically cybersecurity.

  The code will consist of 3 code blocks. The first, generates a random number, using the Quantum Random Number Generator algorithm (QRNG). The second code block transforms this binary number into a decimal number using binary conversion and storing it in a variable. The third and final code block saves this number in a list. These steps are done iterativly N number of times (specified by the user). After the main program loops till end, the final lines execute a ratio between the number of prime numbers inside the list and the total size of the list finding the ratio of prime numbers in this set of numbers.
  
  This is a very efficient and accurate code, as to compute the ratio of prime to natural numbers in a set can be practically impossible for very large N. Our algorithm picks a random sample space from 1 to N, and checks the ratio of prime numbers inside it which will be very close to the real value as the sample space gets bigger.

  This code is more accurate than the mathematical formula $$\frac{1}{\ln(N)}$$, because this formula depends on the asymptotic behavior of the function for very large N. Our code depends on preserving the real value of the ratio despite the size of N.


Notes:
  We needed a virtual environment to be able to test the code locally due to issues with the Aer module. As the virtual environment was very inefficient in space complexity we decided to not include it in the final submission, and substitute it with a notebook which can be run anywhere.

Done by: Marcelino Sedhum, and Abd El-rahman Essam.
