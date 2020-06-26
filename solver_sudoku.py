def find_empty_space(board):
    """
    find an empty space in the board
    param board: partially complete board
    return: (int, int) the row and the column
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None

def valid_number(board, number, position):
    """
    return if the number fit in the position
    param board: 2d list of ints
    param position: (row, col)
    param number: integer
    return: boolean
    """
    for i in range(9):
        if board[position[0]][i] == number and position[1] != i:
            return False
    for i in range(9):
        if board[i][position[1]] == number and position[0] != i:
            return False
    box_row = (position[0] // 3)*3
    box_column = (position[1] // 3)*3
    for i in range(box_row, box_row+3):
        for j in range(box_column, box_column+3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True


def solve(board):
    """
    solve a sudoku board using backtracking
    param board: 2d list of integers
    return: solution
    """
    space_found = find_empty_space(board)
    if not space_found:
        return True
    else:
        row, col = space_found
    for i in range(1, 10):
        if valid_number(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False



def print_board(board):
    """
    prints the board
    param board: 2d List of integers
    return: None
    """
    for i in range(9):
        if i%3 == 0 and i != 0:
            print("-"*21, sep=' ', end='\n')
        for j in range(9):
            if j%3 == 0 and j != 0:
                print('|', sep=' ', end=' ')
            print(board[i][j], sep=' ', end=' ')
        print(' ')
