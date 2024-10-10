import random
from math import gcd
from functools import lru_cache

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
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

    b = random.randint(2, q-1)
    y = (q+1) * b % q

    return x, y

def sign_message(m, x, y, q):
    k = random.randint(2, q-1)
    r = pow(g, k, p)
    s = ((m - y * k) * modinv(k, q)) % q
    return m, r, s

p = 23
g = 5
q = 17
x, y = generate_keypair(p, g, q)

message = "Hello, World!"
m, r, s = sign_message(ord(message[0]), x, y, q)

print("Public key:", (x, y))
print("Signature:", m, r, s)