import sys
input = sys.stdin.readline

def check_row(x, number):
    for i in range(9):
        if number == sudoku_list[x][i]:
            return False
    return True


def check_col(y, number):
    for i in range(9):
        if number == sudoku_list[i][y]:
            return False
    return True


def check_square(x, y, number):
    x1 = (x // 3) * 3
    y1 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if number == sudoku_list[x1 + i][y1 + j]:
                return False
    return True


def recursion(n):
    if n == len(zero_list):
        for i in range(9):
            for j in range(9):
                print(sudoku_list[i][j], end="")
            print()
        exit(0)

    for num in range(1, 10):
        x = zero_list[n][0]
        y = zero_list[n][1]
        if check_row(x, num) and check_col(y, num) and check_square(x, y, num):
            sudoku_list[x][y] = num
            recursion(n + 1)
            sudoku_list[x][y] = 0


sudoku_list = []
zero_list = []
for i in range(9):
    sudoku_list.append(list(map(int, input().rstrip())))

    for j in range(9):
        if sudoku_list[i][j] == 0:
            zero_list.append([i, j])

recursion(0)