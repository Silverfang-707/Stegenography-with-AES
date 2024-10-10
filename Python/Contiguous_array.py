def findMaxLength(nums):
    count = 0
    max_length = 0
    table = {0: -1}
    for index, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in table:
            max_length = max(max_length, index - table[count])
        else:
            table[count] = index

    return max_length

nums = list(map(int, input().split()))
print(findMaxLength(nums))
