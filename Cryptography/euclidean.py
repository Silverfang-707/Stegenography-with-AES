def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Get user inputs
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate GCD
gcd_result = gcd(a, b)
print("GCD of", a, "and", b, "is:", gcd_result)

# Perform extended Euclidean algorithm
gcd, x, y = extended_gcd(a, b)
print("Linear expression of GCD as a sum of", a, "and", b, "is:", gcd, "=", a, "*", x, "+", b, "*", y)
