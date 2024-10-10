def extended_euclidean(a, n):
    if a < 0:
        a = -a
    if n == 0:
        return (1, 0, 0)
    if a > n:
        a, n = n, a

    if a == n:
        return (n, 1, 0)

    if n % a == 0:
        return (a, 1, 0)

    gcd, x, y = extended_euclidean(n % a, a)
    if n > a:
        return (gcd, y, x - y * (n // a))
    else:
        return (gcd, x - y * (n // a), y)


def find_inverse(a, n):
    gcd, x, _ = extended_euclidean(a, n)
    if gcd != 1:
        raise ValueError("Inverse does not exist")

    return x


a = int(input("Enter the value of 'a': "))
n = int(input("Enter the value of 'n': "))

x = find_inverse(a, n)

print(f"The modular multiplicative inverse is {x} (mod {n})")