def isValidSudoku(board, n):
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                num = int(board[i][j])
                box_index = (i // 3) * 3 + j // 3

                if (num in rows[i]) or (num in cols[j]) or (num in boxes[box_index]):
                    return "NO"
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

    return "YES"

# User input
n = int(input())
board = []
for _ in range(n):
    row = list(map(str, input().split()))
    board.append(row)

print(isValidSudoku(board, n))
