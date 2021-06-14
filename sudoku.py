import numpy as np
import copy

#This script will create a sudoku board solver by backtracking.
#It will also generate a random sudoku board to solve.
#GUI to come.

#Start with a 3x3 matrix:
board=np.zeros(shape=(9,9))


#Find the first missing cell on the board
def find_empty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y]==0:
                return(x,y)
    return None

#Check if a board is valid
def valid_board(board):
    #Check rows
    for x in range(len(board)):
        if np.count_nonzero(board[x,:]) != np.count_nonzero(np.unique(board[x,:])):
            return False
    #Check columns
    for y in range(len(board[0])):
        if np.count_nonzero(board[:,y]) != np.count_nonzero(np.unique(board[:,y])):
            return False

    #Check each of the 9 non-overlapping 3x3 squares
    squares=[
            range(0,3),
            range(3,6),
            range(6,9)]
    for xsquare in squares:
        for ysquare in squares:
            if np.count_nonzero(board[xsquare,:][:,ysquare]) != np.count_nonzero(np.unique(board[xsquare,:][:,ysquare])):
                return False

    return True


#Now lets write a solver

def board_solver(board):
    #If a cell is missing a number
    find=find_empty(board)
    if find != None:
        row,col = find
        print(row,col)
    else:
        return True

    #For this cell, lets search for a value that would fit
    #This will reduce our search space from 9 values each time to a much smaller set.
    square=board[:,range(3*(col//3),3*(col//3)+3)][range(3*(row//3),3*(row//3)+3),:]
    list_1=np.unique(np.array([board[:,col],board[row,:],np.ndarray.flatten(square)]))
    list_2=np.array(range(1,10))

    #What is in the valid set of values (1-9), which is not in the current row, column, or 3x3 square
    viable=np.setdiff1d(list_2,list_1)

    #For each of these possible set of values
    for val in viable:
        board[row,col]=val
        #If its a valid value
        if valid_board(board):
            #Recall this function to proceed with this value stored
            #If it returns true, the full board is solved, otherwise it will proceed down this path
            #If this path ultimately fails, it will call the next val in value and continue.
            if board_solver(board):
                return True
        board[row,col]=0
    return False


#Function to create a random board
def make_board(nfill):
    name=np.zeros(shape=(9,9))
    #Nfill=the number of values to fill in on the board
    for f in range(1,nfill+1):
        #Generate random numbers
        rng = np.random.default_rng()
        r1 = rng.integers(low=0, high=9, size=1)
        r2 = rng.integers(low=0, high=9, size=1)
        r3 = rng.integers(low=1, high=10, size=1)
        #Try this random value
        name[r1,r2]=r3
        #Keep retrying this as long as the row/columns are not missing a value or the board is invalid
        while (valid_board(name) is False) or (np.count_nonzero(name) == 0):
            r3 = rng.integers(low=1, high=10, size=1)
            name[r1,r2]=r3
    return name


#Example board
board2 = np.array([
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
        ])
