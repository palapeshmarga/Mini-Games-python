import random

def print_board(board):
    """Prints the 9x9 Sudoku board with formatted grid dividers."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def is_valid(board, row, col, num):
    """Checks if placing a number at a specific position is valid."""
    # Check row and column constraints
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
            
    # Check 3x3 subgrid box constraint
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
                # Create a randomized list of digits 1-9
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

def generate_puzzle():
    """Generates a complete board and removes random numbers to create a puzzle."""
    # 1. Start with an empty 9x9 grid
    board = [[0]*9 for _ in range(9)]
    
    # 2. Fill it completely using randomized backtracking
    fill_board(board)
    
    # 3. Randomly remove numbers to make it a playable puzzle
    # Change 45 to a higher number for a harder puzzle (fewer starting numbers)
    cells_to_remove = 45 
    while cells_to_remove > 0:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if board[r][c] != 0:
            board[r][c] = 0
            cells_to_remove -= 1
            
    return board

# Run the generator
random_board = generate_puzzle()
print_board(random_board)

Nums = []
for i in random_board:
    for j in i:
        if j == 0:
            Nums.append("")
        else:
            Nums.append(j)