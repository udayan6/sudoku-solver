import random
from app.solver import solve

def generate_board(difficulty=40):
    """Generates a new Sudoku board with a valid solution and a specific difficulty level"""
    board = [[0 for i in range(9)] for i in range(9)]
    fill_diagonal_boxes(board)
    solve(board)
    remove_numbers(board, difficulty)
    return board

def fill_diagonal_boxes(board):
    """Fill the diagonal 3x3 boxes as they are independent"""
    for i in range(0, 9, 3):
        fill_box(board, i, i)

def fill_box(board, row, col):
    """Fill a 3x3 box with numbers 1-9 without repetition"""
    numbers = random.sample(range(1, 10), 9)
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = numbers[i * 3 + j] #i*3 + j is used to translate from a 1d list to 2d list

def remove_numbers(board, difficulty):
    """Removes a set number of cells from the board to create the puzzle"""
    count = difficulty
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count -= 1