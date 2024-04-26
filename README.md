# Diffie-Hellman Key Exchange Protocol

## Introduction
This script implements a simplified version of the Diffie-Hellman key exchange protocol, which allows two parties to establish a shared secret key over an insecure channel without prior shared secrets.

## Prerequisites
- Python 3.x
- Required modules: `random`, `math`

## Usage
1. Ensure Python is installed on your system.
2. Run the script `diffie_hellman.py`.
3. The script will generate prime numbers, calculate primitive roots, and simulate the key exchange between Alice and Bob.
4. It will print whether the shared secret keys match.

## How It Works
1. Generate a prime number `p` and a primitive root `g` for the prime number.
2. Generate random private keys `a` and `b` for Alice and Bob respectively.
3. Calculate public keys `A` and `B` for Alice and Bob using the formula `(g ** a) % p` and `(g ** b) % p`.
4. Calculate the shared secret keys `shared_secret_key_A` and `shared_secret_key_B` for Alice and Bob using the formula `(B ** a) % p` and `(A ** b) % p`.
5. Print whether the shared secret keys match.

## Functions
1. `isPrime(number)`: Checks if a given number is prime.
2. `generatePrime()`: Generates a random prime number greater than 10 and less than 100.
3. `primitiveRoot(prime)`: Calculates a primitive root of a given prime number.
4. `printTable(a, b, A, B, Sa, Sb)`: Prints a table with three columns: Alice, Bob, and Eve, showing the values of `a`, `b`, `A`, `B`, and `S` for Alice, Bob, and an eavesdropper Eve.

## Note
- This script provides a basic implementation of the Diffie-Hellman key exchange protocol and is for educational purposes only. It may not be suitable for production environments.
