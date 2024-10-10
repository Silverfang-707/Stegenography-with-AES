import random
from math import gcd

# Generate a random prime number p and a random prime number q, and their product n = p * q
p = random.randint(10**5, 10**6)
q = random.randint(10**5, 10**6)
n = p * q

# Find the modular multiplicative inverse d using the Extended Euclidean Algorithm
d = (pow(2, n - 1, n)) % n
print("Private key:", d)

# Compute the public key e and the private key d
e = random.randint(2, n - 1)
while pow(e, d, n) != 1:
    e += 1

def encrypt(n, message):
    ciphertext = []
    for char in message:
        c = ord(char)
        if c < 0 or c > 255:
            raise ValueError("Message must contain only ASCII characters")
        else:
            ciphertext.append((c ** e) % n)
    return ciphertext

def decrypt(n, ciphertext):
    plaintext = []
    for block in ciphertext:
        c = pow(block, d, n)
        if c < 0 or c > 255:
            raise ValueError("Ciphertext must contain only ASCII characters")
        else:
            plaintext.append(chr(c))
    return "".join(plaintext)

message = "Hello, World!"
ciphertext = encrypt(n, message.encode())
print("Encrypted Message:", ciphertext)

plaintext = decrypt(n, ciphertext)
print("Decrypted Message:", plaintext)