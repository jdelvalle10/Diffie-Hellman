# This script implements a simple version of the Diffie-Hellman key exchange protocol.

# Import the random module
import random
# Import the math module
import math


# This function isPrime(number) checks if a given number is prime.

def isPrime(number):
    # Check if the number is 2
    if number == 2:
        # If the number is 2, return True
        return True
    # Check if the number is even
    if number % 2 == 0:
        # If the number is even, return False
        return False
    # Calculate the square root of the number
    sqrt = math.sqrt(number)
    # Convert the square root to an integer
    sqrt = int(sqrt)
    # Iterate from 3 to the square root of the number
    for i in range(3, sqrt + 1, 2):
        # Check if the number is divisible by i
        if number % i == 0:
            # If the number is divisible by i, return False
            return False
    # If the number is not divisible by any number from 3 to the square root of the number, return True
    return True


# This function generates a random prime number greater than 10 and less than 100

def generatePrime():
    # Generate a random number between 10 and 100
    num = random.randint(10, 1000)
    # Check if the number is prime
    while not isPrime(num):
        # If the number is not prime, generate a new number
        num = random.randint(10, 1000)
    # Return the prime number
    return num


#This function calculates a primitive root of a given prime number.

def primitiveRoot(prime):
    # Iterate from 2 to the prime number
    for i in range(2, prime):
        # Initialize a list to store the powers of i
        powers = []
        # Iterate from 1 to the prime number
        for j in range(1, prime):
            # Calculate the power of i modulo the prime number
            power = (i ** j) % prime
            # Check if the power is in the list of powers
            if power in powers:
                # If the power is in the list of powers, break the loop
                break
            # Add the power to the list of powers
            powers.append(power)
        # Check if all the numbers from 1 to the prime number are in the list of powers
        if len(powers) == prime - 1:
            # If all the numbers from 1 to the prime number are in the list of powers, return i
            return i
    # If no primitive root is found, return None
    return None

p = generatePrime()
g = primitiveRoot(p)

print("Prime number p:", p)
print("Primitive root g:", g)

# Now we generate Alice's private key
a = random.randint(1, p - 1)
print("Alice's private key:", a)

# Now we calculate Alice's public key
A = (g ** a) % p
print("Alice's public key:", A)

# Now we generate Bob's private key
b = random.randint(1, p - 1)
print("Bob's private key:", b)

# Now we calculate Bob's public key
B = (g ** b) % p
print("Bob's public key:", B)

# Now Alice and Bob exchange their public keys and calculate the shared secret key

# Alice calculates the shared secret key
shared_secret_key_A = (B ** a) % p
print("Alice's shared secret key:", shared_secret_key_A)

# Bob calculates the shared secret key
shared_secret_key_B = (A ** b) % p
print("Bob's shared secret key:", shared_secret_key_B)

# Check if the shared secret keys are equal
if shared_secret_key_A == shared_secret_key_B:
    print("Shared secret keys match!")

else:
    print("Shared secret keys do not match!")


