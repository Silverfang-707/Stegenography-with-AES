import random

# Generate a random 1000-bit binary string
random_binary_string = ''.join(str(random.randint(0, 1)) for _ in range(1000))

# Function to convert binary string to bytes
def binary_string_to_bytes(binary_string):
    return int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, byteorder='big')

# Convert binary string to bytes
binary_string_bytes = binary_string_to_bytes(random_binary_string)

# SHA-256 constants
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# Initial hash values
H = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
]

# Helper functions
def rotate_right(x, n):
    return (x >> n) | (x << (32 - n)) & 0xFFFFFFFF

def ch(x, y, z):
    return (x & y) ^ (~x & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def sigma_0(x):
    return rotate_right(x, 2) ^ rotate_right(x, 13) ^ rotate_right(x, 22)

def sigma_1(x):
    return rotate_right(x, 6) ^ rotate_right(x, 11) ^ rotate_right(x, 25)

def gamma_0(x):
    return rotate_right(x, 7) ^ rotate_right(x, 18) ^ (x >> 3)

def gamma_1(x):
    return rotate_right(x, 17) ^ rotate_right(x, 19) ^ (x >> 10)

# Padding the message
def pad_message(message):
    ml = len(message)
    message += b'\x80'
    while (len(message) % 64) != 56:
        message += b'\x00'
    message += ml.to_bytes(8, 'big')
    return message

# Main hash function
def sha256(message):
    message = pad_message(message)
    chunks = [message[i:i+64] for i in range(0, len(message), 64)]
    for chunk in chunks:
        w = [0] * 64
        for i in range(16):
            w[i] = int.from_bytes(chunk[i*4:(i+1)*4], 'big')
        for i in range(16, 64):
            w[i] = (gamma_1(w[i-2]) + w[i-7] + gamma_0(w[i-15]) + w[i-16]) & 0xFFFFFFFF
        a, b, c, d, e, f, g, h = H
        for i in range(64):
            T1 = h + sigma_1(e) + ch(e, f, g) + K[i] + w[i]
            T2 = sigma_0(a) + maj(a, b, c)
            h = g
            g = f
            f = e
            e = (d + T1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xFFFFFFFF
        H[0] = (H[0] + a) & 0xFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFF
    return b''.join(x.to_bytes(4, 'big') for x in H)

# Example usage
print("Random binary string:", random_binary_string)
binary_string_bytes = binary_string_to_bytes(random_binary_string)
sha256_hash = sha256(binary_string_bytes)
print("SHA-256 hash:", ''.join(format(byte, '02x') for byte in sha256_hash))
