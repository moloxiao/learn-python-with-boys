import time
def solve_sudoku(sudoku_data):
    """
    Solves a Sudoku puzzle and returns the solved board.

    :param sudoku_data: 1D list of integers representing the Sudoku board (0 represents an empty cell)
    :return: Solved Sudoku board as a 1D list
    """
    # Convert the 1D list to a 2D list (9x9)
    board = [sudoku_data[i:i + 9] for i in range(0, len(sudoku_data), 9)]

    def is_valid(num, row, col):
        # Check row
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check 3x3 box
        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if solve():
                                return True
                            board[row][col] = 0
                    return False
        return True

    if solve():
        # Convert back to 1D list before returning
        return [num for row in board for num in row]
    else:
        return "No solution exists"

sudoku_data = [
    8, 4, 0, 1, 0, 0, 9, 0, 0,
    6, 0, 0, 7, 9, 0, 4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 3, 0, 0, 5, 1, 9, 0,
    0, 6, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 8, 0, 7, 5, 0,
    7, 5, 8, 0, 0, 0, 0, 3, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 5,
    0, 0, 0, 0, 2, 0, 8, 7, 0,
]

# Solve the Sudoku puzzle
start_time = time.time()
sudoku_solution = solve_sudoku(sudoku_data)
end_time = time.time()
execution_time = end_time - start_time
print(sudoku_solution)
print(f"My function took {execution_time} seconds to execute.")

