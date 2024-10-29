from numpy import random
from sudoku import Sudoku as SudokuGenerator

class Sudoku:
    def __init__(self):
        puzzle = SudokuGenerator(3, 3).difficulty(0.7)
        self.board = puzzle.board 
        puzzle.show()  
        print(self.board)     
        
    def solve_sudoku(self, board):
        # Find the first empty cell in the board
        empty_cell = self.find_empty_cell(board)
        
        # If there are no empty cells, the puzzle is solved
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        # Try filling in a digit from 1 to 9 by assigning num
        for num in range(1, 10):
            # after this we try the number if it passes the constrains
            if self.is_valid_move(board, row, col, num):
                # If the move is valid, set the cell to the chosen number
                board[row][col] = num
                
                # Recursively try to solve the rest of the puzzle
                if self.solve_sudoku(board):
                    return True
                
                # If the puzzle cannot be solved with this choice, backtrack
                board[row][col] = None
        
        # If no valid number can be placed, backtrack to the previous cell
        return False

    def find_empty_cell(self, board):
        # Find the first empty cell in the board
        for row in range(9):
            for col in range(9):
                if board[row][col] == None or board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid_move(self, board, row, col, num):
        # Check if the chosen number is valid for the given cell
        return (
            not self.used_in_row(board, row, num) and
            not self.used_in_col(board, col, num) and
            not self.used_in_box(board, row - row % 3, col - col % 3, num)
        )

    def used_in_row(self, board, row, num):
        # Check if the number is used in the same row
        return num in board[row]

    def used_in_col(self, board, col, num):
        # Check if the number is used in the same column
        return num in [board[i][col] for i in range(9)] # i is for the row and col is the index of the number in all rows 

    def used_in_box(self, board, box_start_row, box_start_col, num):
        # Check if the number is used in the 3x3 box
        for i in range(3):
            for j in range(3):
                if board[i + box_start_row][j + box_start_col] == num:
                    return True
        return False

# Example Sudoku board
solver = Sudoku()



if solver.solve_sudoku(solver.board):
    result = SudokuGenerator(3, 3, board=solver.board)
    result.show()
    # for row in solver.board:
    #     print(row)
else:
    print("No solution exists.")