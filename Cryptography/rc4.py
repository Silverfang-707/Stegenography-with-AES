def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

def encrypt(data, key):
    keystream = RC4(key)
    encrypted = bytearray()
    for byte in data:
        encrypted.append(byte ^ next(keystream))
    return encrypted

def decrypt(data, key):
    return encrypt(data, key)  # RC4 is symmetric, so encryption and decryption are the same

# Example usage
if __name__ == "__main__":
    key = b"SecretKey"  # Key should be a byte string
    plaintext = b"Secret Message"  # Plaintext should be a byte string

    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text.decode())
