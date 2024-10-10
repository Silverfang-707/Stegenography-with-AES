import random
from math import gcd
from functools import lru_cache
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

@lru_cache(maxsize=None)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def generate_keypair(p, g, q):
    a = random.randint(2, p-1)
    x = pow(g, a, p)
    h = (q+1) * a % q
    return x, h

def encrypt_message(m, public_key, private_key):
    g, h = public_key
    k = random.randint(2, 1000)
    r = pow(g, k, p)
    c = ((m - h * k) * modinv(k, p)) % p
    return m, r, c

def sign_message(m, private_key):
    p, q = private_key
    signature = pow(1, m, p) * pow(q, m, p) % p
    return signature

p = 23
g = 5
q = 17
x, h = generate_keypair(p, g, q)
message = "Hello, World!"
m, r, c = encrypt_message(ord(message[0]), (g, h), (p, q))
signature = sign_message(m, (p, q))

print("Public key:", x)
print("Encrypted message:", m, r, c)
print("Signature:", signature)
