import random

def is_valid(board, row, col, num):
    """Checks if placing a number at a specific position is valid."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
            
    box_row, box_col = (row // 3) * 3, (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def fill_board(board):
    """Uses randomized backtracking to fill the board with valid numbers."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                
                for num in numbers:
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if fill_board(board):
                            return True
                        board[r][c] = 0  # Backtrack
                return False
    return True

def generate_nums():
    """Generates a playable board and returns a flat 81-element list."""
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)
    
    # Remove numbers to create the puzzle (increase for higher difficulty)
    cells_to_remove = 45 
    while cells_to_remove > 0:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if board[r][c] != 0:
            board[r][c] = 0
            cells_to_remove -= 1
            
    nums = []
    for row in board:
        for val in row:
            nums.append("" if val == 0 else str(val))
    return nums