import random
import math

# Function to calculate greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1

# Function to generate keys
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Compute d
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Function to encrypt
def encrypt(pk, plaintext):
    e, n = pk
    return [pow(ord(c), e, n) for c in plaintext]

# Function to decrypt
def decrypt(pk, ciphertext):
    d, n = pk
    return ''.join(chr(pow(c, d, n)) for c in ciphertext)

# Function to sign
def sign(sk, message):
    d, n = sk
    return pow(simple_hash(message), d, n)

# Function to verify
def verify(pk, message, signature):
    e, n = pk
    return pow(signature, e, n) == simple_hash(message)

# Function to hash
def simple_hash(message):
    # Initialize hash value to 0
    hash_value = 0

    # Iterate over each character in the string
    for char in message:
        # Update the hash value based on the ASCII value of the character
        hash_value += ord(char)

    # Return the hash value
    return hash_value

# Test the functions
p = 61
q = 53
public_key, private_key = generate_keys(p, q)
message = "Hello, World!"
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)
signature = sign(private_key, message)
is_valid = verify(public_key, message, signature)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")
print(f"Signature: {signature}")
print(f"Is the signature valid? {is_valid}")