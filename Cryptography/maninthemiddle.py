import random

# Simulating Diffie-Hellman Key Exchange
def diffie_hellman(n, g, a, b):
    A = (g**a) % n
    B = (g**b) % n
    key_A = (B**a) % n
    key_B = (A**b) % n
    return key_A, key_B

# Simulating Man-in-the-Middle Attack
def mitm_attack(n, g, a, b, e):
    A = (g**a) % n
    B = (g**b) % n
    A_mitm = (g**e) % n
    B_mitm = (g**e) % n
    key_A_mitm = (B_mitm**a) % n
    key_B_mitm = (A_mitm**b) % n
    return key_A_mitm, key_B_mitm

# Encryption and Decryption using Diffie-Hellman shared keys
def encrypt_decrypt(message, key):
    return ''.join(chr(ord(c) ^ key) for c in message)

# Parameters
n = 23
g = 5
a = random.randint(1, n)
b = random.randint(1, n)
e = random.randint(1, n)

# Diffie-Hellman Key Exchange
key_A, key_B = diffie_hellman(n, g, a, b)
print(f"Key A: {key_A}, Key B: {key_B}")

# Man-in-the-Middle Attack
key_A_mitm, key_B_mitm = mitm_attack(n, g, a, b, e)
print(f"Key A (MitM): {key_A_mitm}, Key B (MitM): {key_B_mitm}")

# Message to be encrypted
message = input("Enter String: ")

# Encryption and decryption without MitM attack
encrypted_message_A = encrypt_decrypt(message, key_A)
decrypted_message_A = encrypt_decrypt(encrypted_message_A, key_A)
print(f"Encrypted Message A: {encrypted_message_A}")
print(f"Decrypted Message A: {decrypted_message_A}")

# Encryption and decryption with MitM attack
encrypted_message_A_mitm = encrypt_decrypt(message, key_A_mitm)
decrypted_message_A_mitm = encrypt_decrypt(encrypted_message_A_mitm, key_A_mitm)
print(f"Encrypted Message A (MitM): {encrypted_message_A_mitm}")
print(f"Decrypted Message A (MitM): {decrypted_message_A_mitm}")
