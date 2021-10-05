#
#
#

import random
import node

##### Functions
def randomizePuzzle():
    random.shuffle(puzzle)

def printPuzzle():
    for i in range(9):
        print(str(puzzle[i]), end = ' ')
        if(((i+1)%3) == 0):
            print(" ", end='\n')
      

def goalCheck():
    if puzzle == goalState:
        return True
    else:
        return False

def moveToEmpty(boardState, emptyIndex, toMoveIndex):
    temp = boardState[toMoveIndex]
    boardState[toMoveIndex] = emptyIndex
    boardState[emptyIndex] = temp

#### "Main"
puzzle = [1,2,3,4,5,6,7,8,0]

goalState = [1,2,3,4,5,6,7,8,0]

#has all adjacent indices
neighbors = {
    0 : [1,3],
    1 : [0,2,4],
    2 : [1,5],
    3 : [4,0,6],
    4 : [3,5,1,7],
    5 : [4,2,8],
    6 : [7,3],
    7 : [6,8,4],
    8 : [7,5],
}

print(goalCheck())

randomizePuzzle()

printPuzzle()
print(goalCheck())

node1 = node.Node(puzzle, 0, goalState)
