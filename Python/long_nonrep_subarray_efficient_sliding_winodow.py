def long_str(string):
    seen = set()
    start = 0
    max_len = 0

    for end in range(len(string)):
        while string[end] in seen:
            seen.remove(string[start])
            start += 1
        seen.add(string[end])
        max_len = max(max_len, end - start + 1)

    return max_len

string = input()
print(long_str(string))