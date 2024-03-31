def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()


def reveal_cell(board, revealed, row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row, new_col = row + i, col + j
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    reveal_cell(board, revealed, new_row, new_col)


def solve_minesweeper(board):
    rows, cols = len(board), len(board[0])
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == -1:
                revealed[row][col] = True

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0 and not revealed[row][col]:
                reveal_cell(board, revealed, row, col)

    return revealed


if __name__ == "__main__":
    minesweeper_board = [
        [0, 0, -1, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, -1, 0, 0]
    ]

    print("Original Minesweeper Board:")
    print_board(minesweeper_board)

    solution = solve_minesweeper(minesweeper_board)

    print("Solution:")
    print_board(solution)
