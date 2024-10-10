def min_occupied_diagonals(n, k):
    total_diagonals = 2 * n - 1
    if k >= total_diagonals:
        return total_diagonals
    else:
        return n + max(0, k - n)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = min_occupied_diagonals(n, k)
    print(result)
