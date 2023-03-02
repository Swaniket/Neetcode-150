# URL: https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict

def isValidSudoku(board):
    cols = defaultdict(set) # Key -> Current Column we are in
    rows = defaultdict(set) # Key -> Current Row we are in
    squares = defaultdict(set) # Key -> (r//3, c//3)

    # Iterate over the grid
    for r in range(9):
        for c in range(9):
            # If its an empty space, we can skip it
            if board[r][c] == ".":
                continue
            # Check if it's a duplicate, then we will return false
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]):
                return False
            # If not duplicate, we will update the hashmap
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[((r//3, c//3))].add(board[r][c])

    return True
    
    

if __name__ =="__main__":
    boardFalse = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
    
    boardTrue = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
    
    print(isValidSudoku(boardFalse))